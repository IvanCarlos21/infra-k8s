#!/bin/bash

# Démarrer cron en arrière-plan
service cron start

# Lancer l'application FastAPI
uvicorn application.backend.main:app --host 0.0.0.0 --port 8000 --reload
