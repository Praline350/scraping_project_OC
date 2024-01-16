import requests
from bs4 import BeautifulSoup
import unicodedata
import os

class ProductScraper:
    def __init__(self):
        pass

    def scrape_product(self, product_url):
        response_product = requests.get(product_url)
        if response_product.ok:
            soup_product = BeautifulSoup(response_product.text, "html.parser")
            title = soup_product.find("h1")
            product_td = soup_product.findAll("td")
            tds = [td.text for td in product_td]

            upc = tds[0]
            tax_incl = tds[3]
            tax_excl = tds[2]
            availability = tds[5]
            review = tds[6]
            info_product = []
            info_product.extend([product_url, upc, title.text, tax_incl, tax_excl, availability, review])
            print(info_product)
            return info_product
        

    
    def write_product(self, filename, info_product):       
        with open(f"{filename}", "a", encoding="utf-8") as outfile:
            outfile.write(f"{info_product[0]}, {info_product[1]}, {info_product[2]}, {info_product[3]},"
                           f"{info_product[4]}, {info_product[5]}, {info_product[6]}\n")



          
          
    


                
    



    
