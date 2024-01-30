import requests
from bs4 import BeautifulSoup
import unicodedata
import os
import csv

class PageScraper:
    def __init__(self, folder_csv):
        self.folder_csv = folder_csv
        
        if not os.path.exists(self.folder_csv):
            os.makedirs(folder_csv)
        
        
            

    def initialize_csv(self, title_category):
        if not os.path.exists(title_category):
            with open(title_category, "w", newline='', encoding="utf-8") as outfile:
                csv_writer = csv.writer(outfile, delimiter=';', quoting = csv.QUOTE_ALL)
                csv_writer.writerow(["catégories", "product_page_url", "UPC", "title", "price_includind_tax",
                                "price_excluding_tax", "number_available", "review_rating", "product_description",
                                "image_url"])
            

    def scrape_page(self,url, page_url):
        product_url_list = []
        page_number = 1
        while True:
            current_page = f"{url}{page_url}"
            response = requests.get(current_page)            
            if response.ok:
                soup = BeautifulSoup(response.text, "html.parser")
                title_category = soup.find("h1")
                h3s = soup.findAll("h3")
                next_button = soup.find("li", {"class": "next"})              
                for h3 in h3s:
                    a = h3.find("a")
                    product_url = "http://books.toscrape.com/catalogue/" + a["href"].replace("../../../", "")
                    product_url_list.append(product_url)
                if next_button:
                    page_number += 1
                    page_url = page_url.replace("index.html", "page-1.html")
                    page_url = page_url.replace(f"page-{page_number-1}", f"page-{page_number}")
                    #print(f"Passage à la page suivante : {url}{page_url}")
                    
                    
                else:
                    break        
        print("page OK")
        return product_url_list
    
    def visited_product(self, product_url):
        # Lit le fichier CSV pour vérifier si url est deja visité
        with open(self.visited_url, "r") as memoryFile:
            csv_reader = csv.reader(memoryFile)
            for row in csv_reader:
                if row and row[0] == product_url:
                    return True







