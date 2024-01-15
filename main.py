import requests
from bs4 import BeautifulSoup
import unicodedata
import os
from product_scraper import ProductScraper
from page_scraper import PageScraper


product_csv = "Catégories.csv"
product_url = "http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html"
category_url = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"

scraper = ProductScraper(product_csv)
scraper.scrape_product(product_url)