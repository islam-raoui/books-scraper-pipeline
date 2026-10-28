from sqlalchemy.orm import sessionmaker
from models import engine ,categorie , livre

Session = sessionmaker(bind=engine)
session = Session()

def save_categorie(categorie_liste):
    for data in categorie_liste:
        existe = session.query(categorie).filter_by(nom = data["nom"]).first()

        if not existe:
            nouvelle_cat =  categorie(nom = data["nom"] , url = data["url"])
            session.add(nouvelle_cat)

    session.commit()

    print("success!")


def save_livres(listes_livres, categorie_id):
    for data in listes_livres:
        existe = session.query(livre).filter_by(upc = data["upc"]).first()

        if not existe:
            # 1. 7yedna "" w : w redinaha = 
            nouvelle_livres = livre(
                url = data["url"],
                url_image = data["url_image"],
                upc = data["upc"],
                titre = data["titre"] ,
                prix_ht = data["prix_ht"] ,
                prix_ttc = data["prix_ttc"],
                stock = data["stock"] ,
                nb_avis = data["nb_avis"],
                note = data["note"],
                description = data["description"],
                categorie_id = categorie_id
            )
            
            # 2. Kan-zidou l-ktab l s-session
            session.add(nouvelle_livres)
            
    # 3. Mli kat-sali l-boucle kamla, kan-validiw t-tkhzan f MySQL
    session.commit()
    print("succees! les livres stocker dans la base de donnees ")


def get_categorie_id(nom_categorie):
    cat = session.query(categorie).filter_by(nom=nom_categorie).first()
    if cat:
        return cat.categorie_id
    return None