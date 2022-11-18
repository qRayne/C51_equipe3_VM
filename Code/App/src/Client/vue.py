import tkinter as tk
from tkinter import Toplevel, ttk
from sys import path

path.append('./Module')
from controleur_client import Controleur_Client

path.append('./Module')
from vue_enregistrer import Vue_enregistrer

path.append('./Module')
from vue_accueil import Vue_accueil

class Vue(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.ctrl_client = Controleur_Client()
        self.remplir_vue()
        # self.module = Module()
        self.if_enregistrer = False;
        
    def set_controleur(self, controleur):
        self.ctrl_client = controleur

    def remplir_vue(self):
        self.label_nom = ttk.Label(self, text='Nom ')
        self.label_nom.grid(row=1, column=0, pady=(5, 0), sticky=tk.E)

        self.var_nom = tk.StringVar()
        self.input_nom = ttk.Entry(self, textvariable=self.var_nom, width=30)
        self.input_nom.grid(row=1, column=1, sticky=tk.E)

        self.label_mdp = ttk.Label(self, text='Mot de passe ')
        self.label_mdp.grid(row=2, column=0, pady=(5, 0), sticky=tk.E)

        self.var_mdp = tk.StringVar()
        self.input_mdp = ttk.Entry(self, textvariable=self.var_mdp, show='*', width=30)
        self.input_mdp.grid(row=2, column=1, sticky=tk.E)
        
        self.bouton_enregistrer = ttk.Button(self, text='Enregistrer', command=self.btn_enregistrer)
        self.bouton_enregistrer.bind('<Return>', lambda e: self.bouton_connexion.invoke())
        self.bouton_enregistrer.grid(row=6, column=0, pady=(20, 0), sticky=tk.E)
        
        self.bouton_connexion = ttk.Button(self, text='Connexion', command=self.clic_bouton_connexion)
        self.bouton_connexion.bind('<Return>', lambda e: self.bouton_connexion.invoke())
        self.bouton_connexion.grid(row=3, column=1, pady=(20, 0), sticky=tk.E)
        
        self.bouton_annuler = ttk.Button(self, text='Annuler', command=self.btn_annuler)
        self.bouton_annuler.bind('<Return>', lambda e: self.bouton_annuler.invoke())
        self.bouton_annuler.grid(row=4, column=1, pady=(10, 0), sticky=tk.E)
        
        self.label_message = ttk.Label(self, text='', foreground='red')
        self.label_message.grid(row=5, column=0, columnspan=2, sticky=tk.W)

    def clic_bouton_connexion(self):
        if self.ctrl_client:
            #message d'erreur par controleur ou par vue?
            reponse = self.ctrl_client.identifier_usager(self.var_nom.get(), self.var_mdp.get())
            print(self.var_nom.get())
            print(self.var_mdp.get())
            print(reponse)
            
            
            if len(reponse):
                print('reposnse')
                self.afficher_succes(reponse)
                return True  
            else:
                self.afficher_erreur(f'Nom ou mot de passe incorrects')
                return False
            
    def btn_enregistrer(self):
        # layout_enregistrer = Vue_enregistrer()
        layout_enregistrer = Toplevel()
        layout_enregistrer.title("Projet")
       
        pseudo_text = ttk.Label(layout_enregistrer, text="Pseudo : ")
        pseudo_text.grid(row=0, column=1,  pady=(5, 0), sticky=tk.E)
        
        self.pseudo_var = tk.StringVar()
        self.pseudo_edit = ttk.Entry(layout_enregistrer, textvariable=self.pseudo_var, width=30)
        self.pseudo_edit.grid(row=0, column=2,  pady=(5, 0), sticky=tk.E)
       
        nom_text = ttk.Label(layout_enregistrer, text="Nom : ")
        nom_text.grid(row=1, column=1,  pady=(5, 0), sticky=tk.E)
        
        self.nom_var = tk.StringVar()
        self.nom_edit = ttk.Entry(layout_enregistrer, textvariable=self.nom_var, width=30)
        self.nom_edit.grid(row=1, column=2,  pady=(5, 0), sticky=tk.E)      
        
        prenom_var = ttk.Label(layout_enregistrer, text="Prenom : ")
        prenom_var.grid(row=2, column=1, pady=(5, 0), sticky=tk.E)
        
        self.prenom_var = tk.StringVar()
        self.prenom_edit = ttk.Entry(layout_enregistrer, textvariable=self.prenom_var, width=30)
        self.prenom_edit.grid(row=2, column=2, pady=(5, 0), sticky=tk.E)
        
        courriel_text = ttk.Label(layout_enregistrer, text="E-mail : ")
        courriel_text.grid(row=3, column=1, pady=(5, 0), sticky=tk.E)
        
        self.courriel_var= tk.StringVar()
        self.courriel_edit = ttk.Entry(layout_enregistrer, textvariable=self.courriel_var, width=30)
        self.courriel_edit.grid(row=3, column=2, pady=(5, 0), sticky=tk.E)
        
    
        tel_text = ttk.Label(layout_enregistrer, text="Tel# : ")
        tel_text.grid(row=4, column=1, pady=(5, 0), sticky=tk.E)
    
        self.tel_var = tk.StringVar()
        self.tel_edit = ttk.Entry(layout_enregistrer, textvariable=self.tel_var, width=30)
        self.tel_edit.grid(row=4, column=2, pady=(5, 0), sticky=tk.E)
        
        adresse_text = ttk.Label(layout_enregistrer, text="Adresse : ")
        adresse_text.grid(row=5, column=1, pady=(5, 0), sticky=tk.E)
        
        self.adresse_var = tk.StringVar()
        self.adresse_edit = ttk.Entry(layout_enregistrer, textvariable=self.adresse_var, width=30)
        self.adresse_edit.grid(row=5, pady=(5, 0),column=2, sticky=tk.E)
        
        locateur_text = ttk.Label(layout_enregistrer, text="Locateur : ")
        locateur_text.grid(row=6, column=1, pady=(5, 0), sticky=tk.E)
        
        self.locateur_var = tk.StringVar()
        self.locateur_edit = ttk.Entry(layout_enregistrer, textvariable=self.locateur_var, width=30)
        self.locateur_edit.grid(row=6, pady=(5, 0),column=2, sticky=tk.E)
        
        mdp_text = ttk.Label(layout_enregistrer, text="Mot de passe : ")
        mdp_text.grid(row=7, column=1, pady=(5, 0), sticky=tk.E)
        
        self.mdp_var = tk.StringVar()
        self.mdp_edit = ttk.Entry(layout_enregistrer, textvariable=self.mdp_var, width=30)
        self.mdp_edit.grid(row=7, pady=(5, 0),column=2, sticky=tk.E)
        
        btn_1 = ttk.Button(layout_enregistrer, text="Enregistrer", command=self.clic_enregistrer)
        btn_1.grid(row=8, column=2)
        
    def clic_enregistrer(self):
        print("clic enregistrer") 
        self.ctrl_client.creer_personne(self.nom_var.get(), self.prenom_var.get(), self.courriel_var.get(), self.tel_var.get(), self.adresse_var.get())
        self.ctrl_client.enregistrer_usager(self.courriel_var.get(), self.locateur_var.get(), self.nom_var.get(), self.mdp_var.get(), 'admin')
        if (self.nom_var.get()):
            self.afficher_succes(self.nom_var)
            return True  
        else:
            self.afficher_erreur(f'Vide, remplis les cases, mon cher')
            return False
        
    def btn_connexion(self):
        layout_enregistrer = Vue_accueil()
        # l.grid(row=0, column=0, padx=10, pady=10)
        layout_enregistrer.set_controleur(self.ctrl_client)
        self.ctrl_client.set_vue(layout_enregistrer)
        self.if_enregistrer = True;
            
    # def clic_bouton_enregistrer(self):
    #     layout_enregistrer = Vue_enregistrer()
    #     # l.grid(row=0, column=0, padx=10, pady=10)
    #     layout_enregistrer.set_controleur(self.controleur)
    #     self.controleur.set_vue(layout_enregistrer)
    #     self.if_enregistrer = True;
        
    def if_clic_enregistrer(self):
        return self.if_enregistrer;
    
    def clicked_enregistrer(self):
        self.if_enregistrer = False;
         
    def btn_annuler(self):
        self.var_nom.set('')
        self.var_mdp.set('')

    def afficher_erreur(self, message):
        self.label_message['text'] = message
        self.label_message['foreground'] = 'red'
        self.label_message.after(3000, self.cacher_message)
        self.input_nom['foreground'] = 'red'
        self.input_mdp['foreground'] = 'red'

    def afficher_succes(self, message):
        self.label_message['text'] = message
        self.label_message['foreground'] = 'green'
        self.label_message.after(3000, self.cacher_message)
        self.input_nom['foreground'] = 'black'
        #self.var_nom.set(self.input_nom)
        self.input_mdp['foreground'] = 'black'
        #self.var_mdp.set(self.input_mdp)

    def cacher_message(self):
        self.label_message['text'] = ''
