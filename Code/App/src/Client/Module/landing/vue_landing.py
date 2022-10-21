from tkinter import *
from tkinter.ttk import *

class Vue_landing():
    def __init__(self):
        super().__init__()
        self.title = "Landing page"
        self.width = 1280
        self.height = 720
        self.master = None
        self.controleur = None
        self.remplir_vue()

    def set_controleur(self, controleur):
        self.controleur = controleur

    def remplir_vue(self):
        self.master = Tk()
        label = Label(self.master, text="test")
        label.pack()
        
        
        