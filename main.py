import customtkinter as ctk

from pages.signin import SignInPage
from pages.login import LoginPage
from pages.instructions import InstructionsPage
from pages.home import HomePage
from pages.quiz import QuizPage
from pages.learning import LearningPage

# ==========================================
# MAIN WINDOW
# ==========================================

app = ctk.CTk()

app.title("WordDesk")
app.geometry("900x650")
app.resizable(False, False)


# CONTAINER

container = ctk.CTkFrame(
    app,
    fg_color="transparent"
)

container.pack(
    fill="both",
    expand=True
)


# PAGE MANAGER

pages = {}


def show_page(page_name):

    page = pages[page_name]

    page.tkraise()


# CREATE PAGES


pages["home"] = HomePage(
    container,
    show_page
)

pages["quiz"] = QuizPage(
    container,
    show_page
)

pages["dictionary"] = DictionaryPage(
    container,
    show_page
)

pages["favorites"] = FavoritesPage(
    container,
    show_page
)


# POSITION ALL PAGES

for page in pages.values():

    page.place(
        x=0,
        y=0,
        relwidth=1,
        relheight=1
    )
 
# START PAGE

show_page("home")

# RUN
app.mainloop()