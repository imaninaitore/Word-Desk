import tkinter as tk
from tkinter import messagebox

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

    # Temporary login details
    elif username == "admin" and password == "1234":
        messagebox.showinfo(
            "Success",
            "Login successful!"
        )

    else:
        messagebox.showerror(
            "Login Failed",
            "Incorrect username or password."
        )


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