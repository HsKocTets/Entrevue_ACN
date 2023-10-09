from  dotenv import load_dotenv 
from flask import Flask

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Nomme l'application  
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'