import logging

from django.core.management.base import BaseCommand

from apps.contacts.models import Contact


class Command(BaseCommand):
    def handle(self, *args, **options):
        logger = logging.getLogger("django")

        queryset = Contact.objects.all()
        logger.info(f"Current amount of contacts before: {queryset.count()}")

        total_deleted, details = queryset.delete()
        logger.info(f"Total deleted: {total_deleted}, details: {details}")

        logger.info(f"Current amount of contacts after: {queryset.count()}")
