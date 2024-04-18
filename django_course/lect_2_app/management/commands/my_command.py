from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Prints 'Hello world'"

    def add_arguments(self, parser):
        parser.add_argument('num', type=int, help='Number')

    def handle(self, *args, **options):
        self.stdout.write(f'Hello world {options['num']}')
