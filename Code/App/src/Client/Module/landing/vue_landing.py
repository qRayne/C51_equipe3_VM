from ast import Pass
import tkinter as tk
from tkinter import ttk

class Vue_landing():
    def __init__(self):
        super().__init__()
        self.controleur = None
        self.remplir_vue()

    def set_controleur(self, controleur):
        self.controleur = controleur

    def remplir_vue(self):
        ttk.Frame()
        