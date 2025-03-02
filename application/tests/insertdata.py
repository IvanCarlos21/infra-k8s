import random
import string
from sqlalchemy.orm import Session
from application.database.database import User, SessionLocal
from application.backend.crud import calculate_status

# Fonction pour générer un nom aléatoire
def generate_random_name():
    return ''.join(random.choices(string.ascii_lowercase, k=7)).capitalize()

# Fonction pour générer un email aléatoire
def generate_random_email(name):
    return f"{name.lower()}@example.com"

# Fonction pour générer des points de fidélité aléatoires
def generate_random_loyalty_points():
    return random.randint(0, 1000)

# Insérer 10 utilisateurs aléatoires dans la base
def insert_random_users(db: Session):
    for _ in range(5000):
        name = generate_random_name()
        email = generate_random_email(name)
        loyalty_points = generate_random_loyalty_points()
        status = calculate_status(loyalty_points)

        # Créer un nouvel utilisateur avec les données générées
        new_user = User(name=name, email=email, loyalty_points=loyalty_points, status=status)

        # Ajouter l'utilisateur à la base de données
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        print(f"Utilisateur créé: {new_user.name}, Email: {new_user.email}, Points: {new_user.loyalty_points}, Statut: {new_user.status}")

# Créer une session DB et insérer des utilisateurs
db = SessionLocal()
try:
    insert_random_users(db)
finally:
    db.close()
