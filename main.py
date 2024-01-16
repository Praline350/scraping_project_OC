import requests
from bs4 import BeautifulSoup
import unicodedata
import os
from product_scraper import ProductScraper
from page_scraper import PageScraper
from category_scraper import CategoryScraper
import csv
import time

#Test de perfomance#
start_time = time.time()


check_number = 1
url = "http://books.toscrape.com/"
folder_csv = "Dossier CSV par catégories"
folder_image ="Books image"
index_categories = 0
titles = []

"""Extraction des catégories"""

category = CategoryScraper()
categories, title_category = category.scrape_category(url)


"""création dossiers"""

page = PageScraper(folder_csv)


"""Exctration des titre de catégories et création des fichier CSV"""

for title in title_category:
    filename = os.path.join(folder_csv, f"{title}.csv")
    page.initialize_csv(filename)
    titles.append(title)
    

product = ProductScraper(folder_image)

"""Exctaction des info de chaque produit, par catégories et écriture dans leurs CSV réspectif"""
"""Ainsi que l'enregistrement de chaque images dans un dossier separé par catégories"""

while index_categories != len(categories):
    product_url_list = page.scrape_page(url, categories[index_categories])
    for product_url in product_url_list:
        info_product = product.scrape_product(product_url, title_category[index_categories])
        current_filename = os.path.join(folder_csv, f"{title_category[index_categories]}.csv")
        product.write_product(current_filename, info_product, titles[index_categories] )    

    print(f"Ecriture {titles[index_categories]} OK")
    index_categories += 1


print("fin d'Extraction")
end_time = time.time()
program_time = end_time - start_time
print(f"Le programme a mis {program_time} seconde")










