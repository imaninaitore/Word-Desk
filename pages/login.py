import sqlite3
import customtkinter as ctk
from tkinter import messagebox
import bcrypt


# DATABASE CONNECTION
connection = sqlite3.connect("WordDesk.db")

# CREATE CURSOR
cursor = connection.cursor()


# LOGIN PAGE
class LoginPage(ctk.CTkFrame):

    # Set up the login page
    def __init__(self, parent, show_page):

        super().__init__(parent)

        # Save the page manager
        self.show_page = show_page

        # LOGIN FRAME
        login_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        login_frame.pack(
            expand=True
        )

        # TITLE
        title = ctk.CTkLabel(
            login_frame,
            text="WORD DESK",
            font=("Arial", 24)
        )

        title.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=20
        )


        subtitle = ctk.CTkLabel(
            login_frame,
            text="Login to Your Account",
            font=("Arial", 16)
        )

        subtitle.grid(
            row=1,
            column=0,
            columnspan=2,
            pady=10
        )


        # USERNAME
        username_label = ctk.CTkLabel(
            login_frame,
            text="Username:",
            font=("Arial", 14)
        )

        username_label.grid(
            row=2,
            column=0,
            padx=10,
            pady=10
        )


        self.username_entry = ctk.CTkEntry(
            login_frame,
            width=280,
            height=40,
            placeholder_text="Enter your username"
        )

        self.username_entry.grid(
            row=2,
            column=1,
            padx=10,
            pady=10
        )


        # PASSWORD
        password_label = ctk.CTkLabel(
            login_frame,
            text="Password:",
            font=("Arial", 14)
        )

        password_label.grid(
            row=3,
            column=0,
            padx=10,
            pady=10
        )


        self.password_entry = ctk.CTkEntry(
            login_frame,
            width=280,
            height=40,
            placeholder_text="Enter your password",
            show="*"
        )

        self.password_entry.grid(
            row=3,
            column=1,
            padx=10,
            pady=10
        )


        # LOGIN BUTTON
        login_button = ctk.CTkButton(
            login_frame,
            text="LOGIN",
            width=220,
            height=40,
            command=self.login
        )

        login_button.grid(
            row=4,
            column=0,
            columnspan=2,
            pady=20
        )


        # CREATE ACCOUNT
        create_label = ctk.CTkLabel(
            login_frame,
            text="Don't have an account?"
        )

        create_label.grid(
            row=5,
            column=0,
            columnspan=2
        )


        create_button = ctk.CTkButton(
            login_frame,
            text="CREATE ACCOUNT",
            width=200,
            height=35,
            fg_color="transparent",
            border_width=1,
            command=lambda: self.show_page("signin")
        )

        create_button.grid(
            row=6,
            column=0,
            columnspan=2,
            pady=10
        )


    # LOGIN FUNCTION
    def login(self):

        username = self.username_entry.get().strip()
        password = self.password_entry.get()

        # Check if fields are empty
        if username == "" or password == "":

            messagebox.showerror(
                "Error",
                "Please enter your username and password."
            )

            return

        # Search for the username
        cursor.execute(
            """
            SELECT * FROM users
            WHERE username = ?
            """,
            (username,)
        )

        # Get the user
        user = cursor.fetchone()

        # Check if username exists
        if user is None:

            messagebox.showerror(
                "Error",
                "Incorrect username or password."
            )

            return

        # Get the hashed password
        stored_password = user[2]

        # Check the password
        try:

            password_correct = bcrypt.checkpw(
                password.encode("utf-8"),
                stored_password.encode("utf-8")
            )

        except ValueError:

            messagebox.showerror(
                "Error",
                "There is a problem with the stored password."
            )

            return

        # Check result
        if password_correct:

            messagebox.showinfo(
                "Success",
                "Login successful!"
            )

            # Clear the login fields
            self.username_entry.delete(0, "end")
            self.password_entry.delete(0, "end")

            # Move to the instructions page
            self.show_page("instructions")

        else:

            messagebox.showerror(
                "Error",
                "Incorrect username or password."
            )