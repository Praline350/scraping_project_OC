import requests
from bs4 import BeautifulSoup
import unicodedata
import os

class PageScraper:
    def __init__(self, folder_csv) -> None:
        self.visited_page = set()
        self.folder_csv = folder_csv

        if not os.path.exists(self.folder_csv):
            os.makedirs(folder_csv)
            

    def initialize_csv(self, title_category):
        with open(title_category, "w", encoding="utf-8") as outfile:
            outfile.write("product_page_url, UPC, title, price_includind_tax, "
                          "price_excluding_tax, number_available, product_description, "
                          "category, review_rating, image_url\n")
            

    def scrape_page(self,url, page_url):
        links = []
        page_number = 1
        while True:
            current_page = f"{url}{page_url}"
            #print(current_page)
            response = requests.get(current_page)            
            #print(f"acces a {current_page}")
            if current_page in self.visited_page:
                break
            if response.ok:
                soup = BeautifulSoup(response.text, "html.parser")
                title_category = soup.find("h1")
                h3s = soup.findAll("h3")
                next_button = soup.find("li", {"class": "next"})
                self.visited_page.add(current_page)
                for h3 in h3s:
                    a = h3.find("a")
                    product_url = "http://books.toscrape.com/catalogue/" + a["href"].replace("../../../", "")
                    links.append(product_url)
                if next_button:
                    page_number += 1
                    page_url = page_url.replace("index.html", "page-1.html")
                    page_url = page_url.replace(f"page-{page_number-1}", f"page-{page_number}")
                    #print(f"Passage à la page suivante : {url}{page_url}")
                    
                    
                else:
                    #print('pas de next')
                    break        
        print("page ok")
        return links

"""url = "http://books.toscrape.com/"
page_url = "catalogue/category/books/mystery_3/page-1.html"
scraper = PageScraper()
scraper.scrape_page(url, page_url)"""






