# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import re
from scrapy.loader.processors import MapCompose, TakeFirst, Join

#Remove the surface's unit
def remove_surface_unit(value):
    return value.replace(u"\u00b2",'m²')

#Extract the date
def remove_date(value):
    return value[0:9]

#Remove the unit from the price 
def remove_prix(value):
    return value.replace(u"\u00e0",'')

#Remove the tags from the description
def remove_tags(value):
    return re.sub(r"\d+\\>",'',value.replace('</span>','').replace('<br>','').replace(("<span class=\"content-CxPmi\" data-reactid=\""),''))

    



class offerItem(scrapy.Item):
    type_bien= scrapy.Field()
    piece= scrapy.Field()
    surface= scrapy.Field(
        input_processor= MapCompose(remove_surface_unit)
    )
    ges= scrapy.Field()
    classe_energie= scrapy.Field()

    nom_annonce= scrapy.Field()
    date_annonce= scrapy.Field(
        input_processor= MapCompose(remove_date),
        output_processor= TakeFirst()
    )
    prix= scrapy.Field(
        input_processor= MapCompose(remove_prix),
        output_processor= TakeFirst()
    )

    ville= scrapy.Field()
    description= scrapy.Field(
        #MongoDB
        input_processor= MapCompose(remove_tags)
        #input_processor= MapCompose(count_elements)
    )

