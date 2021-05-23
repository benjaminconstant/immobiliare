import scrapy
from backend.models import House, Search, Image
from ..items import HouseItem
import re
from django.utils import timezone
from datetime import datetime, timedelta
import locale
locale.setlocale(locale.LC_ALL, 'it_IT')


class ImmobiliareSpider(scrapy.Spider):
    name = "immobiliare"
    STATE_CHOICES = {
        'Da ristrutturare': 1,
        'Buono / Abitabile': 2,
        'Ottimo / Ristrutturato': 3,
        'Nuovo / In costruzione': 4,
        'N.D.': 5
    }

    def start_requests(self):
        for search in Search.objects.filter(platform=1):
            page = 0
            yield scrapy.Request(url=search.link, callback=self.parse, cb_kwargs=dict(search=search, page=page))

    def parse(self, response, search, page):

        house_counter = response.css('span.visible-xs-inline::text').get()
        house_container = response.css('li.listing-item.js-row-detail')
        page += 1
        print('pag: ' + str(page) + ' ' + search.name + ' ' + '(' + str(len(house_container)) + ' annunci)')

        for house in house_container:
            h = HouseItem()
            h['search'] = search
            h['uid'] = house.css('::attr(data-id)').get()
            try:
                h['price'] = float(house.css('li.lif__item.lif__pricing::text').get().strip().split('€ ')[1].replace('.', ''))
            except:
                h['price'] = float(house.css('li.lif__item.lif__pricing > div::text').get().strip().split('€ ')[1].replace('.', ''))
            h['title'] = house.css('p.titolo.text-primary > a::text').get().strip()
            h['link'] = house.css('p.titolo.text-primary > a::attr(href)').get()
            h['mq'] = int(house.xpath('.//div[text()[contains(., "superficie")]]/preceding-sibling::div/span/node()').get().replace('.', ''))
            h['price_mq'] = round(h['price']/h['mq'], 2)

            obj, created = House.objects.get_or_create(uid=h['uid'], search=search)
            obj.title = h['title']
            obj.price = h['price']
            obj.link = h['link']
            obj.mq = h['mq']
            obj.price_mq = h['price_mq']
            obj.has_changed = True
            obj.save()

            print(('created: ' if created else 'updated: ') + obj.link + ' ' + h['search'].name)

            yield scrapy.Request(h['link'], self.parse_detail, cb_kwargs=dict(h=h))

        next_page = response.css('a[title="Pagina successiva"]::attr(href)').get()
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse, cb_kwargs=dict(search=search, page=page))

    def parse_detail(self, response, h):
        h['text'] = ''.join(response.css('div.im-description__text.js-readAllText::text').getall()).strip()
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

        h['is_private'] = response.css('div.im-lead__supervisor > div > p::text').get() == 'Privato'

        obj_list = House.objects.filter(uid=h['uid'])
        for obj in obj_list:
            obj.state = h['state']
            obj.text = h['text']
            obj.costs = h['costs']
            obj.date_publish = h['date_publish']
            obj.is_private = h['is_private']
            obj.save()

            for image in response.css('img.nd-ratio__img::attr(src)').getall()[:3]:
                i = Image.objects.get_or_create(house=obj, url=image)

            print('deep updated: ' + obj.link)


class CasaDaPrivatoSpider(scrapy.Spider):
    name = "casadaprivato"

    def start_requests(self):
        page = 0
        start_urls = [
            'https://www.casadaprivato.it/annunci-vendita/immobili/monza_brianza-arcore',
            'https://www.casadaprivato.it/annunci-vendita/immobili/monza_brianza-camparada',
            'https://www.casadaprivato.it/annunci-vendita/immobili/monza_brianza-carnate',
            'https://www.casadaprivato.it/annunci-vendita/immobili/monza_brianza-correzzana',
            'https://www.casadaprivato.it/annunci-vendita/immobili/monza_brianza-lesmo',
            'https://www.casadaprivato.it/annunci-vendita/immobili/monza_brianza-triuggio',
            'https://www.casadaprivato.it/annunci-vendita/immobili/monza_brianza-usmate_velate',
            'https://www.casadaprivato.it/annunci-vendita/immobili/monza_brianza-villasanta',
            'https://www.casadaprivato.it/annunci-vendita/immobili/monza_brianza-vimercate',
            'https://www.casadaprivato.it/annunci-vendita/immobili/lecco-casatenovo'
        ]
        for search in Search.objects.filter(platform=2):
            for url in start_urls:
                page = 0
                yield scrapy.Request(url=url, callback=self.parse, cb_kwargs=dict(page=page, search=search,))

    def parse(self, response, page, search):
        detail_url_list = response.css('div.info > h3 > a::attr(href)').getall()
        page += 1

        print('pag: ' + str(page) + ' ' + search.name + ' ' + response.url + ' ' + '(' + str(len(detail_url_list)) + ' annunci)')
        for url in detail_url_list:
            yield scrapy.Request('https://www.casadaprivato.it' + url, callback=self.parse_detail, cb_kwargs=dict(search=search))

        next_page = response.css('li.next > a::attr(href)').get()
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse, cb_kwargs=dict(page=page, search=search))

    def parse_detail(self, response, search):
        h = HouseItem()
        h['uid'] = response.xpath('//dt[text()[contains(., "Riferimento")]]/following-sibling::dd/node()').get()
        title = response.css('div#titlebar > div > h1::text').get().strip()
        address = ''.join(response.css('div#titlebar > div > span::text').getall()).strip().replace('(Monza e Brianza)', '')
        h['title'] = '-'.join([title, address])
        h['link'] = response.url
        try:
            h['price'] = int(response.css('div.price > span::text').get().strip().split('€ ')[1].replace('.', ''))
        except:
            h['price'] = 0

        h['mq'] = int(response.xpath('.//li[text()[contains(., " mq")]]/text()').get().replace(' mq', ''))
        h['price_mq'] = round(h['price']/h['mq'], 2)
        date = response.css('ul.contact-us > li > span::text').get().replace('Aggiornato al ', '').replace('Annuncio del ', '')
        h['date_publish'] = datetime.strptime(date, '%d %b %Y').date()

        h['text'] = response.css('div.section-data > div.col-sm-12.section-margin.text-justify::text').get().strip()

        if h['price'] <= 100000:
            obj, created = House.objects.get_or_create(uid=h['uid'], search=search)
            obj.title = h['title']
            obj.link = h['link']
            obj.price = h['price']
            obj.mq = h['mq']
            obj.price_mq = h['price_mq']
            obj.date_publish = h['date_publish']
            obj.text = h['text']
            obj.has_changed = True
            obj.save()
            print(('created: ' if created else 'updated: ') + obj.link + ' ' + search.name)

            for image in response.css('div.item > img::attr(src)').getall()[:3]:
                i = Image.objects.get_or_create(house=obj, url=image)
