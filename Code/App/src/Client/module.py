from traceback import print_exc
from tkinter import Tk
from vue import Vue
from controleur_client import Controleur_Client
from sys import path
path.append('./Module/landing')
from controleur import Controleur_landing 
path.append('./Module/landing')
from vue_landing import Vue_landing


class Module(Tk):
    def __init__(self):
        super().__init__()
        controleur = Controleur_Client()   
        login = Vue(self)
        login.grid(row=0, column=0, padx=10, pady=10)
        login.set_controleur(controleur)
        controleur.set_vue(login)
        
        Cl = Controleur_landing()
        l = Vue_landing()
        # l.grid(row=0, column=0, padx=10, pady=10)
        l.set_controleur(Cl)
        Cl.set_vue(l)
    
    
        
        
        

def main():
    try:
        module = Module()
        module.mainloop()
    except:
        print_exc()
        return 1
    return 0

if __name__ == '__main__':
    quit(main())