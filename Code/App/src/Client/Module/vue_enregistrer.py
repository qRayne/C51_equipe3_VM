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
        label = Label(self.master, text="       ")
        label.grid(row=r, column=c)
    
      
        
    def remplir_vue(self):
        self.master = Tk()
        
        self.label_vide(0, 0)
        self.label_vide(1, 0)
        self.label_vide(2, 0)
        self.label_vide(3, 0)

        last_name_text = Label(self.master, text="last name")
        last_name_text.grid(row=0, column=1)
        
          
        self.var_lastname = StringVar()
        self.input_lastname = Entry(self.master, textvariable=self.var_lastname, width=30)
        self.input_lastname.grid(row=0, column=2, sticky=tk.E)
        
        first_name = Label(self.master, text="first name")
        first_name.grid(row=1, column=1)
        
        self.var_firstname = StringVar()
        self.input_firstname = Entry(self.master, textvariable=self.var_firstname, width=30)
        self.input_firstname.grid(row=1, column=2, sticky=tk.E)
        
        title_name = Label(self.master, text="title name")
        title_name.grid(row=2, column=1)
        
        
        self.var_title = StringVar()
        self.input_title = Entry(self.master, textvariable=self.var_title, width=30)
        self.input_title.grid(row=2, column=2, sticky=E)
        
        btn_1 = Button(self.master, text="Enregistrer",  command=self.add_user)        
        btn_1.grid(row=4, column=4)
                
      
        self.master.mainloop()
        
    def add_user(self):
        # self.var_nom.get(), self.var_mdp.get()
        pass
        