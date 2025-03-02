import logging
from sqlalchemy.orm import Session
from application.database.database import User 

# Configurer le logger
logging.basicConfig(level=logging.INFO)  # Afficher les logs à partir du niveau INFO
logger = logging.getLogger(__name__)

# Fonction pour calculer le statut en fonction des points de fidélité
def calculate_status(loyalty_points: int):
    if loyalty_points >= 500:
        return "platinum"
    elif loyalty_points >= 300 and loyalty_points < 500:
        return "gold"
    elif loyalty_points >= 100 and loyalty_points < 300:
        return "silver"
    else:
        return "bronze"

# Récupérer tous les utilisateurs
def get_users(db: Session):
    logger.info("Récupération de tous les utilisateurs.")
    return db.query(User).all()

# Récupérer tous les utilisateurs
def get_users(db: Session):
    return db.query(User).all()

# Récupérer un utilisateur par ID
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Ajouter un utilisateur
def create_user(db: Session, name: str, email: str, loyalty_points: int):
    statuses = calculate_status(loyalty_points)
    logger.info(f"Ajout d'un nouvel utilisateur : {name}, avec le statut {statuses}.")
    new_user = User(name=name, email=email, loyalty_points=loyalty_points, status=statuses)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Mettre à jour un utilisateur
def update_user(db: Session, user_id: int, name: str, email: str, loyalty_points: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None

    status = calculate_status(loyalty_points)
    user.name = name
    user.email = email
    user.loyalty_points = loyalty_points
    user.status = status

    db.commit()
    db.refresh(user)
    return user

# Supprimer un utilisateur
def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None

    db.delete(user)
    db.commit()
    return user
