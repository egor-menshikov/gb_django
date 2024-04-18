from django.core.management import BaseCommand

from ...models import User


class Command(BaseCommand):
    help = 'Update user age.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User_ID')
        parser.add_argument('age', type=int, help='User_age')

    def handle(self, *args, **options):
        age = options.get('age')
        pk = options.get('pk')
        user = User.objects.filter(pk=pk).first()
        user.age = age
        user.save()
        self.stdout.write(f'{user}')
