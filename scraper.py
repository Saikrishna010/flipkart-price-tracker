import requests
from bs4 import BeautifulSoup


PRICE_CLASS="_30jeq3 _16Jk6d"
PRODUCT_NAME_CLASS="B_NuCI"


# intilization of Scraper class
class Scraper:
    def start_scarp(self, PRODUCT):
        """
        takes the url of the product and returns the 
        current price of the product and name of the product
        """
        # request to get the product web page
        self.response = requests.get(PRODUCT)
        # creating soup object with BeautifulSoup
        self.soup = BeautifulSoup(self.response.content, "lxml")
        #finding the value by class & converting into text
        self.price_p=self.soup.find(class_=PRICE_CLASS).get_text()
        self.price_p=self.price_p.split("₹")[1]
        self.price_p=self.price_p.split(",")

        self.current_price=int(self.price_p[0]+self.price_p[1])
        #finding the value by class & converting into text
        self.product_name=self.soup.find(class_=PRODUCT_NAME_CLASS).get_text()

        return self.current_price, self.product_name

