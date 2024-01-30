import requests
from bs4 import BeautifulSoup
import unicodedata
import os
import csv


class CategoryScraper:
    def __init__(self):
        pass

    def scrape_category(self, url):
        categories = []
        response = requests.get(url)
        if response.ok:
            soup = BeautifulSoup(response.text, "html.parser")
            uls = soup.findAll("ul")
            uls = uls[2]
            lis = uls.findAll("li")
            title_category = [li.find("a").text.strip() for li in lis]
            for li in lis:
                a_tags = li.findAll("a")
                for a_tag in a_tags:
                    category_url = a_tag["href"]
                    categories.append(category_url)
        print("category OK")
        return categories, title_category
        


