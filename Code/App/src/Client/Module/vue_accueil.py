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
        
        btn_1 = Button(self.master, text="Projet", command=self.open_projet)        
        btn_1.grid(row=2, column=2)
        
        btn_2 = Button(self.master, text="button 2", command="")
        btn_2.grid(row=3, column=2)
        
        btn_3 = Button(self.master, text="button 3", command="")
        btn_3.grid(row=4, column=2)
        
        btn_4 = Button(self.master, text="button 4", command="")
        btn_4.grid(row=5, column=2)
                
        self.master.mainloop()
        
    def open_projet(self):
        topProjet = Toplevel()
        topProjet.title("projet")
        
        

        
    
    
