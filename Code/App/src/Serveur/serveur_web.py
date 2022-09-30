from flask import Flask,request
from werkzeug.wrappers import Response
from controleur_serveur import Controleur_Serveur

class Serveur_Web:
    __app = Flask(__name__)
    __app.secret_key = "toto1washere2"
    __controleur = None

    @staticmethod
    def lancer(hote, port):
        Serveur_Web.__app.run(debug=True, host=hote, port=port)

    @staticmethod
    def set_controleur(controleur):
        Serveur_Web.__controleur = controleur

    @__app.route('/', methods=["GET","POST"])
    def index():
        if request.method == "POST":
            # on transmet le formulaire qui a été envoyé
            # par le controleur_client au controleur_serveur
            data = Serveur_Web.__controleur.reponse(request.form) 
            return Response(data, mimetype='application/json')
        else:
            return "403 FORBIDDEN"
