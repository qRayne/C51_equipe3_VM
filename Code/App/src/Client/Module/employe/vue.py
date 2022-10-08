from ast import Pass
import tkinter as tk
from tkinter import ttk

class Vue(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controleur = None
        self.remplir_vue()

    def set_controleur(self, controleur):
        self.controleur = controleur

    def remplir_vue(self):
        Pass