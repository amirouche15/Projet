from flask import *

# Création d'un objet application web Flask
app = Flask(__name__)

# Création d'une fonction accueillir() associée à l'URL "/"
# pour générer une page web dynamique
@app.route("/")
def accueillir():
    """Affiche un message dans le navigateur web"""
    return "<h1>Bienvenue</h1>"

# Nouvelle page "A propos" associée à l’URL "/a-propos"
@app.route("/a-propos")
def renseigner():
    """Affiche la page a-propos"""
    return "Application web BONJOUR v0.2"
# Lancement de l'application web et son serveur
# accessible à l'URL : http://127.0.0.1:1664
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1664, debug=True)