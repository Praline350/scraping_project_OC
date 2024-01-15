import requests
from bs4 import BeautifulSoup
import unicodedata
import os

class ProductScraper:
    def __init__(self, product_csv):
        self.product_csv = product_csv

        # Crée le fichier CSV s'il n'existe pas
        if not os.path.exists(self.product_csv): 
            self.initialize_csv()

    def initialize_csv(self):
        # Initialise le fichier CSV avec les en-têtes
        with open(self.product_csv, "w", encoding="utf-8") as outfile:
            outfile.write("product_page_url, UPC, title, price_includind_tax, "
                          "price_excluding_tax, number_available, product_description, "
                          "category, review_rating, image_url\n")

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

            # Ajoute les données au fichier CSV
            with open(self.product_csv, "a", encoding="utf-8") as outfile:
                outfile.write(f"{product_url}, {upc}, {title.text}, {tax_incl}, "
                              f"{tax_excl}, {availability}, description, category, "
                              f"{review}, image\n")



          
          
    


                
    



    
