import requests
from bs4 import BeautifulSoup
import unicodedata
import os
import csv
from PIL import Image
from io import BytesIO
import re

# créer le dossier images s'il n'existe pas a la création d'une instance

class ProductScraper:
    def __init__(self, folder_image):
        self.folder_image = folder_image
        if not os.path.exists(folder_image):
            os.makedirs(folder_image)
        
# Supprimes les caractères non valides pour un nom de fichier

    def clean_filename(self, filename):
        return re.sub(r'[\\/:"*?<>|]+', '', filename)
    
# normalise les caractère de l'argument    
    def normalize(self, info):
        return unicodedata.normalize('NFKD', info).encode('ascii', 'ignore').decode('utf-8')
    
# télécharges les images 

    def download_image(self, image_url, title, category):
        image_response = requests.get(image_url)
        if image_response.ok:
            folder_category_image = os.path.join(self.folder_image, category)
            if not os.path.exists(folder_category_image):
                #creer un dossier images par categories
                os.makedirs(folder_category_image)
            image = Image.open(BytesIO(image_response.content))
            cleaned_title = self.clean_filename(title)
            image_png = os.path.join(folder_category_image, cleaned_title + ".jpg")
            image.save(image_png, "JPEG")
            image.close
            return image_png

        
        else:
            print("echec dl image")
            return None
        
#Scraping de toutes les infos produit

    def scrape_product(self, product_url, category):
        response_product = requests.get(product_url)
        if response_product.ok:
            soup_product = BeautifulSoup(response_product.text, "html.parser")
            title = self.normalize(soup_product.find("h1").text)
            image = soup_product.find("img", class_="thumbnail")
            all_p = soup_product.findAll("p")
            product_description = self.normalize(all_p[3].text)
            product_td = soup_product.findAll("td")
            review = soup_product.find("p", class_="star-rating")
            review = review["class"][1]
            if image:
                image_url = image['src'].replace("../../", "http://books.toscrape.com/")
                self.download_image(image_url, title, category)
            else:
                image_url = "Pas d'image"
            tds = [td.text for td in product_td]


            upc = self.normalize(tds[0])
            tax_incl = tds[3]
            tax_excl = tds[2]
            availability = self.normalize(tds[5])
            info_product = []
            info_product.extend([product_url, upc, title, tax_incl, tax_excl, 
                                 availability, review, product_description, image_url])
            info_product = [info_product[0],  # l'URL
                            info_product[1],  # l'UPC
                            info_product[2],  # Titre
                            info_product[3].replace("Â", ""), #tax incl
                            info_product[4].replace("Â", ""), #tax excl
                            info_product[5],  # Disponibilité
                            info_product[6],  # Note de revue
                            info_product[7],  #description
                            info_product[8]]  # chemin des fichier images dl           
            return info_product
        

    
    def write_product(self, filename, info_product, title_category):       
        with open(f"{filename}", "a",newline='', encoding="utf-8") as outfile:
            csv_writer = csv.writer(outfile, delimiter=';')
            csv_writer.writerow([title_category, info_product[0], info_product[1], info_product[2], info_product[3],
                             info_product[4], info_product[5], info_product[6], info_product[7],
                             info_product[8]] )
            
    
            
    




          
          
    


                
    



    
