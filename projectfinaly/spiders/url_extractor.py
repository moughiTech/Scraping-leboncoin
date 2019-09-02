# -*- coding: utf-8 -*-
import scrapy
#rom scrapy.loader import ItemLoader
#from projectfinaly.items import urlItem

#Role: extracting the Offers URL's from the parsed pages
#This spider should be called with a file named urls.json as output
class UrlExtractorSpider(scrapy.Spider):
    name = 'url_extractor'
    allowed_domains = ['leboncoin.fr/recherche/?category=9']
    start_urls = ['https://www.leboncoin.fr/recherche/?category=9&locations=Massy_91300',
                  'https://www.leboncoin.fr/recherche/?category=9&locations=Massy_91300&page=2',
                  'https://www.leboncoin.fr/recherche/?category=9&locations=Massy_91300&page=3',
                  'https://www.leboncoin.fr/recherche/?category=9&locations=Massy_91300&page=4',
                  'https://www.leboncoin.fr/recherche/?category=9&locations=Massy_91300&page=5',
                  'https://www.leboncoin.fr/recherche/?category=9&locations=Massy_91300&page=6',
                  'https://www.leboncoin.fr/recherche/?category=9&locations=Massy_91300&page=7',]

    def parse(self, response):
        yield {
            'url_page_offers': response.xpath("//li[@class='_3DFQ-']/a/@href").extract(),
        }
        
