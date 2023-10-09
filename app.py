from  dotenv import load_dotenv 
from flask import Flask, request
import os
import psycopg2

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Nomme l'application  
app = Flask(__name__)

# Sauvegarde les données secrets localement
host = os.getenv("HOST")
port = os.getenv("PORT")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
db_name = os.getenv("NAME")
public_schema = os.getenv("PUBLIC_SCHEMA")
user_schema = os.getenv("USER_SCHEMA")

# Méthode HTTP
@app.route("/top", methods=['GET'])
def get_top_n():
    try:
    # Connexion à la base de données
        connection = psycopg2.connect(
            host=host,
            port=port,
            dbname=db_name,
            user=username,
            password=password
        )
        return "CONNECTION SUCCEEDED"
    except Exception as e:
        return f"CONNECTION FAILED: {e}", 400