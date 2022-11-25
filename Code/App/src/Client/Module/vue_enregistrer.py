import tkinter as tk
from tkinter import ttk
import os


from controleur_client import Controleur_Client




class Vue_enregistrer(tk.Frame):
    def __init__(self, parent,new_view):
        tk.Frame.__init__(self,parent)
        self.ctr_client = Controleur_Client()
        self.new_view = new_view
        self.remplir_vue()
        
        
    def open_file(self, file):
        os.system('python' + file)

   
    def remplir_vue(self):
       
        nom_text = ttk.Label(self, text="Nom : ")
        nom_text.grid(row=0, column=1,  pady=(5, 0), sticky=tk.E)
        
        self.nom_var = tk.StringVar()
        self.nom_edit = ttk.Entry(self, textvariable=self.nom_var, width=30)
        self.nom_edit.grid(row=0, column=2,  pady=(5, 0), sticky=tk.E)
        
        prenom_var = ttk.Label(self, text="Prenom : ")
        prenom_var.grid(row=1, column=1, pady=(5, 0), sticky=tk.E)
        
        self.prenom_var = tk.StringVar()
        self.prenom_edit = ttk.Entry(self, textvariable=self.prenom_var, width=30)
        self.prenom_edit.grid(row=1, column=2, pady=(5, 0), sticky=tk.E)
        
        courriel_text = ttk.Label(self, text="E-mail : ")
        courriel_text.grid(row=2, column=1, pady=(5, 0), sticky=tk.E)
        
        
        
        self.courriel_var= tk.StringVar()
        self.courriel_edit = ttk.Entry(self, textvariable=self.courriel_var, width=30)
        self.courriel_edit.grid(row=2, column=2, pady=(5, 0), sticky=tk.E)
        
    
        tel_text = ttk.Label(self, text="Tel# : ")
        tel_text.grid(row=3, column=1, pady=(5, 0), sticky=tk.E)
    
        self.tel_var = tk.StringVar()
        self.tel_edit = ttk.Entry(self, textvariable=self.tel_var, width=30)
        self.tel_edit.grid(row=3, column=2, pady=(5, 0), sticky=tk.E)
        
        adresse_text = ttk.Label(self, text="Adresse : ")
        adresse_text.grid(row=4, column=1, pady=(5, 0), sticky=tk.E)
        
        self.adresse_var = tk.StringVar()
        self.adresse_edit = ttk.Entry(self, textvariable=self.adresse_var, width=30)
        self.adresse_edit.grid(row=4, pady=(5, 0),column=2, sticky=tk.E)
        
        btn_1 = ttk.Button(self, text="Enregistrer", command=self.btn_enregistrer)
        btn_1.grid(row=6, column=2)

        btn_1 = ttk.Button(self, text="Back", command=self.forget)
        btn_1.grid(row=8, column=2)
    

    def btn_enregistrer(self):
          
        reponse = self.ctr_client.creer_personne(self.nom_var.get(), self.prenom_var.get(), self.courriel_var.get(), self.tel_var.get(), self.adresse_var.get())
            
        if len(reponse):
            self.afficher_succes(reponse)
            return True  
        else:
            self.afficher_erreur(f'Vide, remplis les cases, mon cher')
            return False
    
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