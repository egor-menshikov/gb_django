from django.core.management.base import BaseCommand
from ...models import User


class Command(BaseCommand):
    help = "Get user by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        user = User.objects.filter(pk=pk).first()
        self.stdout.write(f'{user}')

    # def handle(self, *args, **kwargs):
    #     user = User.objects.filter(pk__range=(0, 12))
    #     self.stdout.write(f'{user}')

# class Command(BaseCommand):
#     help = "Get user by id."
#
#     def add_arguments(self, parser):
#         parser.add_argument('id', type=int, help='User ID')
#
#     def handle(self, *args, **kwargs):
#         id = kwargs['id']
#         user = User.objects.get(id=id)
#         self.stdout.write(f'{user}')
