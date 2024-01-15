import requests
from bs4 import BeautifulSoup
import unicodedata
import os


"""Requête pour les liens catégories"""

url = "http://books.toscrape.com/"
response = requests.get(url)
if response.ok:
    soup = BeautifulSoup(response.text, "html.parser")
    categories = []
    lis = soup.findAll("li")
    for li in lis:
        a = li.find("a")

        """ Verifie les balises li sans balise a"""

        if a and "href" in a.attrs:
            category = a["href"]
            categories.append(category)
            if len(categories) >= 52:
                break


"""Requête pour les liens des pages livre"""

index_categories = 2
page_number = 1

"""Création dossier pour les fichiers CSV"""

csv_folder = "Dossier CSV catégories"
if not os.path.exists(csv_folder):
    os.makedirs(csv_folder)


for category in categories:
    category_url = "http://books.toscrape.com/" + categories[index_categories]

    while True:
        response_category = requests.get(category_url)
        print(category_url)
        if response_category.ok:
            links = []
            soup_category = BeautifulSoup(response_category.text, "html.parser")

            h3s = soup_category.findAll("h3")
            title_category = soup_category.find("h1")
            next_button = soup_category.find("li", {"class": "next"})

            for h3 in h3s:
                a = h3.find("a")
                link = a["href"]
                links.append("http://books.toscrape.com/catalogue/" + link.replace("../../../", ""))

            path_csv_folder = os.path.join(csv_folder, f"{title_category.text}.csv")

            with open(path_csv_folder, "a", encoding="utf-8") as outFile:
                outFile.write("Titre, Prix\n")

                for link in links:
                    response_page = requests.get(link)
                    if response_page.ok:
                        soup_page = BeautifulSoup(response_page.text, "html.parser")

                        title_soup = soup_page.find("h1")
                        price_soup = soup_page.find("p", {"class": "price_color"})

                        title = unicodedata.normalize('NFKD', title_soup.text).encode('ascii', 'ignore').decode('utf-8')
                        price = unicodedata.normalize('NFKD', price_soup.text).encode('ascii', 'ignore').decode('utf-8')

                        #print(f"{title},{price}")

                        outFile.write(str(title.replace(",", ".")) + "," + price + "\n")
                    else:
                        print("erreur page livre")
                        break

                if next_button:
                    page_number += 1
                    category_url = category_url.replace("index.html", f"page-{page_number}.html")
                    category_url = category_url.replace(f"page-{page_number-1}", f"page-{page_number}")
                #print(page_number)
                #print(category_url)

                else:
                    page_number = 1
                    break

        else:
            print("erreur pagination")
            break
    index_categories += 1

    if index_categories == len(categories):
        print("Exctraction terminer")
        break

