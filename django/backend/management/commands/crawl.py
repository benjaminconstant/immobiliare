import os
from scrapy.utils.project import get_project_settings
from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scraper.scraper.spiders.spider import ImmobiliareSpider


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
        os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'scraper.scraper.settings')
        process = CrawlerProcess(get_project_settings())
        process.crawl(ImmobiliareSpider)
        process.start()
