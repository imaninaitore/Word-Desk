import sqlite3
import tkinter as tk
from tkinter import messagebox

#DATABASE CONNECTION
connection = sqlite3.connect("WordDesk.db")

# CREATE CURSOR
cursor = connection.cursor()

# CREATE USERS TABLE
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT UNIQUE NOT NULL
    )
""")

# SAVE CHANGES
connection.commit()

# MAIN WINDOW
window = tk.Tk()
window.title("Word Desk - Create Account")
window.geometry("500x500")


# ACCOUNT CREATION FRAME

account_frame = tk.Frame(window)
account_frame.pack()


# TITLE
title = tk.Label(account_frame,text="WORD DESK",font=("Arial", 24))
title.grid(row=0, column=0, columnspan=2, pady=20)


subtitle = tk.Label(account_frame,text="Create Your Account",font=("Arial", 16))
subtitle.grid(row=1, column=0, columnspan=2, pady=10)


# USERNAME
username_label = tk.Label(account_frame,text="Username:")
username_label.grid(row=2, column=0, padx=10, pady=10)

username_entry = tk.Entry(account_frame)
username_entry.grid(row=2, column=1, padx=10, pady=10)


# PASSWORD
password_label = tk.Label(account_frame,text="Password:")
password_label.grid(row=3, column=0, padx=10, pady=10)

password_entry = tk.Entry(account_frame,show="*")
password_entry.grid(row=3, column=1, padx=10, pady=10)


# CONFIRM PASSWORD
confirm_label = tk.Label(account_frame,text="Confirm Password:")
confirm_label.grid(row=4, column=0, padx=10, pady=10)

confirm_entry = tk.Entry(account_frame,show="*")
confirm_entry.grid(row=4, column=1, padx=10, pady=10)


# CREATE ACCOUNT FUNCTION
def create_account():

    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_entry.get()

    # Check if fields are empty
    if username == "" or password == "" or confirm_password == "":
        messagebox.showerror(
            "Error",
            "Please fill in all fields."
        )

    # Check if passwords match
    elif password != confirm_password:
        messagebox.showerror(
            "Error",
            "Passwords do not match."
        )

    else:
        messagebox.showinfo(
            "Success",
            "Account created successfully!"
        )


# CREATE ACCOUNT BUTTON

create_button = tk.Button(account_frame,text="CREATE ACCOUNT",command=create_account)
create_button.grid(row=5, column=0, columnspan=2, pady=20)

# LOGIN BUTTON
login_label = tk.Label(account_frame,text="Already have an account?")
login_label.grid(row=6,column=0,columnspan=2)

login_button = tk.Button(account_frame,text="LOGIN")
login_button.grid( row=7, column=0, columnspan=2, pady=10)

# KEEP WINDOW RUNNING
window.mainloop()