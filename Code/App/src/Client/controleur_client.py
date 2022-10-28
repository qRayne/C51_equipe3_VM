import urllib.request
import urllib.parse 
import json

from sys import path
path.append('../Utils')
import utils


path.append('./Module')
from vue_accueil import Vue_accueil


class Controleur_Client:
    def set_vue(self, vue):
        self.vue = vue

    # On prépare et on envoie les infos, incluant
    # le nom de la fonction, au serveur_web, qui, lui
    # les reliera au controleur_serveur qui, lui
    # communiquera avec la BD
    # La réponse est json-ifiée
    def appel_serveur(self, args):
        # on encode les données en format url
        # et ensuite en bytes
        data = urllib.parse.urlencode(args).encode('ascii')

        # on effectue la demande au serveur
        #reponse = urllib.request.urlopen(Controleur.URL, data)
        reponse = urllib.request.urlopen(utils.URL, data)

        # on retourne l'objet retourné par le serveur
        # qui avait été json-ifié
        return json.loads(reponse.read())

    # Le nom de la fonction voulue est envoyée
    # par le controleur_client et reçu par le
    # controleur_serveur dans le request.form
    def identifier_usager(self, identifiant, mdp):
        infos = {
            utils.FONCTION:utils.IDENTIFIER_USAGER,
            utils.IDENTIFIANT:identifiant,
            utils.MDP:mdp
        }
        return self.appel_serveur(infos)
    
    def creer_personne(self, nom, prenom, courriel, telephonePersonne, adresse=""):
        infos = {
            utils.FONCTION:utils.CREER_PERSONNE,
            utils.NOM:nom,
            utils.PRENOM:prenom,
            utils.COURRIEL:courriel,
            utils.TELEPHONE:telephonePersonne,
            utils.ADRESSE:adresse
        }
        return self.appel_serveur(infos)
    
    def creer_locateur(self,nomCompagnie,telephoneCompagnie,adresse=""):
        infos = {
            utils.FONCTION:utils.CREER_LOCATEUR,
            utils.NOM_COMPAGNIE:nomCompagnie,
            utils.TELEPHONE_COMPAGNIE:telephoneCompagnie,
            utils.ADRESSE:adresse
        }
        return self.appel_serveur(infos)

    
    def enregistrer_usager(self,personneEmail,locateurNomCompagnie,identifiant,mdp,permission):
        infos = {
            utils.FONCTION:utils.ENREGISTER_USAGER,
            utils.PERSONNE_EMAIL:personneEmail,
            utils.LOCATEUR_NOM_COMPAGNIE:locateurNomCompagnie,
            utils.IDENTIFIANT:identifiant,
            utils.MDP:mdp,
            utils.PERMISSION:permission
        }
        return self.appel_serveur(infos)
    
    def creer_adresse(self, rue, numero, appartement, ville, province_etat, pays, code_postal):
        infos = {
            utils.FONCTION:utils.CREER_ADRESSE,
            utils.RUE:rue,
            utils.NUMERO:numero,
            utils.APPARTEMENT:appartement,
            utils.VILLE:ville,
            utils.PROVINCE_ETAT:province_etat,
            utils.PAYS:pays,
            utils.CODE_POSTAL:code_postal
        }
        return self.appel_serveur(infos)
        
    
# test
def main():
    c = Controleur_Client()
    d = c.identifier_usager('toto', 'totototo')
    e = c.set_vue(Vue_accueil);
    
    print(d)
    return 0

if __name__ == '__main__':
    quit(main())