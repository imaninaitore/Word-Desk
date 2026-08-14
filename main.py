import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.title("WordDesk")
window.geometry("700x500")

#create the notebook
notebook = ttk.Notebook(window)
notebook.pack( fill="both",expand=True)


