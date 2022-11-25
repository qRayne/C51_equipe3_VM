from traceback import print_exc
import tkinter as tk
from vue import Vue
from sys import path

path.append('./Module')
from vue_accueil import Vue_accueil

path.append('./Module')
from vue_enregistrer import Vue_enregistrer 


class Module(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.x = 500
        self.y = 800
        window = tk.Frame(self)
        window.pack()
        window.grid_rowconfigure(0, minsize = self.x)
        window.grid_columnconfigure(0, minsize = self.y)
        self.title('Gestion')
        
        self['bg'] = '#FA8072'
     
        self.frames = {}
        for F in (Vue, Vue_accueil, Vue_enregistrer):
            frame = F(window,self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        self.show_frame(Vue)

    def show_frame(self,page):
        frame = self.frames[page]
        frame.tkraise()
    
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