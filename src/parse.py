from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re 

def categorie(html , base_url):
    soup = BeautifulSoup(html , "lxml")
    categories = []

    element = soup.select(".side_categories ul ul a")

    if not element:
        return categories

    for tag in element:
        name = tag.get_text(strip=True)
        href = tag.get("href")

        if name and href :
            lien = urljoin(base_url , href)
            categories.append({"nom":name , "url" :lien })


    return categories


def get_book_link(html , base_url):
    soup = BeautifulSoup(html , "lxml")
    link_book = []

    for tag in soup.select(".product_pod h3 a "):
        lien = urljoin(base_url , tag.get("href"))
        link_book.append(lien)

    next_btn = soup.select_one("li.next a")
    next_url = urljoin(base_url , next_btn.get("href")) if next_btn else None

    return link_book , next_url


def parse_book_details(html , book_url):
    soup = BeautifulSoup(html , "lxml")

    titre_tag = soup.select_one("h1")
    titre =  titre_tag.get_text(strip=True) if titre_tag else "N/A"

    description_tag = soup.select_one("#product_description ~ p")
    description = description_tag.get_text(strip=True) if description_tag else ""

    image_tag = soup.select_one("#product_gallery img")
    url_image = urljoin(book_url , image_tag.get("src")) if image_tag else ""

    info={}
    for tr in soup.select("table.table-striped tr"):
        th = tr.select_one("th")
        td = tr.select_one("td")
        if th and td :
            info[th.get_text(strip=True)] = td.get_text(strip=True)

    stock_text = info.get("Availability","")
    stock_number = re.findall(r'\d+' , stock_text)
    stock_int = int(stock_number[0]) if stock_number else 0

    prix_ht_text = info.get("Price (excl. tax)", "0")

    prix_ht_numbers = re.findall(r'[\d.]+', prix_ht_text)
    prix_ht_float = float(prix_ht_numbers[0]) if prix_ht_numbers else 0.0

    prix_ttc_text = info.get("Price (incl. tax)", "0")
    prix_ttc_numbers = re.findall(r'[\d.]+', prix_ttc_text)
    prix_ttc_float = float(prix_ttc_numbers[0]) if prix_ttc_numbers else 0.0

    nb_avis_text = info.get("Number of reviews", "0")
    nb_avis = int(nb_avis_text)

    rating_tag = soup.select_one("p.star-rating")
    note = 0

    if rating_tag :
        classes = rating_tag.get('class' , [])
        dict_notes = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

        for c in classes:
            if c in dict_notes:
                note = dict_notes[c]
                break

    return{
        "url" : book_url ,
        "url_image" :url_image ,
        "upc" : info.get("UPC", ""),
        "titre" : titre,
        "prix_ht" : prix_ht_float,
        "prix_ttc" : prix_ttc_float,
        "stock" : stock_int,
        "nb_avis" : nb_avis,
        "note" : note,
        "description":description
    }




        