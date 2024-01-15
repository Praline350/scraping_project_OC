import requests
from bs4 import BeautifulSoup
import unicodedata
import os
from product_scraper import ProductScraper
from page_scraper import PageScraper
from category_scraper import CategoryScraper


url = "http://books.toscrape.com/"
product_csv = "Catégories.csv"
folder_csv = "Dossier CSV par catégories"

#Extraction des catégories

category = CategoryScraper()
categories, title_category = category.scrape_category(url)
page = PageScraper(folder_csv)
for title in title_category:
    filename = os.path.join(folder_csv, f"{title}.csv")
    page.initialize_csv(filename)


for category_url in categories:
    #print(url + category_url)
    product_url = page.scrape_page(url, category_url)

print("fin")










