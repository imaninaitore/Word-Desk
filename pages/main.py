import customtkinter as ctk
import sqlite3

from pages.signin import SignInPage
from pages.login import LoginPage
from pages.instructions import InstructionsPage
from pages.home import HomePage
from pages.quiz import QuizPage
from pages.learning import LearningPage

# DATABASE SETUP

# Connect to the WordDesk database
connection = sqlite3.connect("WordDesk.db")

# Create a cursor
cursor = connection.cursor()

# Create the quiz scores table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS quiz_scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        score INTEGER NOT NULL,
        total_questions INTEGER NOT NULL,
        played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

# Save the table
connection.commit()

# Close the database connection
connection.close()

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


# Store the currently logged-in user
current_user = None

# Change which page is displayed
def show_page(page_name):

    # Get the selected page
    page = pages[page_name]

    # Bring the selected page to the front
    page.tkraise()

    # Update the username whenever HomePage is opened
    if page_name == "home":
        page.update_user()

    # Print the current page for testing
    print("Current page:", page_name)

# Get the currently logged-in user
def get_current_user():
    return current_user

# Set the currently logged-in user
def set_current_user(username):
    global current_user
    current_user = username
    print("Logged in user:", current_user)


pages["signin"] = SignInPage(
    container,
    show_page
)

pages["login"] = LoginPage(
    container,
    show_page,
    set_current_user
)

pages["instructions"] = InstructionsPage(
    container,
    show_page
)

pages["home"] = HomePage(
    container,
    show_page,
    get_current_user,
    set_current_user
)

pages["quiz"] = QuizPage(
    container,
    show_page,
    get_current_user,
    set_current_user
)

pages["learning"] = LearningPage(
    container,
    show_page
)


#positioning
for page in pages.values():

    page.place(
        x=0,
        y=0,
        relwidth=1,
        relheight=1
    )

#starting page
show_page("signin")

#run 
app.mainloop()