from fastapi import FastAPI, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
from starlette.requests import Request
from sqlalchemy.orm import Session
from . import crud
from application.database.database import SessionLocal
from application.database.database import User

app = FastAPI()

# Initialiser les templates avec le dossier "templates"
templates = Jinja2Templates(directory="application/frontend/templates")

# Servir les fichiers statiques (CSS, JS, images)
app.mount("/static", StaticFiles(directory="application/frontend/static"), name="static")

# Dépendance pour obtenir la session de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
# def read_root():
#     return {"message": "Bienvenue sur l'API CRUD avec FastAPI!"}
async def read_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


#  Récupérer tous les utilisateurs
@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

#  Récupérer un utilisateur par ID
@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return user

#  Ajouter un utilisateur
@app.post("/users")
def create_user(name: str, email: str, loyalty_points: int = 0,  db: Session = Depends(get_db)):
    return crud.create_user(db, name, email, loyalty_points)

#  Mettre à jour un utilisateur
@app.put("/users/{user_id}")
def update_user(user_id: int, name: str, email: str, loyalty_points: int, db: Session = Depends(get_db)):
    user = crud.update_user(db, user_id, name, email, loyalty_points)
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return user

#  Supprimer un utilisateur
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return {"message": "Utilisateur supprimé avec succès"}