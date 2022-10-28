import json
from dao import Dao

from sys import path
path.append('../Utils')
import utils


# class Controleur_Serveur(Controleur):
class Controleur_Serveur:
    def __init__(self):
        self.fonctions = {
            utils.IDENTIFIER_USAGER:self.identifier_usager
        }

    # Le nom de la fonction voulue est envoyée
    # par le controleur_client et reçu par le
    # controleur_serveur dans le request.form
    # la réponse de la BD est JSON-ifiée
    def reponse(self, request_form):
        fonction_str = request_form[utils.FONCTION]
        fonction = self.fonctions[fonction_str]
        infos = fonction(request_form)
        return json.dumps(infos)

    # instance de sqlite3 doit être utilisée dans le même
    # thread que celui de sa création
    def identifier_usager(self, form):
        identifiant = form[utils.IDENTIFIANT]
        mdp = form[utils.MDP]
        return Dao().identifier_usager(identifiant, mdp)
    
    def creer_personne(self,form):
        nom = form[utils.NOM],
        prenom = form[utils.PRENOM],
        courriel = form[utils.COURRIEL],
        telephone = form[utils.TELEPHONE_PERSONNE],
        adresse = form[utils.ADRESSE]
        return Dao.creer_personne(nom,prenom,courriel,telephone,adresse) 
    
    def creer_locateur(self,form):
        nomCompagnie = form[utils.NOM_COMPAGNIE],
        telephoneCompagnie = form[utils.TELEPHONE_COMPAGNIE],
        adresse = form[utils.ADRESSE]
        return Dao.creer_locateur(nomCompagnie,telephoneCompagnie,adresse)  
    
    def enregister_usager(self,form):
        personneEmail = form[utils.PERSONNE_EMAIL],
        locateurNomCompagnie = form[utils.LOCATEUR_NOM_COMPAGNIE],
        identifiant = form[utils.IDENTIFIANT]
        mdp = form[utils.MDP],
        permission = form[utils.PERMISSION]
        return Dao.enregistrer_usager(personneEmail,locateurNomCompagnie,identifiant,mdp,permission) 

    
    def creer_adresse(self,form):
        rue = form[utils.RUE],
        numero = form[utils.NUMERO],
        appartement = form[utils.APPARTEMENT],
        ville = form[utils.VILLE],
        province = form[utils.PROVINCE_ETAT],
        pays = form[utils.PAYS],
        codePostal = form[utils.CODE_POSTAL]
        return Dao.creer_adresse(rue,numero,appartement,ville,province,pays,codePostal)
    