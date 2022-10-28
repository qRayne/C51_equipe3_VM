from cProfile import label
from tkinter import *
import tkinter as tk
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

        identifiant_text = Label(self.master, text="ID: ") # prenom
        identifiant_text.grid(row=0, column=1,  pady=(5, 0), sticky=tk.E)
        
        self.var_identifiant = StringVar()
        self.input_identifiant = Entry(self.master, textvariable=self.var_identifiant, width=30)
        self.input_identifiant.grid(row=0, column=2,  pady=(5, 0), sticky=tk.E)
        
        nom_company_text = Label(self.master, text="Compagnie: ") # nom Compagnie
        nom_company_text.grid(row=1, column=1, pady=(5, 0), sticky=tk.E)
        
        self.var_name_compagny = StringVar()
        self.input_name_company = Entry(self.master, textvariable=self.var_name_compagny, width=30)
        self.input_name_company.grid(row=1, column=2, pady=(5, 0), sticky=tk.E)
        
        email_text = Label(self.master, text="E-mail: ") # mail
        email_text.grid(row=2, column=1, pady=(5, 0), sticky=tk.E)
        
        
        self.var_email= StringVar()
        self.input_email = Entry(self.master, textvariable=self.var_email, width=30)
        self.input_email.grid(row=2, column=2, pady=(5, 0), sticky=tk.E)
        
    
        password_text = Label(self.master, text="Mot de passe: ") # mot de passe
        password_text.grid(row=3, column=1, pady=(5, 0), sticky=tk.E)
    
        self.var_password = StringVar()
        self.input_title = Entry(self.master, textvariable=self.var_password, width=30)
        self.input_title.grid(row=3, column=2, pady=(5, 0), sticky=tk.E)
        
        permission_text = Label(self.master, text="Permission: ") # permission
        permission_text.grid(row=4, column=1, pady=(5, 0), sticky=tk.E)
        
        self.var_permission = StringVar()
        self.input_permission = Entry(self.master, textvariable=self.var_permission, width=30)
        self.input_permission.grid(row=4, pady=(5, 0),column=2, sticky=tk.E)
        
        
        btn_1 = Button(self.master, text="Enregistrer", command=self.btn_enregistrer)        
        btn_1.grid(row=6, column=2)
                
      
        self.master.mainloop()
        
    def btn_enregistrer(self):
        #if self.controleur:
            #message d'erreur par controleur ou par vue?
            #reponse = self.controleur.enregistrer_usager()
            pass
        