import scrapy
from backend.models import House, Search
from ..items import HouseItem
import re
from django.utils import timezone
from datetime import datetime, timedelta


class ImmobiliareSpider(scrapy.Spider):
    name = "scraper"
    STATE_CHOICES = {
        'Da ristrutturare': 1,
        'Buono / Abitabile': 2,
        'Ottimo / Ristrutturato': 3,
        'Nuovo / In costruzione': 4,
        'N.D.': 5
    }
    House.objects.all().update(has_changed=False)
    for house in House.objects.all():
        house.searches.clear()

    def start_requests(self):
        for search in Search.objects.all():
            page = 0
            yield scrapy.Request(url=search.link, callback=self.parse, cb_kwargs=dict(search=search, page=page))

    def parse(self, response, search, page):

        house_counter = response.css('span.visible-xs-inline::text').get()
        house_container = response.css('li.listing-item.js-row-detail')
        page += 1
        print('pag: ' + str(page) + ' ' + search.name + ' ' + '(' + str(len(house_container)) + ' annunci)')

        for house in house_container:
            h = HouseItem()
            h['search_name'] = search.name
            h['uid'] = house.css('::attr(data-id)').get()
            try:
                h['price'] = float(house.css('li.lif__item.lif__pricing::text').get().strip().split('€ ')[1].replace('.', ''))
            except:
                h['price'] = float(house.css('li.lif__item.lif__pricing > div::text').get().strip().split('€ ')[1].replace('.', ''))
            h['title'] = house.css('p.titolo.text-primary > a::text').get().strip()
            h['link'] = house.css('p.titolo.text-primary > a::attr(href)').get()
            h['mq'] = float(house.xpath('.//div[text()[contains(., "superficie")]]/preceding-sibling::div/span/node()').get())
            h['price_mq'] = round(h['price']/h['mq'], 2)

            obj, created = House.objects.get_or_create(id=h['uid'])
            obj.title = h['title']
            obj.price = h['price']
            obj.link = h['link']
            obj.mq = h['mq']
            obj.price_mq = h['price_mq']
            obj.has_changed = True
            obj.searches.add(search.id)
            obj.save()

            if created:
                print('created: ' + obj.link + ' ' + h['search_name'])
            else:
                print('updated: ' + obj.link + ' ' + h['search_name'])

            yield scrapy.Request(h['link'], self.parse_house, cb_kwargs=dict(h=h))

        next_page = response.css('a[title="Pagina successiva"]::attr(href)').get()
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse, cb_kwargs=dict(search=search, page=page))

    def parse_house(self, response, h):
        h['text'] = ''.join(response.css('div.im-description__text.js-readAllText::text').extract()).strip()
        date_raw = response.xpath('//dt[text()[contains(., "riferimento e Data annuncio")]]/following-sibling::dd/node()').get().strip()
        match = re.search('\d{2}/\d{2}/\d{4}', date_raw)
        h['date_publish'] = datetime.strptime(match.group(), '%d/%m/%Y').date()

        try:
            h['costs'] = response.xpath('//dt[text()[contains(., "spese condominio")]]/following-sibling::dd/node()').get().strip()
            if h['costs'] == 'Nessuna spesa condominiale':
                h['costs'] = 0
            else:
                h['costs'] = int(h['costs'].replace('€ ', '').replace('.', '').replace('/', '').replace('mese', ''))
        except:
            h['costs'] = -1

        try:
            h['state'] = self.STATE_CHOICES[response.xpath('//dt[text()[contains(., "stato")]]/following-sibling::dd/node()').get().strip()]
        except:
            h['state'] = self.STATE_CHOICES['N.D.']

        obj = House.objects.get(id=h['uid'])
        obj.state = h['state']
        obj.text = h['text']
        obj.costs = h['costs']
        obj.date_publish = h['date_publish']
        obj.save()

        print('deep updated: ' + obj.link + ' ' + h['search_name'])

    def closed(self, reason):
        not_updated = House.objects.filter(has_changed=False)
        for house in not_updated:
            print('deleting: ' + house.link)
        not_updated.delete()
