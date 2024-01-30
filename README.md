Ce programme extrait des données sur des livres venant du site http://books.toscrape.com

Il va écrire un fichier CSV par catégorie.

Les informations extraite et ecrite sont:
 la catégorie, l'url produit, l'UPC, le titre, le prix avec et sans les taxes, le nombre en stock, la review ainsi que l'url de l'image.

Le programme téléchargera et enregistrera toutes les images dans un dossier "Books image", rangé en dossier par catégories.

Le nom des fichier image sera le titre du livre en question.

Quelques print() sont présents pour s'assurer du bon déroulement du programme ainsi que le module time pour calculer le temps d'execution.

Avant de lancer main.py assurez vous d'avoir préalablement configurer votre environnement grâce au fichier "requirements.txt"

Pour installé les modules necessaires utilisé la commande pip freeze > requirements.txt

Assurez vous aussi d'avoir bien les modules product_scraper.py, page_scraper.py, category_scraper.py dans le même répertoire que main.py

Lancez main.py. Un messages vous confirmera la fin du programme.
