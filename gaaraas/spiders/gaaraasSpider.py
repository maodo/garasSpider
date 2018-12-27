import scrapy 
from gaaraas.items import GaaraasItem
from scrapy.http import Request
from hashlib import sha1

class gaaraasSpider(scrapy.Spider):
    
    name = 'gaaraasSpider'
    allowed_domains = ['gaaraas.com']
    start_urls = ['https://www.gaaraas.com/petites-annonces-Voitures']

    
    
    def parse_details(self,response):
        item = GaaraasItem()
        proprietes = response.css('div.prop >div> span::text').extract()
        item['prix'] = response.css('div.ad-price > span::text').extract_first()
        item['moteur'] = proprietes[1]
        item['boite_de_vitesse'] = proprietes[3]
        item['kilometrage'] = proprietes[5]
        item['annee'] = proprietes[7]
        item['couleur'] = proprietes[9]
        item['carosserie'] = proprietes[11]
        item['carburant'] = proprietes[13]
        item['climatisation'] = proprietes[15]
        item['volant_position'] = proprietes[17]
        item['condition'] = proprietes[19]
        item['localisation'] = response.css('div.ad-title > a > span::text').extract_first()
        item['date_post'] = response.css('div.ad-created-border > span >strong::text').extract_first()
        item['nom_vendeur'] = response.css('div.profile-data>h5::text').extract_first()
        item['commentaires'] = response.css('div.comment-wrapper::text').extract()
        item['nom_voiture'] = response.css('div.ad-title > h2::text').extract_first()
        
        images_tag = response.css('div.slider-nav')
        listOfImagesUrl = images_tag.css('img::attr(src)').extract()
        concat_url = ""
        for imageurl in listOfImagesUrl :
            result_Of_Hash = sha1(imageurl.encode())
            concat_url =concat_url+"|"+result_Of_Hash.hexdigest() 
        
        item['image_url'] = concat_url
    

        yield item


    def parse(self, response):
        

        base_url = 'https://www.gaaraas.com'
        cars_urls = response.css('a.common-ad-card::attr(href)').extract()
        for car_url in cars_urls : 
            url = base_url+car_url

            yield Request(url = url,callback=self.parse_details)
        

        next_page_url = response.css('a.next_page::attr(href)').extract_first()

        if(next_page_url) : 
        	next_page_url = response.urljoin(next_page_url)
        	yield scrapy.Request(url = next_page_url,callback = self.parse)