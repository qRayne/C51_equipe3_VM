import tkinter as tk
from tkinter import ttk
from controleur_client import Controleur_Client
from vue_accueil import Vue_accueil

class Vue(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.ctrl_client = Controleur_Client()
        
    def set_controleur(self, controleur):
        self.ctrl_client = controleur

    def remplir_vue(self):
        print("remplir vue")
        self.label_nom = ttk.Label(self, text='Gestion', font=("Times New Roman", 30), background='#FA8072')
        self.label_nom.grid(row=0, column=0)

        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TButton', font=('Times New Roman', 10),background='#232323', foreground='white')
        style.map('TButton',background=[('active', 'Blue')])
        style.map('TLabel',background=[('active', 'Blue')])
        
        # self.label_nom = ttk.Label(self, text='Pseudo :', background='#FA8072')
        # self.label_nom.grid(row=1, column=0)

        self.var_pseudo = tk.StringVar()
        self.input_nom = ttk.Entry(self, textvariable=self.var_pseudo, width=30)
        self.input_nom.insert(0, 'Pseudo')
        self.input_nom.grid(row=2, column=0)

        # self.label_mdp = ttk.Label(self, text='Mot de passe :', background='#FA8072')
        # self.label_mdp.grid(row=0, column=0)

        self.var_mdp = tk.StringVar()
        self.input_mdp = ttk.Entry(self, textvariable=self.var_mdp, show='*', width=30)
        self.input_mdp.insert(0, 'Mot de passe')
        self.input_mdp.grid(row=3, column=0)

        self.input_mdp.bind("<Button-1>", lambda e: self.click(self.input_mdp))
        # self.input_mdp.bind("<Leave>", lambda e: self.leave(self.input_mdp))
        
        self.input_nom.bind("<Button-1>", lambda e: self.click(self.input_nom))
        # self.input_nom.bind("<Leave>", lambda e: self.leave(self.input_nom))
        
        self.bouton_connexion = ttk.Button(self, text='Connexion', command=self.clic_bouton_connexion)
        self.bouton_connexion.bind('<Return>', lambda e: self.bouton_connexion.invoke())
        self.bouton_connexion.grid(row=4, column=0)

        self.bouton_annuler = ttk.Button(self, text='Annuler', command=self.btn_annuler)
        self.bouton_annuler.bind('<Return>', lambda e: self.bouton_annuler.invoke())
        self.bouton_annuler.grid(row=5, column=0)

        self.label_message = ttk.Label(self, text='',background='#FA8072',foreground='red')
        self.label_message.grid(row=6, column=0)


    def click(self, input):
        input.delete(0, 'end')
            
    def leave(self, input):
        input.delete(0, 'end')
        if input == self.input_mdp:
            input.insert(0, 'Mot de passe')
        elif input == self.input_nom:
            input.insert(0, 'Pseudo')
            
    def clic_bouton_connexion(self):
        if self.ctrl_client:
            #message d'erreur par controleur ou par vue?
            reponse = self.ctrl_client.identifier_usager(self.var_pseudo.get(), self.var_mdp.get())
            if len(reponse):
                self.afficher_succes(reponse)
                self.parent.show_frame(self, Vue_accueil)
            else:
                self.afficher_erreur(f'Nom ou mot de passe incorrects')
                return False
         
    def btn_annuler(self):
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
        #self.var_nom.set(self.input_nom)
        self.input_mdp['foreground'] = 'black'
        #self.var_mdp.set(self.input_mdp)

    def cacher_message(self):
        self.label_message['text'] = ''
