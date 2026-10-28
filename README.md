# 📚 Books Scraper ETL Pipeline

Un pipeline ETL (Extract, Transform, Load) robuste développé en Python pour extraire les données de 1000 livres depuis `books.toscrape.com` et les stocker de manière structurée dans une base de données MySQL.

## 🛠️ Technologies Utilisées
- **Python 3**
- **BeautifulSoup4 & Regex** : Extraction et nettoyage des données HTML.
- **SQLAlchemy (ORM)** : Modélisation et gestion de la base de données.
- **MySQL** : Stockage relationnel des catégories et des livres.
- **Requests** : Gestion des requêtes HTTP et des sessions.

## ⚙️ Architecture du Projet
- `fetch.py` : Récupération sécurisée du code HTML avec gestion des headers.
- `parse.py` : Scraping, pagination et nettoyage des données brutes (prix, stock, notes, etc.).
- `models.py` : Schéma de la base de données (Tables `categories` et `livres`).
- `store.py` : Insertion des données avec SQLAlchemy.
- `main.py` : Orchestration du pipeline complet.