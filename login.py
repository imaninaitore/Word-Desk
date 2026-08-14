import sqlite3
import tkinter as tk
from tkinter import messagebox
import bcrypt

#DATABASE CONNECTION
connection = sqlite3.connect("WordDesk.db")

# CREATE CURSOR
cursor = connection.cursor()

# MAIN WINDOW
window = tk.Tk()
window.title("Word Desk - Login")
window.geometry("500x500")

# LOGIN FRAME
login_frame = tk.Frame(window)
login_frame.pack()

# TITLE
title = tk.Label(login_frame,text="WORD DESK",font=("Arial", 24))
title.grid(row=0, column=0, columnspan=2, pady=20)


subtitle = tk.Label(login_frame,text="Login to Your Account",font=("Arial", 16))
subtitle.grid(row=1, column=0, columnspan=2, pady=10)

# USERNAME
username_label = tk.Label( login_frame, text="Username:")
username_label.grid( row=2,column=0,padx=10,pady=10)

username_entry = tk.Entry(login_frame)
username_entry.grid( row=2, column=1, padx=10, pady=10)

# PASSWORD
password_label = tk.Label(login_frame,text="Password:")
password_label.grid(row=3,column=0,padx=10,pady=10)

password_entry = tk.Entry(login_frame,show="*")
password_entry.grid( row=3, column=1, padx=10, pady=10)


# LOGIN FUNCTION
def login():

    username = username_entry.get()
    password = password_entry.get()

    # Check if fields are empty
    if username == "" or password == "":
        messagebox.showerror(
            "Error",
            "Please enter your username and password."
        )
        return
    #searching the database
    cursor.execute(
    """
    SELECT * FROM users
    WHERE username = ? AND password = ?
    """,(username, password)
 )
# Search for the user
    cursor.execute(
    "SELECT * FROM users WHERE username = ? AND password = ?",
    (username, password)
     )

# Fetch the matching user
    user = cursor.fetchone()

# Check if a user was found
    if user:
      messagebox.showinfo("Success", "Login successful!")
    else:
      messagebox.showerror("Error", "Incorrect username or password.")


# LOGIN BUTTON
login_button = tk.Button( login_frame, text="LOGIN", command=login)
login_button.grid(row=4,column=0,columnspan=2,pady=20)

# CREATE ACCOUNT
create_label = tk.Label(login_frame,text="Don't have an account?")
create_label.grid(row=5,column=0,columnspan=2)

create_button = tk.Button(login_frame,text="CREATE ACCOUNT")

create_button.grid(row=6,column=0,columnspan=2, pady=10)

# KEEP WINDOW RUNNING
window.mainloop()