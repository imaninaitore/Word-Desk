import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.title("WordDesk")
window.geometry("700x500")

#create the notebook
notebook = ttk.Notebook(window)
notebook.pack( fill="both",expand=True)

#create the pages
signin_page=tk.Frame(notebook)
login_page=tk.Frame(notebook)
instructions_page = tk.Frame(notebook)
home_page = tk.Frame(notebook)
quiz_page = tk.Frame(notebook)
learning_page = tk.Frame(notebook)
