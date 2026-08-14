# Import SQLite for the database
import sqlite3

# Import CustomTkinter for the interface
import customtkinter as ctk

# Import messagebox for error and success messages
from tkinter import messagebox


# DATABASE CONNECTION

# Connect to the WordDesk database
connection = sqlite3.connect("WordDesk.db")

# Create a cursor for database commands
cursor = connection.cursor()


# LOGIN PAGE

# Create the LoginPage that will live inside the main application
class LoginPage(ctk.CTkFrame):

    # Set up the login page
    def __init__(self, parent, show_page):

        # Initialize the parent frame
        super().__init__(parent)

        # Save the page manager
        self.show_page = show_page

        # LOGIN FRAME

        # Create the frame that holds the login widgets
        login_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        # Position the login frame
        login_frame.pack(
            expand=True
        )


        # TITLE

        # Create the WordDesk title
        title = ctk.CTkLabel(
            login_frame,
            text="WORD DESK",
            font=("Arial", 24)
        )

        # Position the title
        title.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=20
        )


        # Create the subtitle
        subtitle = ctk.CTkLabel(
            login_frame,
            text="Login to Your Account",
            font=("Arial", 16)
        )

        # Position the subtitle
        subtitle.grid(
            row=1,
            column=0,
            columnspan=2,
            pady=10
        )


        # USERNAME

        # Create the username label
        username_label = ctk.CTkLabel(
            login_frame,
            text="Username:",
            font=("Arial", 14)
        )

        # Position the username label
        username_label.grid(
            row=2,
            column=0,
            padx=10,
            pady=10
        )


        # Create the username entry
        self.username_entry = ctk.CTkEntry(
            login_frame,
            width=280,
            height=40,
            placeholder_text="Enter your username"
        )

        # Position the username entry
        self.username_entry.grid(
            row=2,
            column=1,
            padx=10,
            pady=10
        )


        # PASSWORD

        # Create the password label
        password_label = ctk.CTkLabel(
            login_frame,
            text="Password:",
            font=("Arial", 14)
        )

        # Position the password label
        password_label.grid(
            row=3,
            column=0,
            padx=10,
            pady=10
        )


        # Create the password entry
        self.password_entry = ctk.CTkEntry(
            login_frame,
            width=280,
            height=40,
            placeholder_text="Enter your password",
            show="*"
        )

        # Position the password entry
        self.password_entry.grid(
            row=3,
            column=1,
            padx=10,
            pady=10
        )


        # LOGIN BUTTON

        # Create the login button
        login_button = ctk.CTkButton(
            login_frame,
            text="LOGIN",
            width=220,
            height=40,
            command=self.login
        )

        # Position the login button
        login_button.grid(
            row=4,
            column=0,
            columnspan=2,
            pady=20
        )


        # CREATE ACCOUNT

        # Create the account message
        create_label = ctk.CTkLabel(
            login_frame,
            text="Don't have an account?"
        )

        # Position the account message
        create_label.grid(
            row=5,
            column=0,
            columnspan=2
        )


        # Create the create-account button
        create_button = ctk.CTkButton(
            login_frame,
            text="CREATE ACCOUNT",
            width=200,
            height=35,
            fg_color="transparent",
            border_width=1,
            command=lambda: self.show_page("signin")
        )

        # Position the create-account button
        create_button.grid(
            row=6,
            column=0,
            columnspan=2,
            pady=10
        )


    # LOGIN FUNCTION

    # Check the user's login details
    def login(self):

        # Get the username and password from the entry fields
        username = self.username_entry.get().strip()
        password = self.password_entry.get()

        # Check if fields are empty
        if username == "" or password == "":

            messagebox.showerror(
                "Error",
                "Please enter your username and password."
            )

            return


        # Search for the username in the database
        cursor.execute(
            """
            SELECT * FROM users
            WHERE username = ?
            """,
            (username,)
        )


        # Get the user from the database
        user = cursor.fetchone()


        # Check if username exists
        if user is None:

            messagebox.showerror(
                "Error",
                "Incorrect username or password."
            )

            return


        # Get the password stored in the database
        stored_password = user[2]


        # Compare the entered password with the stored password
        if password == stored_password:

            # Show successful login message
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

            # Show error for incorrect password
            messagebox.showerror(
                "Error",
                "Incorrect username or password."
            )