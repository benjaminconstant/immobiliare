import os
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
        for search in Search.objects.filter(platform=1, is_active=True):
            page = 0
            yield scrapy.Request(url=search.link, callback=self.parse, cb_kwargs=dict(search=search, page=page), meta={'selenium': True})

    def parse(self, response, search, page):
        # with open(os.getcwd() + '/' + response.url[-15:] + '.html', 'wb') as f:
        #    f.write(response.body)
        ad_url_list = response.css('a.in-card__title::attr(href)').getall()
        page += 1
        print('pag: ' + str(page) + ' ' + search.name + ' ' + '(' + str(len(ad_url_list)) + ' annunci)')

        for url in ad_url_list:
            obj, created = House.objects.get_or_create(uid=url.split('/')[-2], search=search)
            if created:
                print('created: ' + url + ' search: ' + search.name)
            yield scrapy.Request(url=url, callback=self.parse_detail, cb_kwargs=dict(search=search))

        next_page = response.css('div[data-cy="pagination-next"] > a.in-pagination__item::attr(href)').get()
        if next_page is not None:
            yield scrapy.Request(url=next_page, callback=self.parse, cb_kwargs=dict(search=search, page=page), meta={'selenium': True})

    def parse_detail(self, response, search):
        h = HouseItem()
        h['search'] = search
        h['uid'] = response.url.split('/')[-2]
        h['text'] = ''.join(response.css('div.im-description__text.js-readAllText::text').getall()).strip()
        tag_list = ' '.join(''.join(response.css('span.im-features__tag::text').getall()).split())
        h['text'] = 'TAGS: '.join(h['text'], tag_list)
        price_raw = response.css('div.im-mainFeatures__title').get().replace('.', '')
        h['price'] = float(re.findall('\d+', price_raw)[0])
        mq_raw = response.xpath('//dt[text()[contains(., "superficie")]]/following-sibling::dd/node()').get().replace('.', '')
        h['mq'] = int(re.findall('\d+', mq_raw)[0])
        h['price_mq'] = round(h['price']/h['mq'], 2)
        h['title'] = response.css('span.im-titleBlock__title::text').get()
        h['link'] = response.url
        h['is_private'] = response.css('div.im-lead__supervisor > div > p::text').get() == 'Privato'

        # date
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

        obj_list = House.objects.filter(uid=h['uid'])
        for obj in obj_list:
            obj.date_publish = h['date_publish']
            obj.title = h['title']
            obj.link = h['link']
            obj.state = h['state']
            obj.text = h['text']
            obj.price = h['price']
            obj.price_mq = h['price_mq']
            obj.mq = h['mq']
            obj.costs = h['costs']
            obj.is_private = h['is_private']
            obj.has_changed = True
            obj.save()
            for image in response.css('img.nd-ratio__img::attr(src)').getall()[:3]:
                i = Image.objects.get_or_create(house=obj, url=image)
            print(('updated: ') + obj.link + ' ' + h['search'].name)


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
        for search in Search.objects.filter(platform=2, is_active=True):
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

        if h['price'] <= 120000:
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
