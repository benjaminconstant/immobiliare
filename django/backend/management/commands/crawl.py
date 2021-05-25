import os
from scrapy.utils.project import get_project_settings
from django.core.management.base import BaseCommand
from backend.models import House
from scrapy.crawler import CrawlerProcess
from scraper.scraper.spiders.spider import ImmobiliareSpider, CasaDaPrivatoSpider


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '-p',
            default='all',
            help='platform to scrape',
            type=str
        )

    def handle(self, *args, **options):
        # platform = options.get('p')
        os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'scraper.scraper.settings')
        process = CrawlerProcess(get_project_settings())

        House.objects.all().update(has_changed=False)

        process.crawl(CasaDaPrivatoSpider)
        process.crawl(ImmobiliareSpider)
        process.start()

        not_updated = House.objects.filter(has_changed=False)
        for house in not_updated:
            print('deleting: ' + house.link)
        not_updated.delete()
