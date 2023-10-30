import logging

from apps.contacts.models import Contact
from apps.contacts.services.faker_init import faker


def generate_and_save_contact(amount: int):
    logger = logging.getLogger("django")

    queryset = Contact.objects.all()

    logger.info(f"Current amount of contacts before: {queryset.count()}")

    for _ in range(amount):
        Contact.objects.create(
            name=faker.unique.user_name(),
            email=faker.unique.company_email(),
            phone=faker.unique.phone_number(),
            address=faker.unique.address()
        )

    logger.info(f"Current amount of contacts after: {queryset.count()}")
