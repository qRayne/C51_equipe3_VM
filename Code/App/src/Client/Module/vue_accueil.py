from ast import Mod
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

        self.x = 350
        self.y = 50
        
        self.var_name = tk.StringVar()
        self.var_name = self.name[0][1]

        first_name = ttk.Label(self, text='name : ' + self.var_name)
        first_name.grid(row=0, column=1)
        
        title_name = ttk.Label(self, text="title name")
        title_name.place(x=700, y=0)
        
        btn_1 = ttk.Button(self, text="Enregistrer", command=self.open_enregistrer)        
        btn_1.place(x=self.x, y=self.y)
        
        btn_2 = ttk.Button(self, text="Materiel", command=self.open_materiel)
        btn_2.place(x=self.x , y=self.y+30)
        
        btn_3 = ttk.Button(self, text="Projet", command=self.open_projet)
        btn_3.place(x=self.x , y=self.y+60)
                
        btn_4 = ttk.Button(self, text="Locaux", command=self.open_locaux)
        btn_4.place(x=self.x , y=self.y+90)
        
        btn_5 = ttk.Button(self, text="Employe", command=self.open_employe)
        btn_5.place(x=self.x , y=self.y+120)
                
        btn_6 = ttk.Button(self, text="Facture", command=self.open_facture)
        btn_6.place(x=self.x , y=self.y+150)
                
        btn_7 = ttk.Button(self, text="Messagerie", command=self.open_messagerie)
        btn_7.place(x=self.x , y=self.y+180)
                
        btn_8 = ttk.Button(self, text="Developpeur", command=self.open_developpeur)
        btn_8.place(x=self.x , y=self.y+210)
                
        btn_9 = ttk.Button(self, text="Admin", command=self.open_admin)
        btn_9.place(x=self.x , y=self.y+240)
        

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
        