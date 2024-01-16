import requests
from bs4 import BeautifulSoup
import unicodedata
import os
from product_scraper import ProductScraper
from page_scraper import PageScraper
from category_scraper import CategoryScraper


url = "http://books.toscrape.com/"
folder_csv = "Dossier CSV par catégories"
index_categories = 0

#Extraction des catégories

category = CategoryScraper()
categories, title_category = category.scrape_category(url)
#print(len(categories))

# création dossier csv

page = PageScraper(folder_csv)
product = ProductScraper()

for title in title_category:
    filename = os.path.join(folder_csv, f"{title}.csv")
    page.initialize_csv(filename)

while index_categories != 1:
    product_url_list = page.scrape_page(url, categories[index_categories])
    #print(categories[index_categories])
    for product_url in product_url_list:
        info_product = product.scrape_product(product_url)
        #print(product_url)
        current_filename = os.path.join(folder_csv, f"{title_category[index_categories]}.csv")
        product.write_product(current_filename, info_product)
    index_categories += 1
    print(index_categories)
    






print("fin d'extraction")










