from django.core.management import BaseCommand

from ...models import User


class Command(BaseCommand):
    help = 'Delete user.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User_id')

    def handle(self, *args, **options):
        if user := User.objects.filter(pk=options.get('pk')).first():
            self.stdout.write(f'{user}')
            user.delete()
        else:
            self.stdout.write('No such user.')
