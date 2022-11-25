import tkinter as tk
from tkinter import Toplevel, ttk
import os

from vue_enregistrer import Vue_enregistrer
from controleur_client import Controleur_Client

class Vue_accueil(tk.Frame):
    def __init__(self, parent, new_view):
        tk.Frame.__init__(self, parent)
        self.new_view = new_view
        self.ctrl_client = Controleur_Client()
        self.remplir_vue()
        
    def open_file(self, file):
        os.system('python' + file)
    
    def remplir_vue(self):
        self.name = self.ctrl_client.get_employe(1)

        self.var_name = tk.StringVar()
        self.var_name = self.name[0][1]

        first_name = ttk.Label(self, text='name : ' + self.var_name)
        first_name.grid(row=0, column=1)
        
        title_name = ttk.Label(self, text="title name")
        title_name.grid(row=0, column=5)
        
        btn_1 = ttk.Button(self, text="Enregistrer", command=self.open_enregistrer)        
        btn_1.grid(row=2, column=2)
        
        btn_2 = ttk.Button(self, text="Materiel", command=self.open_materiel)
        btn_2.grid(row=3, column=2)
        
        btn_3 = ttk.Button(self, text="Projet", command=self.open_projet)
        btn_3.grid(row=4, column=2)
                
        btn_4 = ttk.Button(self, text="Locaux", command=self.open_locaux)
        btn_4.grid(row=5, column=2)
        
        btn_4 = ttk.Button(self, text="Employe", command=self.open_employe)
        btn_4.grid(row=6, column=2)
                
        btn_4 = ttk.Button(self, text="Facture", command=self.open_facture)
        btn_4.grid(row=7, column=2)
                
        btn_4 = ttk.Button(self, text="Messagerie", command=self.open_messagerie)
        btn_4.grid(row=8, column=2)
                
        btn_4 = ttk.Button(self, text="Developpeur", command=self.open_developpeur)
        btn_4.grid(row=9, column=2)
                
        btn_4 = ttk.Button(self, text="Admin", command=self.open_admin)
        btn_4.grid(row=10, column=2)

        btn_4 = ttk.Button(self, text="Enregistrer", command=lambda : self.new_view.show_frame(Vue_enregistrer))
        btn_4.place(x=300,y=300)
        

    def open_enregistrer(self):
        topProjet = Toplevel()
        topProjet.title("Enregistrer")
        
    def open_materiel(self):
        topProjet = Toplevel()
        topProjet.title("Materiel")
        
    def open_projet(self):
        topProjet = Toplevel()
        topProjet.title("Projet")
        
    def open_locaux(self):
        topProjet = Toplevel()
        topProjet.title("Locaux")
        
    def open_employe(self):
        topProjet = Toplevel()
        topProjet.title("employe")
        
    def open_facture(self):
        topProjet = Toplevel()
        topProjet.title("facture")
        
    def open_messagerie(self):
        topProjet = Toplevel()
        topProjet.title("messagerie")
        
    def open_developpeur(self):
        topProjet = Toplevel()
        topProjet.title("developpeur")
        
    def open_admin(self):
        topProjet = Toplevel()
        topProjet.title("admin")
        