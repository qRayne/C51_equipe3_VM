import tkinter as tk
from tkinter import Toplevel, ttk
import os

from controleur_client import Controleur_Client

class Vue_accueil(tk.Frame):
    def __init__(self, parent, new_view):
        tk.Frame.__init__(self, parent)
        self.new_view = new_view
        self.ctrl_client = Controleur_Client()
        self.topProjet = None
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
        
        btn_1 = ttk.Button(self, text="Creer Personne", command=self.open_enregistrer)        
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
        
        btn_9 = ttk.Button(self, text="Admin", command=self.open_admin)
        btn_9.place(x=self.x , y=self.y+240)
        

    def open_enregistrer(self):
        self.topProjet_enregsiter = Toplevel()
        self.topProjet_enregsiter.title("Enregistrer")
        nom_text = ttk.Label(self.topProjet_enregsiter, text="Nom : ")
        nom_text.grid(row=0, column=1,  pady=(5, 0), sticky=tk.E)
        
        self.nom_var = tk.StringVar()
        self.nom_edit = ttk.Entry(self.topProjet_enregsiter, textvariable=self.nom_var, width=30)
        self.nom_edit.grid(row=0, column=2,  pady=(5, 0), sticky=tk.E)
        
        prenom_var = ttk.Label(self.topProjet_enregsiter, text="Prenom : ")
        prenom_var.grid(row=1, column=1, pady=(5, 0), sticky=tk.E)
        
        self.prenom_var = tk.StringVar()
        self.prenom_edit = ttk.Entry(self.topProjet_enregsiter, textvariable=self.prenom_var, width=30)
        self.prenom_edit.grid(row=1, column=2, pady=(5, 0), sticky=tk.E)
        
        courriel_text = ttk.Label(self.topProjet_enregsiter, text="E-mail : ")
        courriel_text.grid(row=2, column=1, pady=(5, 0), sticky=tk.E)
        
        self.courriel_var= tk.StringVar()
        self.courriel_edit = ttk.Entry(self.topProjet_enregsiter, textvariable=self.courriel_var, width=30)
        self.courriel_edit.grid(row=2, column=2, pady=(5, 0), sticky=tk.E)
    
        tel_text = ttk.Label(self.topProjet_enregsiter, text="Tel# : ")
        tel_text.grid(row=3, column=1, pady=(5, 0), sticky=tk.E)
    
        self.tel_var = tk.StringVar()
        self.tel_edit = ttk.Entry(self.topProjet_enregsiter, textvariable=self.tel_var, width=30)
        self.tel_edit.grid(row=3, column=2, pady=(5, 0), sticky=tk.E)
        
        adresse_text = ttk.Label(self.topProjet_enregsiter, text="Adresse : ")
        adresse_text.grid(row=4, column=1, pady=(5, 0), sticky=tk.E)
        
        self.adresse_var = tk.StringVar()
        self.adresse_edit = ttk.Entry(self.topProjet_enregsiter, textvariable=self.adresse_var, width=30)
        self.adresse_edit.grid(row=4, pady=(5, 0),column=2, sticky=tk.E)
        
        self.check = ttk.Checkbutton(self.topProjet_enregsiter, text = "Créer usager?", command=self.isChecked)
        self.check.grid(row=6, column=1)
        
        btn_1 = ttk.Button(self.topProjet_enregsiter, text="Enregistrer", command=self.btn_savepersonne)
        btn_1.grid(row=6, column=2)
        
    def isChecked(self):
        if "selected" in str(self.check.state()):
            return True
        else:
            return False
            
        
    def open_usager(self):
        self.topProjet = Toplevel()
        self.topProjet.title("Créer Usager")
        
        id_text = ttk.Label(self.topProjet, text="Identifiant : ")
        id_text.grid(row=0, column=1,  pady=(5, 0), sticky=tk.E)
        
        self.id_var = tk.StringVar()
        self.id_edit = ttk.Entry(self.topProjet, textvariable=self.id_var, width=30)
        self.id_edit.grid(row=0, column=2,  pady=(5, 0), sticky=tk.E)
        
        mdp_var = ttk.Label(self.topProjet, text="Mot de passe : ")
        mdp_var.grid(row=1, column=1, pady=(5, 0), sticky=tk.E)
        
        self.mdp_var = tk.StringVar()
        self.mdp_edit = ttk.Entry(self.topProjet, textvariable=self.mdp_var, width=30)
        self.mdp_edit.grid(row=1, column=2, pady=(5, 0), sticky=tk.E)
        
        btn_1 = ttk.Button(self.topProjet, text="Enregistrer", command=self.btn_saveusager)
        btn_1.grid(row=2, column=1)
        
    def open_materiel(self):
        self.topProjet = Toplevel()
        self.topProjet.title("Materiel")
        
    def open_projet(self):
        self.topProjet = Toplevel()
        self.topProjet.title("Projet")
        
    def open_locaux(self):
        self.topProjet = Toplevel()
        self.topProjet.title("Locaux")
        
    def open_employe(self):
        
        liste_emp = self.ctrl_client.get_employe(1)
        
        self.top_employe = Toplevel()
        self.top_employe.title("employe")
        
        nom_col = ["id", "pseudo", "prenom", "courriel", "num telephone", "adresse"]
        
        for i, col in enumerate(nom_col):
            frame_employe = tk.Frame(master=self.top_employe, relief=tk.FLAT, borderwidth=2)
            frame_employe.grid(row=0, column=i)
            labelGrid = tk.Label(master=frame_employe, text=col)
            labelGrid.pack()
            
        for y in range(6):
            for x, emp in enumerate(liste_emp):
                employe = self.ctrl_client.get_personne(emp[0])
                frame_employe = tk.Frame(master=self.top_employe, relief=tk.FLAT, borderwidth=2)
                frame_employe.grid(row=(x + 1), column=y)
                labelGrid = tk.Label(master=frame_employe, text=str(employe[0][y]))
                labelGrid.pack()
        self.text_liste = tk.Text(frame_employe, width= 100, height=50)
        

        # for i, emp in enumerate(liste_emp):
        #     employe = self.ctrl_client.get_personne(emp[0])
        #     self.text_liste.insert(str(i) + '.0' , str(employe[0][1]) + '\n')
        #     print(employe)
        
        # self.text_liste.pack()
        # self.text_liste['state'] = 'disabled'
        
    def open_facture(self):
        self.topProjet = Toplevel()
        self.topProjet.title("facture")
        
    def open_messagerie(self):
        self.topProjet = Toplevel()
        self.topProjet.title("messagerie")
        
    def open_developpeur(self):
        self.topProjet = Toplevel()
        self.topProjet.title("developpeur")
        
    def open_admin(self):
        self.topProjet = Toplevel()
        self.topProjet.title("admin")
        
    def btn_savepersonne(self):
        self.ctrl_client.creer_personne(self.nom_var.get(), self.prenom_var.get(), self.courriel_var.get(), self.tel_var.get(), self.adresse_var.get())
        
        if self.isChecked():
            self.open_usager()  
            
        self.topProjet_enregsiter.destroy()
        
    def btn_saveusager(self):
        self.ctrl_client.enregistrer_usager(self.courriel_var.get(),"Bell",self.id_var.get(), self.mdp_var.get(), "user")
        self.topProjet.destroy() 
        