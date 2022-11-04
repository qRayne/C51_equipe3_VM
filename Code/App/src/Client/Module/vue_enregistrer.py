from cProfile import label
from tkinter import *
import tkinter as tk
import tkinter
from tkinter.ttk import *
import os

class Vue_enregistrer():
    def __init__(self):
        super().__init__()
        self.title = "Enregistrement"
        self.width = 1280
        self.height = 720
        self.master = None
        self.controleur = None
        self.remplir_vue()
      
       
    def set_controleur(self, controleur):
        self.controleur = controleur
        
    def open_file(self, file):
        os.system('python' + file)

    def label_vide(self, r, c):
        label = Label(self.master)
        label.grid(row=r, column=c,  pady=(5, 0))
        
    def remplir_vue(self):
        self.master = Tk()
        
        self.label_vide(0, 0)
        self.label_vide(1, 0)
        self.label_vide(2, 0)
        self.label_vide(3, 0)

        nom_text = Label(self.master, text="Nom : ")
        nom_text.grid(row=0, column=1,  pady=(5, 0), sticky=tk.E)
        
        self.nom_var = StringVar()
        self.nom_edit = Entry(self.master, textvariable=self.nom_var, width=30)
        self.nom_edit.grid(row=0, column=2,  pady=(5, 0), sticky=tk.E)
        
        prenom_var = Label(self.master, text="Prenom : ")
        prenom_var.grid(row=1, column=1, pady=(5, 0), sticky=tk.E)
        
        self.prenom_var = StringVar()
        self.prenom_edit = Entry(self.master, textvariable=self.prenom_var, width=30)
        self.prenom_edit.grid(row=1, column=2, pady=(5, 0), sticky=tk.E)
        
        courriel_text = Label(self.master, text="E-mail : ")
        courriel_text.grid(row=2, column=1, pady=(5, 0), sticky=tk.E)
        
        
        self.courriel_var= StringVar()
        self.courriel_edit = Entry(self.master, textvariable=self.courriel_var, width=30)
        self.courriel_edit.grid(row=2, column=2, pady=(5, 0), sticky=tk.E)
        
    
        tel_text = Label(self.master, text="Tel# : ")
        tel_text.grid(row=3, column=1, pady=(5, 0), sticky=tk.E)
    
        self.tel_var = StringVar()
        self.tel_edit = Entry(self.master, textvariable=self.tel_var, width=30)
        self.tel_edit.grid(row=3, column=2, pady=(5, 0), sticky=tk.E)
        
        adresse_text = Label(self.master, text="Adresse : ")
        adresse_text.grid(row=4, column=1, pady=(5, 0), sticky=tk.E)
        
        self.adresse_var = StringVar()
        self.adresse_edit = Entry(self.master, textvariable=self.adresse_var, width=30)
        self.adresse_edit.grid(row=4, pady=(5, 0),column=2, sticky=tk.E)
        
        
        btn_1 = Button(self.master, text="Enregistrer", command=self.btn_enregistrer)        
        btn_1.grid(row=6, column=2)
                
      
        self.master.mainloop()
        

    def btn_enregistrer(self):
        if self.controleur:
            #message d'erreur par controleur ou par vue?
            reponse = self.controleur.creer_personne(self.nom_var.get(), self.prenom_var.get(), self.courriel_var.get(), self.tel_var.get(), self.adresse_var.get())
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