from  dotenv import load_dotenv 
from flask import Flask, request, jsonify
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

        n = int(request.args.get('N'))
        if n < 1 or n > 100:
            # Code d'erreur 400 pour "Bad Request"
            return 'Error: N must be between 1 and 100', 400
        
        cursor = connection.cursor()

        # Exécute la requête SQL pour créer la vue sur ma database
        cursor.execute(f"""
            SELECT c.id, c.url, c.title, c.lang, c.last_crawled, c.last_updated, c.last_updated_date, c.md5hash, s.score
            FROM {public_schema}.crawl c
            JOIN {public_schema}.score s ON c.id = s.entity_id
            ORDER BY s.score DESC
            LIMIT {n};
        """)

        top_scores = cursor.fetchall()

        # Convertir le résultat en un format JSON
        json = {"top_documents_with_scores": top_scores}

        return jsonify(json)

    except Exception as e:
        return f"CONNECTION FAILED OR BAD TOP: {e}", 400