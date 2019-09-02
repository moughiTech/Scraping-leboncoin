# -*- coding: utf-8 -*-
import scrapy
import json
import re
from scrapy.loader import ItemLoader
from projectfinaly.items import offerItem
#from pymongo import MongoClient

class OfferScraperSpider(scrapy.Spider):

    name = 'offer_scraper'
    #The allowed domain
    allowed_domains = ['leboncoin.fr/recherche/?category=9&locations=Massy_91300']

    #Importing the urls scraped by url_extractor' spider
    with open('urls2.json','r') as f:
        urls_dics = json.load(f)

    urls_list=[]
    for dic in urls_dics:
        temp_var1= dic['url_page_offers']
        urls_list= urls_list+temp_var1

    urls_ready=[]
    for i in range(len(urls_list)):
        urls_ready+=['https://www.leboncoin.fr'+urls_list[i]]

    #parsing the extracted urls
    start_urls = urls_ready

    def parse(self, response):

        yield{
            'type_bien': response.xpath(".//div[starts-with(text(),'Type de bien')]/following-sibling::node()/text()").extract(),
            'piece': response.xpath("//div[starts-with(text(),'Pièces')]/following-sibling::node()/text()") .extract(),
            'surface': response.xpath(".//div[starts-with(text(),'Surface')]/following-sibling::node()/text()").extract()[0],
            'ges': response.xpath("//div[contains(@data-qa-id,'criteria_item_ges')]/descendant::node()[@class='_2RkBA _3ATYZ _1sd0z']/text()").extract(),
            'classe_energie': response.xpath(".//div[contains(@data-qa-id,'criteria_item_energy_rate')]/descendant::node()[@class='_2RkBA _3ATYZ _1sd0z']/text()").extract(),

            'nom_annonce': response.xpath(".//h1/text()").extract(),
            'prix': response.xpath(".//div[@class='_14taM']//span[@class='_1F5u3']/text()").extract_first(),
            'date_annonce': response.xpath(".//div[@data-qa-id='adview_date']/text()").extract(),
            'description': re.sub(r"\d+\">",'',response.xpath("//span[@class='content-CxPmi']").extract()[0].replace('</span>','').replace('<br>','').replace(("<span class=\"content-CxPmi\" data-reactid=\""),''))
        }
        

     ## Pour stocker les données dans un bd mongodb, on utilise le code suivant.   
     #   loader= ItemLoader(item=offerItem(), response=response)
     #   loader.add_xpath("type_bien", "//div[starts-with(text(),'Type de bien')]/following-sibling::node()/text()")
     #   loader.add_xpath("piece", "//div[starts-with(text(),'Pièces')]/following-sibling::node()/text()")
     #   loader.add_xpath("surface", "//div[starts-with(text(),'Surface')]/following-sibling::node()/text()")
     #   loader.add_xpath("ges", "//div[contains(@data-qa-id,'criteria_item_ges')]/descendant::node()[@class='_2RkBA _3ATYZ _1sd0z']/text()")
     #   loader.add_xpath("classe_energie", "//div[contains(@data-qa-id,'criteria_item_energy_rate')]/descendant::node()[@class='_2RkBA _3ATYZ _1sd0z']/text()")
        
        
        # Nom de l'annonce, prix et date
     #   loader.add_xpath("nom_annonce", "//h1/text()")
     #   loader.add_xpath("prix", "//div[@class='_14taM']//span[@class='_1F5u3']/text()")
     #   loader.add_xpath("date_annonce", "//div[@data-qa-id='adview_date']/text()")
        
        
        # La ville
     #   loader.add_xpath("ville", ".//div[@data-qa-id='adview_location_informations']/child::node()/text()[1]")
        
        
        # La description
     #   loader.add_xpath("description", "//span[@class='content-CxPmi']")
     #   yield loader.load_item()
        
