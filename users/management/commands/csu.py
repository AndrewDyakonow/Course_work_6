import os

from django.core.management import BaseCommand

from users.models import Users


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = Users.objects.create(
            email=os.getenv('EMAIL_SUPERUSER'),
            first_name='Admin',
            last_name='SkyPro',
            is_staff=True,
            is_superuser=True
        )

        user.set_password(os.getenv('PASSWORD_SUPERUSER'))
        user.save()
