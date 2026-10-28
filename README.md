#  Books Scraper ETL Pipeline

Un pipeline ETL (Extract, Transform, Load) robuste développé en Python pour extraire les données de 1000 livres depuis `books.toscrape.com` et les stocker de manière structurée dans une base de données MySQL.

##  Technologies Utilisées
- **Python 3**
- **BeautifulSoup4 & Regex** : Extraction et nettoyage des données HTML.
- **SQLAlchemy (ORM)** : Modélisation et gestion de la base de données.
- **MySQL** : Stockage relationnel des catégories et des livres.
- **Requests** : Gestion des requêtes HTTP et des sessions.

##  Architecture du Projet
- `fetch.py` : Récupération sécurisée du code HTML avec gestion des headers.
- `parse.py` : Scraping, pagination et nettoyage des données brutes (prix, stock, notes, etc.).
- `models.py` : Schéma de la base de données (Tables `categories` et `livres`).
- `store.py` : Insertion des données avec SQLAlchemy.
- `main.py` : Orchestration du pipeline complet.

##  Comment exécuter ce projet localement ?

**1. Cloner le projet**
```bash
git clone [https://github.com/islam-raoui/books-scraper-pipeline.git](https://github.com/islam-raoui/books-scraper-pipeline.git)
cd books-scraper-pipeline

**2. Créer un environnement virtuel et installer les dépendances**
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

**3. Configurer la base de données MySQL**

Créez une base de données nommée books_pipeline dans votre interface MySQL (ex: MySQL Workbench ou phpMyAdmin).

Modifiez la variable DATABASE_URL dans le fichier models.py avec vos propres identifiants (nom d'utilisateur et mot de passe)