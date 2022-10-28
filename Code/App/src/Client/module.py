from traceback import print_exc
from tkinter import Tk

from vue import Vue
from controleur_client import Controleur_Client
from sys import path

path.append('./Module')
from vue_accueil import Vue_accueil

path.append('./Module')
from vue_enregistrer import Vue_enregistre



class Module(Tk):
    def __init__(self):
        super().__init__()
        self.controleur = Controleur_Client()   
        self.login = Vue(self)
        self.login.grid(row=0, column=0, padx=10, pady=10)
        self.login.set_controleur(self.controleur)
        self.controleur.set_vue(self.login)
        
    def pageaccueil(self):
    
        layout_accueil = Vue_accueil()
        # l.grid(row=0, column=0, padx=10, pady=10)
        layout_accueil.set_controleur(self.controleur)
        self.controleur.set_vue(layout_accueil)
        
    def pageaccueil(self):
        layout_enregistre = Vue_enregistre()
        # l.grid(row=0, column=0, padx=10, pady=10)
        layout_enregistre.set_controleur(self.controleur)
        self.controleur.set_vue(layout_enregistre)
    
def main():
    try:
        module = Module()
        #print(module.login.clic_bouton_connexion())
        #module.login.afficher_succes()
        #module.pageaccueil()
            
        
        module.mainloop()
    except:
        print_exc()
        return 1
    return 0

if __name__ == '__main__':
    quit(main())