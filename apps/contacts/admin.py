from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "address", "email")
    list_filter = ("name", "phone", "address", "email")
    search_fields = ("name", "phone", "email")
