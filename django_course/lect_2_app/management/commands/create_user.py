from django.core.management.base import BaseCommand

from lect_2_app.models import User


class Command(BaseCommand):
    help = 'Create user.'

    def handle(self, *args, **options):
        user = User(
            name='Egor',
            email='r@g.com',
            password='secret',
            age=38,
        )
        user.save()
        self.stdout.write(f'{user}')
