# Utilise l'image officielle Python 3.10 comme base
FROM python:3.10  

# Expose le port 5000 pour permettre l'accès à l'application Flask
EXPOSE 5000  

# Définit le répertoire de travail à "/app" dans le conteneur
WORKDIR /app  

# Installe Flask via pip (nécessaire pour exécuter l'application)
RUN pip install flask  

# Copie tous les fichiers du répertoire actuel (sur la machine hôte) vers le répertoire de travail dans le conteneur
COPY . .  

# Définit la commande par défaut pour exécuter l'application Flask
CMD [ "flask", "run", "--host", "0.0.0.0" ]  
# - "flask run" démarre le serveur Flask  
# - "--host 0.0.0.0" permet d'accepter les connexions depuis n'importe quelle adresse IP (nécessaire pour exécuter l'application dans un conteneur)
