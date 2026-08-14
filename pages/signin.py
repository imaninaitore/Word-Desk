import customtkinter as ctk
import sqlite3
from tkinter import messagebox


# Create the sign-in/account creation page
class SignInPage(ctk.CTkFrame):

    # Set up the page and receive the page manager
    def __init__(self, parent, show_page):

        # Initialize the page inside the main application
        super().__init__(parent)

        # Save the page manager so buttons can change pages
        self.show_page = show_page

        # Connect to the WordDesk database
        self.connection = sqlite3.connect("WordDesk.db")

        # Create a cursor for database commands
        self.cursor = self.connection.cursor()

        # Create the users table if it does not already exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        """)

        # Save the database changes
        self.connection.commit()

        # Create the main account creation frame
        account_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        # Position the account frame in the center
        account_frame.pack(
            expand=True
        )

        # Create the main WordDesk title
        title = ctk.CTkLabel(
            account_frame,
            text="WORD DESK",
            font=("Arial", 32, "bold")
        )

        # Position the title
        title.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(10, 5)
        )

        # Create the page subtitle
        subtitle = ctk.CTkLabel(
            account_frame,
            text="Create Your Account",
            font=("Arial", 20, "bold")
        )

        # Position the subtitle
        subtitle.grid(
            row=1,
            column=0,
            columnspan=2,
            pady=(0, 25)
        )

        # Create the username label
        username_label = ctk.CTkLabel(
            account_frame,
            text="Username:",
            font=("Arial", 14)
        )

        # Position the username label
        username_label.grid(
            row=2,
            column=0,
            padx=(10, 15),
            pady=10,
            sticky="e"
        )

        # Create the username entry
        self.username_entry = ctk.CTkEntry(
            account_frame,
            width=280,
            height=40,
            placeholder_text="Enter your username"
        )

        # Position the username entry
        self.username_entry.grid(
            row=2,
            column=1,
            padx=(0, 10),
            pady=10
        )

        # Create the password label
        password_label = ctk.CTkLabel(
            account_frame,
            text="Password:",
            font=("Arial", 14)
        )

        # Position the password label
        password_label.grid(
            row=3,
            column=0,
            padx=(10, 15),
            pady=10,
            sticky="e"
        )

        # Create the password entry
        self.password_entry = ctk.CTkEntry(
            account_frame,
            width=280,
            height=40,
            placeholder_text="Enter your password",
            show="*"
        )

        # Position the password entry
        self.password_entry.grid(
            row=3,
            column=1,
            padx=(0, 10),
            pady=10
        )

        # Create the password requirements label
        password_info = ctk.CTkLabel(
            account_frame,
            text="Password must be at least 6 characters.",
            font=("Arial", 11)
        )

        # Position the password requirements below the password entry
        password_info.grid(
            row=4,
            column=1,
            padx=(0, 10),
            pady=(0, 10),
            sticky="w"
        )

        # Create the confirm password label
        confirm_label = ctk.CTkLabel(
            account_frame,
            text="Confirm Password:",
            font=("Arial", 14)
        )

        # Position the confirm password label
        confirm_label.grid(
            row=5,
            column=0,
            padx=(10, 15),
            pady=10,
            sticky="e"
        )

        # Create the confirm password entry
        self.confirm_entry = ctk.CTkEntry(
            account_frame,
            width=280,
            height=40,
            placeholder_text="Confirm your password",
            show="*"
        )

        # Position the confirm password entry
        self.confirm_entry.grid(
            row=5,
            column=1,
            padx=(0, 10),
            pady=10
        )

        # Create the account button
        create_button = ctk.CTkButton(
            account_frame,
            text="CREATE ACCOUNT",
            width=220,
            height=40,
            command=self.create_account
        )

        # Position the create account button
        create_button.grid(
            row=6,
            column=0,
            columnspan=2,
            pady=(20, 10)
        )

        # Create the existing account label
        login_label = ctk.CTkLabel(
            account_frame,
            text="Already have an account?"
        )

        # Position the existing account label
        login_label.grid(
            row=7,
            column=0,
            columnspan=2,
            pady=(10, 5)
        )

        # Create the login button
        login_button = ctk.CTkButton(
            self,
            text="LOGIN",
            width=180,
            height=35,
            fg_color="transparent",
            border_width=1,
            command=lambda: self.show_page("login")
        )

        # Position the login button
        login_button.pack(pady=(10) )

    # Create a new user account
    def create_account(self):

        # Get the username entered by the user
        username = self.username_entry.get().strip()

        # Get the password entered by the user
        password = self.password_entry.get()

        # Get the confirmation password
        confirm_password = self.confirm_entry.get()

        # Check if any required field is empty
        if username == "" or password == "" or confirm_password == "":
            messagebox.showerror(
                "Error",
                "Please fill in all fields."
            )
            return

        # Check if the password has at least six characters
        if len(password) < 6:
            messagebox.showerror(
                "Invalid Password",
                "Password must be at least 6 characters long."
            )
            return

        # Check if both passwords match
        if password != confirm_password:
            messagebox.showerror(
                "Error",
                "Passwords do not match."
            )
            return

        # Try to save the new account
        try:

            # Insert the new username and password into the database
            self.cursor.execute(
                """
                INSERT INTO users (username, password)
                VALUES (?, ?)
                """,
                (username, password)
            )

            # Save the new account
            self.connection.commit()

            # Tell the user the account was created
            messagebox.showinfo(
                "Success",
                "Account created successfully!"
            )

            # Clear the input fields
            self.username_entry.delete(0, "end")
            self.password_entry.delete(0, "end")
            self.confirm_entry.delete(0, "end")

            # Take the user to the login page
            self.show_page("login")

        # Handle a username that already exists
        except sqlite3.IntegrityError:

            # Show an error message
            messagebox.showerror(
                "Error",
                "That username already exists."
            )