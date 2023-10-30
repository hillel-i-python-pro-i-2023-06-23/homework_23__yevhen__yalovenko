from django.urls import path

from . import views
from .views import ContactList, ContactDetail

app_name = "contacts"

urlpatterns = [
    path('list/', ContactList.as_view(), name='contact-list'),
    path('<int:pk>/', ContactDetail.as_view(), name='contact-detail'),
    path("generate/", views.generate_contacts_view, name="contacts_generate"),
    path("delete/", views.delete_contacts_view, name="contacts_delete"),
]
