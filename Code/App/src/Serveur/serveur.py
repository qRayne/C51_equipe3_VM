from controleur_serveur import Controleur_Serveur
from serveur_web import Serveur_Web
import os

from sys import path
path.append('../Utils')
import utils

def main():
    controleur = Controleur_Serveur()

    Serveur_Web.set_controleur(controleur)
    Serveur_Web.lancer(utils.HOTE, utils.PORT)

    return 0

if __name__ == '__main__':
    # os.system('python dao.py')
    # os.system('python tester_tables_dao.py')
    # os.system('python Code/App/src/Serveur/dao.py')
    # os.system('python Code/App/src/Serveur/tester_tables_dao.py')
    # os.system('python Code/App/src/Serveur/serveur.py')
    
    # os.system('python Code/App/src/Client/module.py')
    quit(main())
