from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from rest_framework import generics

from apps.contacts.forms import GenerateForm
from apps.contacts.models import Contact
from apps.contacts.serializers import ContactSerializer
from apps.contacts.services.delete_contacts import delete_contacts
from apps.contacts.services.generate_and_save_contact import generate_and_save_contact


class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


def generate_contacts_view(request):
    if request.method == "POST":
        form = GenerateForm(request.POST)

        if form.is_valid():
            amount = form.cleaned_data["amount"]

            generate_and_save_contact(amount=amount)
    else:
        form = GenerateForm()

    return render(
        request=request,
        template_name="contacts/contacts_generate.html",
        context=dict(
            users_list=Contact.objects.all(),
            form=form,
        ),
    )


def delete_contacts_view(request):
    delete_contacts()

    return redirect(reverse_lazy("base:home_page"))
