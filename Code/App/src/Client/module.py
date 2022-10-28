from traceback import print_exc
from tkinter import Tk

from vue import Vue
from controleur_client import Controleur_Client
from sys import path

path.append('./Module')
from vue_accueil import Vue_accueil

path.append('./Module')
from vue_enregistrer import Vue_enregistrer

class Module(Tk):
    def __init__(self):
        super().__init__()
        self.controleur = Controleur_Client()   
        self.login = Vue(self)
        self.login.grid(row=0, column=0, padx=10, pady=10)
        self.login.set_controleur(self.controleur)
        self.controleur.set_vue(self.login)
        
    def page_accueil(self):
        layout_accueil = Vue_accueil()
        # l.grid(row=0, column=0, padx=10, pady=10)
        layout_accueil.set_controleur(self.controleur)
        self.controleur.set_vue(layout_accueil)
        
    def page_enregistrer(self):
        layout_enregistrer = Vue_enregistrer()
        # l.grid(row=0, column=0, padx=10, pady=10)
        layout_enregistrer.set_controleur(self.controleur)
        self.controleur.set_vue(layout_enregistrer)
    
def main():
    try:
        module = Module()
        
        if (module.login.if_enregistrer):
            module.page_enregistrer()
            module.login.clicked_enregistrer;
            
        
        #print(module.login.clic_bouton_connexion())
        #module.login.afficher_succes()
        # module.page_accueil()
            
        
        module.mainloop()
    except:
        print_exc()
        return 1
    return 0

if __name__ == '__main__':
    quit(main())