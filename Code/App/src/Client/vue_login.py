from distutils.command.config import config
from math import perm
from sys import path
from turtle import width
from urllib import response

path.append("..")

import tkinter as tk
from tkinter import ttk
from Utils import utils

class VueLogin(ttk.Frame):
    def __init__(self, parent, controleur_client):
        super().__init__(parent)
        self.parent = parent
        self.controleur_client = controleur_client

    def remplir_vue(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)
        self.label_nom = ttk.Label(self, text='Gestion', font=("Times New Roman", 40), background='#2596be')
        # self.label_nom.grid(row=0, column=1)
        self.label_nom.place(x=280, y=120)
        
        self.parent.geometry('720x480')
        self.parent.configure(background="#2596be")
        
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TButton', font=('Times New Roman', 10), background='#232323', foreground='white')
        style.configure('TFrame', background='#2596be')
        style.configure('TLabel', background='#2596be')
        style.map('TButton', background=[('active', 'Blue')])
        style.map('TLabel', background=[('active', 'Blue')])
        
        self.var_pseudo = tk.StringVar()
        self.input_nom = ttk.Entry(self, textvariable=self.var_pseudo, width=30)
        self.input_nom.insert(0, 'Pseudo')
        # self.input_nom.grid(row=2, column=1)
        self.input_nom.place(x=280, y=190)
        self.input_nom.bind("<Button-1>", lambda e: self.placeholder(self.input_nom))
        
        self.var_mdp = tk.StringVar()
        self.input_mdp = ttk.Entry(self, textvariable=self.var_mdp, show='*', width=30)
        self.input_mdp.insert(0, 'Mot de passe')
        # self.input_mdp.grid(row=3, column=1)
        self.input_mdp.place(x=280, y=220)
        self.input_mdp.bind("<Button-1>", lambda e: self.placeholder(self.input_mdp))
        
        self.bouton_connexion = ttk.Button(self, text='Connexion', command=self.clic_bouton_connexion)
        self.parent.bind('<Return>', self.press_enter)

        self.bouton_annuler = ttk.Button(self, text='Annuler', command=self.clic_btn_annuler)
        # self.bouton_connexion.grid(row=4, column=1)
        self.bouton_connexion.place(x=388, y=250)

        # self.bouton_annuler.grid(row=5, column=1)
        self.bouton_annuler.place(x=388, y=280)

        self.label_message = ttk.Label(self, text='',foreground='red')
        # self.label_message.grid(row=6, column=1)
        self.label_message.place(x=280, y=310)

    def placeholder(self, input):
        input.delete(0, 'end')

    def press_enter(self, e):
        self.clic_bouton_connexion()

    def clic_bouton_connexion(self):
        if self.controleur_client:
            reponse = self.controleur_client.identifier_usager(self.var_pseudo.get(), self.var_mdp.get())
            if len(reponse):
                self.afficher_succes(reponse)
                self.controleur_client.credentials["user"] = self.var_pseudo.get()
                user = self.controleur_client.get_utilisateur(self.controleur_client.credentials["user"])
                self.controleur_client.credentials["locateur"] = user[0][2]
                self.controleur_client.credentials["permissions"] = reponse[0][3]
               
                self.parent.show_frame(self, utils.VUE_ACCUEIL)
            else:
                self.afficher_erreur(f'Nom ou mot de passe incorrects')
                return False
         
    def clic_btn_annuler(self):
        self.var_pseudo.set('')
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
        self.input_mdp['foreground'] = 'black'

    def cacher_message(self):
        self.label_message['text'] = ''

