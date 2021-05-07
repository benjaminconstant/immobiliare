from backend.models import House
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '-p',
            action='store',
            default='all',
            help='platform to scrape',
            type=str
        )

    def handle(self, *args, **options):
        # platform = options.get('p')
        high_costs_list = House.objects.filter(costs__gt=50)
        for house in high_costs_list:
            house.is_hidden = True
            house.save()
            print(house.link)
