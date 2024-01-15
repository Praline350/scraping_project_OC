import requests
from bs4 import BeautifulSoup
import unicodedata
import os

class PageScraper:
    def __init__(self,) -> None:
        pass

    def scrape_page(self,category_url):
        links = []
        page_number = 1
        while True:
            response = requests.get(category_url)
            print(category_url)
            if response.ok:
                soup = BeautifulSoup(response.text, "html.parser")
                h3s = soup.findAll("h3")
                next_button = soup.find("li", {"class": "next"})
                
                for h3 in h3s:
                    a = h3.find("a")
                    product_url = "http://books.toscrape.com/catalogue/" + a["href"].replace("../../../", "")
                    links.append(product_url)
                if next_button:
                    page_number += 1
                    category_url = category_url.replace(f"page-{page_number-1}", f"page-{page_number}")
                    print(category_url)
                    
                else:
                    break
        print(len(links))





category_url = "http://books.toscrape.com/catalogue/category/books/mystery_3/page-1.html"
scraper = PageScraper()
scraper.scrape_page(category_url)




