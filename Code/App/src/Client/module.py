from traceback import print_exc
from tkinter import Tk
from vue import Vue
from controleur_client import Controleur_Client
from sys import path

path.append('./Module/accueil')
from vue_accueil import Vue_accueil


class Module(Tk):
    def __init__(self):
        super().__init__()
        controleur = Controleur_Client()   
        self.login = Vue(self)
        self.login.grid(row=0, column=0, padx=10, pady=10)
        self.login.set_controleur(controleur)
        controleur.set_vue(self.login)
        
    def pageaccueil(self):
        Cl = Controleur_Client()
        l = Vue_accueil()
        # l.grid(row=0, column=0, padx=10, pady=10)
        l.set_controleur(Cl)
        Cl.set_vue(l)
    
def main():
    try:
        module = Module()
        # if module.login.clic_bouton_connexion():
        module.pageaccueil()
            
        
        module.mainloop()
    except:
        print_exc()
        return 1
    return 0

if __name__ == '__main__':
    quit(main())