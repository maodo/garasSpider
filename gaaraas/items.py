# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GaaraasItem(scrapy.Item):
    # define the fields for your item here like:
    marque = scrapy.Field()
    #moteur = scrapy.Field()
    boite_de_vitesse = scrapy.Field()
    #localisation = scrapy.Field()
    kilometrage = scrapy.Field()
    annee = scrapy.Field()
    #couleur = scrapy.Field()
    #date_post = scrapy.Field()
    #nom_vendeur = scrapy.Field()
    #statut_vendeur = scrapy.Field()
    type_de_carburant = scrapy.Field() 
    #commentaires = scrapy.Field()
    #image_url = scrapy.Field()
    #url_details = scrapy.Field()
    #climatisation = scrapy.Field()
    #condition = scrapy.Field()
    #volant_position = scrapy.Field()
    prix = scrapy.Field()
    #carosserie = scrapy.Field()
    #image_url = scrapy.Field()
