from traceback import print_exc
import tkinter as tk
from vue import Vue
from vue_accueil import Vue_accueil

class Module(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Gestion')
        self.show_frame(None, Vue)

    def show_frame(self, instance_vue_courante, class_vue):
        if instance_vue_courante is not None:
            for widget in instance_vue_courante.winfo_children():
                widget.destroy()
            instance_vue_courante.destroy()
        self.frame = class_vue(self)
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