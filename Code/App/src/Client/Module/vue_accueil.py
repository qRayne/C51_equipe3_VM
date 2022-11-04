from tkinter import *
from tkinter.ttk import *
import os

class Vue_accueil():
    def __init__(self):
        super().__init__()
        self.title = "Page d'acceuil"
        self.width = 1280
        self.height = 720
        self.master = None
        self.controleur = None
        self.remplir_vue()

    def set_controleur(self, controleur):
        self.controleur = controleur
        
    def open_file(self, file):
        os.system('python' + file)

    def remplir_vue(self):
        self.master = Tk()
        
        label = Label(self.master, text="test")
        
        last_name = Label(self.master, text="last name")
        last_name.grid(row=0, column=0)
        
        first_name = Label(self.master, text="first name")
        first_name.grid(row=0, column=1)
        
        title_name = Label(self.master, text="title name")
        title_name.grid(row=0, column=5)
        
        btn_1 = Button(self.master, text="Enregistrer", command=self.open_enregistrer)        
        btn_1.grid(row=2, column=2)
        
        btn_2 = Button(self.master, text="Materiel", command=self.open_materiel)
        btn_2.grid(row=3, column=2)
        
        btn_3 = Button(self.master, text="Projet", command=self.open_projet)
        btn_3.grid(row=4, column=2)
                
        btn_4 = Button(self.master, text="Locaux", command=self.open_locaux)
        btn_4.grid(row=5, column=2)
        
        btn_4 = Button(self.master, text="Employe", command=self.open_employe)
        btn_4.grid(row=6, column=2)
                
        btn_4 = Button(self.master, text="Facture", command=self.open_facture)
        btn_4.grid(row=7, column=2)
                
        btn_4 = Button(self.master, text="Messagerie", command=self.open_messagerie)
        btn_4.grid(row=8, column=2)
                
        btn_4 = Button(self.master, text="Developpeur", command=self.open_developpeur)
        btn_4.grid(row=9, column=2)
                
        btn_4 = Button(self.master, text="Admin", command=self.open_admin)
        btn_4.grid(row=10, column=2)
                
        self.master.mainloop()
        

        
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
        