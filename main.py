import customtkinter as ctk

from pages.signin import SignInPage
from pages.login import LoginPage
from pages.instructions import InstructionsPage
from pages.home import HomePage
from pages.quiz import QuizPage
from pages.learning import LearningPage

# MAIN WINDOW
app = ctk.CTk()

app.title("WordDesk")
app.geometry("900x650")
app.resizable(False, False)

# CONTAINER- where all pages will be
container = ctk.CTkFrame(
    app,
    fg_color="transparent"
)

container.pack(
    fill="both",
    expand=True
)

#page manager
pages = {}


def show_page(page_name):

    page = pages[page_name]

    page.tkraise()