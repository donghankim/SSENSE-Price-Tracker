from bs4 import BeautifulSoup
from datetime import datetime
import requests


class Items(object):
    def __init__(self):
        #dummy url
        self.url = "http://google.com" 
        self.source = None
        self.soup = None
        
        self.price_val = "N/A"
        self.name = "- Product Name -"
        self.description = "- Product Description -"
        self.date_time = "date - time"

    def set_url(self, url):
        self.url = url
        self.source = requests.get(self.url).content
        self.soup = BeautifulSoup(self.source, 'lxml')

        # get required data 
        price_container = self.soup.find("div", class_ = "span16 price-container")
        self.price_val = price_container.find("span", class_ = "price").text
        self.name = self.soup.find("h2", class_ = "product-name").text
        description_container = self.soup.find("div", class_ = "content")
        description_container2 = description_container.find("div")
        
        try:
            self.description = description_container2.find("p", class_ = "vspace1 product-description-text").text
        except:
            self.description = "Couldnt find product description..."

        # get update time
        now = datetime.now()
        dt_string = now.strftime("%m.%d - %H:%M")
        self.date_time = dt_string




