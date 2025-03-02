# 1. Utilisation de l'image Python officielle
FROM python:3.10

# 2. Définition du répertoire de travail
WORKDIR /

# 3. Copie des fichiers nécessaires
COPY application/ /application

# 4. Installation des dépendances
RUN pip install --no-cache-dir -r /application/requirements.txt

# 5. Installation de cron
RUN apt-get update && apt-get install -y cron

# 6. Ajouter un job cron pour exécuter le script toutes les 20 minutes
RUN echo "*/25 * * * *  cd / && /usr/local/bin/python3 -m application.tests.insertdata >> /var/log/cron.log 2>&1" > /etc/cron.d/insertdata-cron

# 7. Appliquer les bonnes permissions et activer le cron job
RUN chmod 0644 /etc/cron.d/insertdata-cron && crontab /etc/cron.d/insertdata-cron

# 8. Démarrer le service cron en foreground
RUN touch /var/log/cron.log

# 9. Copie du script d'entrée
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# 10. Exposer le port utilisé par FastAPI
EXPOSE 8000

# 11. Lancer l'application avec cron
CMD ["/entrypoint.sh"]
