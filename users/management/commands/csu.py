from django.core.management import BaseCommand

from users.models import User

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='bong@rambler.ru',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('Sergo1234')
        user.save()