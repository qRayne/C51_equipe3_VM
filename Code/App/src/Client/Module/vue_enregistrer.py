from tkinter import *
from tkinter.ttk import *
import os

class Vue_enregistre():
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

    def remplir_vue(self):
        self.master = Tk()
        
        label = Label(self.master, text="test")
        
        last_name = Label(self.master, text="last name")
        last_name.grid(row=0, column=0)
        
        first_name = Label(self.master, text="first name")
        first_name.grid(row=0, column=1)
        
        title_name = Label(self.master, text="title name")
        title_name.grid(row=0, column=5)
        
        btn_1 = Button(self.master, text="button 1")        
        btn_1.grid(row=2, column=2)
        
       
                
        self.master.mainloop()
        
 