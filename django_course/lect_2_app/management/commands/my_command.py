from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Prints 'Hello world'"

    def handle(self, *args, **options):
        self.stdout.write('Hello world')
