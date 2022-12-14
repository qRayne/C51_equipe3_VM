from sys import path

path.append("..")
import tkinter as tk
from tkinter import Toplevel, ttk
import os
from Utils import utils
from controleur_client import Controleur_Client

# TODO: facture, messagerie, developpeur, admin

class VueAccueil(ttk.Frame):
    def __init__(self, parent, controleur_client):
        super().__init__(parent)
        self.parent = parent
        self.controleur_client = controleur_client
        self.user = self.controleur_client.get_utilisateur(self.controleur_client.credentials["user"])
        self.topProjet = None
        
    def open_file(self, file):
        os.system('python' + file)
    
    def remplir_vue(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        
        self.name = self.controleur_client.get_personne(self.user[0][1])
        self.locateur = self.controleur_client.get_locateur(self.controleur_client.credentials["locateur"])[0][1]
        
        self.x = 350
        self.y = 50
        
        self.var_name = tk.StringVar()
        self.var_name = self.name[0][1]
        
        self.parent.geometry('720x480')
        self.parent.configure(background="#2596be")
        
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TButton', font=('Times New Roman', 10), background='#232323', foreground='white')
        style.configure('TFrame', background='#2596be')
        style.configure('TLabel', background='#2596be')
        
        if self.controleur_client.credentials["permissions"] == 'admin':
            btn_1 = ttk.Button(self, text="Creer Personne", command=self.open_enregistrer)        
            btn_1.place(x = 325, y=50)
            
            btn_2 = ttk.Button(self, text="Materiel", command=self.open_materiel)
            btn_2.place(x = 325, y=80)
            
            btn_3 = ttk.Button(self, text="Projet", command=self.open_projet)
            btn_3.place(x = 325, y=110)
                    
            btn_4 = ttk.Button(self, text="Clients", command=self.open_client)
            btn_4.place(x = 325, y=140)
            
            btn_5 = ttk.Button(self, text="Employe", command=self.open_employe)
            btn_5.place(x = 325, y=170)
                    
            btn_6 = ttk.Button(self, text="Facture", command=self.open_facture)
            btn_6.place(x = 325, y=200)
                    
            btn_7 = ttk.Button(self, text="Messagerie", command=self.open_messagerie)
            btn_7.place(x = 325, y=230)
                    
            btn_8 = ttk.Button(self, text="Developpeur", command=self.open_developpeur)
            btn_8.place(x = 325, y=260)
                    
            btn_9 = ttk.Button(self, text="Admin", command=self.open_admin)
            btn_9.place(x = 325, y=290)
    
        first_name = ttk.Label(self, text='NAME : ' + self.var_name)
        first_name.place(x = 0, y=0)
        
        title_name = ttk.Label(self, text="COMPAGNIE : " + str(self.locateur))
        title_name.place(x = 0, y=15)
        
        btn_9 = ttk.Button(self, text="Quitter", command=self.quitter)
        btn_9.place(x=0, y=35)
        
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
        
        self.checkUsager = ttk.Checkbutton(self.topProjet_enregsiter, text = "Cr??er usager?", command=self.isCheckedUsager)
        self.checkUsager.grid(row=6, column=1)
        
        self.checkClient = ttk.Checkbutton(self.topProjet_enregsiter, text = "Cr??er client?", command=self.isCheckedClient)
        self.checkClient.grid(row=6, column=3)
        
        btn_1 = ttk.Button(self.topProjet_enregsiter, text="Enregistrer", command=self.btn_savepersonne)
        btn_1.grid(row=6, column=2)    
        
    def open_usager(self):
        self.topProjet = Toplevel()
        self.topProjet.title("Cr??er Usager")
        
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
        
    def open_client(self):
        
        liste_client = self.controleur_client.get_client(self.controleur_client.credentials["locateur"])
        
        self.top_client = Toplevel()
        self.top_client.title("Client")
        
        nom_col = ["id", "pseudo", "prenom", "courriel", "num telephone", "adresse"]
        
        for i, col in enumerate(nom_col):
            frame_employe = tk.Frame(master=self.top_client, relief=tk.FLAT, borderwidth=2)
            frame_employe.grid(row=0, column=i)
            labelGrid = tk.Label(master=frame_employe, text=col)
            labelGrid.pack()
            
        for y in range(6):
            for x, cli in enumerate(liste_client):
                client = self.controleur_client.get_personne(cli[0])
                frame_employe = tk.Frame(master=self.top_client, relief=tk.FLAT, borderwidth=2)
                frame_employe.grid(row=(x + 1), column=y)
                labelGrid = tk.Label(master=frame_employe, text=str(client[0][y]))
                labelGrid.pack()
        self.text_liste = tk.Text(frame_employe, width= 100, height=50)
        
    def open_employe(self):
        
        liste_emp = self.controleur_client.get_employe(self.controleur_client.credentials["locateur"]) 
        
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
                employe = self.controleur_client.get_personne(emp[0])
                frame_employe = tk.Frame(master=self.top_employe, relief=tk.FLAT, borderwidth=2)
                frame_employe.grid(row=(x + 1), column=y)
                labelGrid = tk.Label(master=frame_employe, text=str(employe[0][y]))
                labelGrid.pack()
        self.text_liste = tk.Text(frame_employe, width= 100, height=50)
        
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
        
    def quitter(self):
        #self.parent.destroy()
        # ici il se log so on reset les deux permissions
        self.parent.show_frame(self, utils.VUE_LOGIN)
        
    def btn_savepersonne(self):
        self.controleur_client.creer_personne(self.nom_var.get(), 
                                              self.prenom_var.get(), 
                                              self.courriel_var.get(), 
                                              self.tel_var.get(), 
                                              self.adresse_var.get())
        
        if self.isCheckedUsager():
            
            self.open_usager()  
            
        if self.isCheckedClient():
            client = self.controleur_client.get_personne_courriel(self.courriel_var.get())
            self.controleur_client.creer_client(self.controleur_client.credentials["locateur"], 
                                                client[0][0])  
    
        self.topProjet_enregsiter.destroy()
        
    def btn_saveusager(self):

        self.controleur_client.enregistrer_usager(self.courriel_var.get(), 
                                                 self.controleur_client.get_locateur(self.controleur_client.credentials["locateur"])[0][1],
                                                 self.id_var.get(), self.mdp_var.get(), "user")
        self.topProjet.destroy() 
            
    def isCheckedUsager(self):
        if "selected" in str(self.checkUsager.state()):
            self.checkClient.grid_forget()
            return True
        else:
            self.checkClient.grid(row=6, column=3)
            return False
        
    def isCheckedClient(self):
        if "selected" in str(self.checkClient.state()):
            self.checkUsager.grid_forget()
            return True
        else:
            self.checkUsager.grid(row=6, column=1)
            return False