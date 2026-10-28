import time
from fetch import get_html
from parse import categorie , get_book_link , parse_book_details
from store import save_categorie, save_livres, get_categorie_id


def main():
    url_base = "http://books.toscrape.com/index.html"
    print("debut")
    html = get_html(url_base)

    if html:
        print("Extraction des catégories")
        liste_categories = categorie(html , url_base)

        print(f"{len(liste_categories)} categories")
        save_categorie(liste_categories)
    else:
        print("erreur!")

    save_categorie(liste_categories)

    print("\n--- extraction des livres de chaque categorie ---")
        
       
    for cat in liste_categories: 
        cat_id = get_categorie_id(cat["nom"])
            
        if cat_id:
            print(f"\nCatégorie: {cat['nom']}")
                
            livres_data = get_all_books_data(cat["url"])
                
                
            save_livres(livres_data, cat_id)

def get_all_categorie_book(category_url):
    liste_all_book = []
    current_url = category_url

    while current_url:
        print(f"debut par {current_url}")
        html = get_html(current_url)

        if not html:
            break

        liens , next_liens = get_book_link(html , current_url)

        liste_all_book.extend(liens)

        current_url = next_liens

        time.sleep(1)

    return liste_all_book


def get_all_books_data(categorie_url):
    lien_livres = get_all_categorie_book(categorie_url)
    donnees_livres = []

    print(f"{len(lien_livres)} livres")
    for lien in lien_livres :
        html = get_html(lien)

        if html:
            infos = parse_book_details(html , lien)
            donnees_livres.append(infos)

        time.sleep(1)

    return donnees_livres



if __name__ == "__main__":
    main()

    




