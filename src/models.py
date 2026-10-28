from sqlalchemy import Column, Integer, String, Float, ForeignKey,Numeric, Text ,create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class categorie(Base):
    __tablename__ = "categories"

    categorie_id = Column(Integer , primary_key=True, autoincrement=True)
    nom = Column(String(255) , unique=True)
    url = Column(String(255))


class livre(Base):
    __tablename__ = "livres"

    id_livre = Column(Integer,primary_key=True)
    url = Column(String(255))
    url_image = Column(String(255))
    upc = Column(String(50) , unique=True)
    titre = Column(String(500))
    prix_ht = Column(Numeric(10, 2))
    prix_ttc = Column(Numeric(10, 2))
    stock = Column(Integer)
    nb_avis = Column(Integer)
    note = Column(Integer)
    description = Column(Text)
    categorie_id = Column(Integer , ForeignKey('categories.categorie_id'))

DATABASE_URL = "mysql+mysqlconnector://root:1234@127.0.0.1:3306/books_pipeline"
engine = create_engine(DATABASE_URL)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("les table cree!")