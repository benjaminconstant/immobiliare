from backend.models import House
from django.core.management.base import BaseCommand
from django.apps import apps


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '-m',
            required=True,
            help='model to delete',
            type=str
        )

    def handle(self, *args, **options):
        model = options.get('m')
        apps.get_model('backend', model).objects.all().delete()
        print('deleted ' + model)
