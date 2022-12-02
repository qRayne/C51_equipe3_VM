from sys import path

path.append("..")

from traceback import print_exc
import tkinter as tk
from vue import Vue
from vue_accueil import Vue_accueil

from Utils import utils

VUES = [Vue, Vue_accueil]

class Module(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Gestion')
        self.show_frame(None, utils.VUE)

    def show_frame(self, instance_vue_courante, index_class_vue):
        if instance_vue_courante is not None:
            for widget in instance_vue_courante.winfo_children():
                widget.destroy()
            instance_vue_courante.destroy()
        # if index_class_vue == utils.VUE:
        #     self.frame = Vue(self)
        # elif index_class_vue == utils.VUE_ACCUEIL:
        #     self.frame = Vue_accueil(self)
        self.frame = VUES[index_class_vue](self)
        
        self.frame.grid(row = 0, column = 0, sticky = "nsew")
        self.frame.remplir_vue()
    
def main():
    try:
        module = Module()   
        module.mainloop()
        
    except:
        print_exc()
        return 1
    return 0

if __name__ == '__main__':
    quit(main())