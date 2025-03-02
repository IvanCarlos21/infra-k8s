
import os
from sqlalchemy import create_engine, Column, Integer, String, Enum
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()                                                                                   # Charger les variables d'environnement (fichier .env)

# Charger les informations de connexion à la BDD
DATABASE_URL = f"mysql+mysqlconnector://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}:3306/{os.getenv('MYSQL_DATABASE')}"
engine = create_engine(DATABASE_URL, echo=True)                                                 # Créer l'engine SQLAlchemy pour la connexion à MySQL

# Créer une base de données déclarative pour les modèles
Base = declarative_base()

class User(Base):
    __tablename__ = "users"  # Nom de la table dans la base de données
    
    id = Column(Integer, primary_key=True, index=True)  # id sera la clé primaire
    name = Column(String(255), index=True)  # nom de l'utilisateur
    email = Column(String(255), unique=True, index=True)  # email de l'utilisateur, unique pour chaque utilisateur
    loyalty_points = Column(Integer, index=True)
    status = Column(String(255), index=True)


# Créer la session SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Créer toutes les tables dans la base de données
Base.metadata.create_all(bind=engine)
