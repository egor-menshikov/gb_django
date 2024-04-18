from django.core.management.base import BaseCommand

from ...models import User


class Command(BaseCommand):
    help = 'Create user.'

    def handle(self, *args, **options):
        user = User(
            name='Trinity',
            email='trinity@zion.com',
            password='secret',
            age=33,
        )
        user.save()

        user = User(
            name='Neo',
            email='neo@zion.com',
            password='imsocool',
            age=31,
        )
        user.save()

        user = User(
            name='Morpheus',
            email='boss@zion.com',
            password='1234',
            age=52,
        )
        user.save()

        self.stdout.write(f'{user}')
