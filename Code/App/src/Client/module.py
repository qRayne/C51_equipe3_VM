from sys import path
from tkinter import ttk

path.append("..")

from traceback import print_exc
import tkinter as tk
from vue_login import VueLogin
from vue_accueil import VueAccueil
from controleur_client import Controleur_Client

from Utils import utils

VUES = [VueLogin, VueAccueil]

class Module(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Gestion')
        self.controleur_client = Controleur_Client()
        self.show_frame(None, utils.VUE_LOGIN)

    def show_frame(self, instance_vue_courante, index_class_vue):
        if instance_vue_courante is not None:
            for widget in instance_vue_courante.winfo_children():
                widget.destroy()
            instance_vue_courante.destroy()
        self.frame = VUES[index_class_vue](self, self.controleur_client)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.frame.grid(row = 0, column = 0, sticky = "nsew")
        self.frame.remplir_vue()
    
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