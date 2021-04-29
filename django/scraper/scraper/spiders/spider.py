import scrapy
from backend.models import House
from ..items import HouseItem
import re
from django.utils import timezone
from datetime import datetime, timedelta


class ImmobiliareSpider(scrapy.Spider):
    name = "scraper"
    start_urls = ['https://www.immobiliare.it/ricerca.php?idCategoria=1&idContratto=1&idNazione=IT&prezzoMassimo=90000&superficieMinima=60&criterio=prezzo&ordine=asc&noAste=1&pag=1&vrt=45.593861,9.260101;45.565626,9.328594;45.578003,9.394684;45.624123,9.409275;45.659887,9.421978;45.684957,9.384899;45.684837,9.323959;45.680759,9.279671;45.658208,9.24551;45.593861,9.260101']
    page = 0
    yesterday = timezone.now() - timedelta(1)
    disappered = House.objects.filter(updated__lte=yesterday)
    print('deleting ' + str(len(disappered)) + ' annunci rimossi')
    for house in disappered:
        print(house.link)
    disappered.delete()

    def parse(self, response):

        house_counter = response.css('span.visible-xs-inline::text').get()
        house_container = response.css('li.listing-item.js-row-detail')
        self.page += 1
        print('pag: ' + str(self.page) + ' ' + '(' + str(len(house_container)) + ' annunci)')

        for house in house_container:
            h = HouseItem()
            h['uid'] = house.css('::attr(data-id)').get()
            try:
                h['price'] = float(house.css('li.lif__item.lif__pricing::text').get().strip().split('€ ')[1].replace('.', ''))
            except:
                h['price'] = float(house.css('li.lif__item.lif__pricing > div::text').get().strip().split('€ ')[1].replace('.', ''))
            h['title'] = house.css('p.titolo.text-primary > a::text').get().strip()
            h['link'] = house.css('p.titolo.text-primary > a::attr(href)').get()
            h['mq'] = float(house.xpath('.//div[text()[contains(., "superficie")]]/preceding-sibling::div/span/node()').get())
            h['price_mq'] = round(h['price']/h['mq'], 2)
            try:
                existingHouse = House.objects.get(id=h['uid'])
                existingHouse.price = h['price']
                existingHouse.title = h['title']
                existingHouse.link = h['link']
                existingHouse.mq = h['mq']
                existingHouse.price_mq = h['price_mq']
                existingHouse.save()
            except:
                yield scrapy.Request(h['link'], self.parse_house, cb_kwargs=dict(h=h))

        next_page = response.css('a[title="Pagina successiva"]::attr(href)').get()
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse)

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
            h['costs'] = None

        House.objects.create(
            id=h['uid'],
            title=h['title'],
            price=h['price'],
            link=h['link'],
            mq=h['mq'],
            text=h['text'],
            price_mq=h['price_mq'],
            costs=h['costs'],
            date_publish=h['date_publish']
        )
        print(h['link'])
