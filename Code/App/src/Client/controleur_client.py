from ctypes import util
import urllib.request
import urllib.parse 
import json

from sys import path
path.append('../Utils')
import utils


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
    
    def creer_personne(self, nom, prenom, courriel, telephone_personne, adresse):
        infos = {
            utils.FONCTION:utils.CREER_PERSONNE,
            utils.NOM:nom,
            utils.PRENOM:prenom,
            utils.COURRIEL:courriel,
            utils.TELEPHONE_PERSONNE:telephone_personne,
            utils.ADRESSE:adresse
        }
        
        print(infos)
        return self.appel_serveur(infos)
    
    def creer_locateur(self,nom_compagnie,telephone_compagnie,adresse=""):
        infos = {
            utils.FONCTION:utils.CREER_LOCATEUR,
            utils.NOM_COMPAGNIE:nom_compagnie,
            utils.TELEPHONE_COMPAGNIE:telephone_compagnie,
            utils.ADRESSE:adresse
        }
        return self.appel_serveur(infos)
    
    
    def enregistrer_usager(self,personne_email,locateur_nom_compagnie,identifiant,mdp,permission):
        infos = {
            utils.FONCTION:utils.ENREGISTRER_USAGER,
            utils.PERSONNE_EMAIL:personne_email,
            utils.LOCATEUR_NOM_COMPAGNIE:locateur_nom_compagnie,
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
    
    def creer_client(self, locateur, client):
        infos = {
            utils.FONCTION:utils.CREER_LOCATEUR_CLIENT,
            utils.LOCATEUR:locateur,
            utils.CLIENT:client
        }
        return self.appel_serveur(infos)
    
    def get_client(self, locateur):
        infos = {
            utils.FONCTION:utils.SELECT_LOCATEUR_CLIENT,
            utils.LOCATEUR:locateur
        }    
        return self.appel_serveur(infos)
    
    def get_personne(self, personne):
        infos = {
            utils.FONCTION:utils.SELECT_PERSONNE,
            utils.PERSONNE:personne
        }
        return self.appel_serveur(infos)
    
    def get_employe(self, locateur):
        infos = {
            utils.FONCTION:utils.SELECT_USAGER,
            utils.LOCATEUR:locateur
        }    
        return self.appel_serveur(infos)
    
    
    
    

# test
def main():
    c = Controleur_Client()

    d = c.identifier_usager('boubou', '12345')

    
    print(d)
    return 0

if __name__ == '__main__':
    quit(main())