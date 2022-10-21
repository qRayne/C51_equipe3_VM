from tkinter import *
from tkinter.ttk import *
from turtle import title
from unicodedata import name


class Vue_projet():
    def __init__(self):
        super().__init__()
        self.title = "Project page"
        self.width = 1280
        self.height = 720
        self.master = None
        self.controleur = None
        self.remplir_vue()

    def set_controleur(self, controleur):
        self.controleur = controleur

    def remplir_vue(self):
        self.master = Tk()
        title_name = Label(self.master, text="Projet")
        title_name.grid(row=0, column=5)
        
        input = Entry(self.master)
        input.grid(row=1, column=2)
        
        btn_1 = Button(self.master, text="button 1")
        btn_1.grid(row=2, column=2)
        btn_2 = Button(self.master, text="button 2")
        btn_2.grid(row=3, column=2)
        
        self.master.mainloop()
