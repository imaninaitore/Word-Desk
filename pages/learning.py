# Import CustomTkinter for the interface
import customtkinter as ctk


# LEARNING PAGE

# Create the LearningPage that will live inside the main application
class LearningPage(ctk.CTkFrame):

    # Create the learning page
    def __init__(self, parent, show_page):

        # Initialize the parent frame
        super().__init__(parent)

        # Store the page manager function
        self.show_page = show_page

        # Create the learning page interface
        self.create_learning_page()


    # LEARNING PAGE INTERFACE

    # Create all the widgets for the learning page
    def create_learning_page(self):

        # Create the main title
        title = ctk.CTkLabel(
            self,
            text="WORD DESK",
            font=("Arial", 32, "bold")
        )

        # Position the title
        title.pack(
            pady=(40, 5)
        )


        # Create the subtitle
        subtitle = ctk.CTkLabel(
            self,
            text="Learning Space",
            font=("Arial", 22, "bold")
        )

        # Position the subtitle
        subtitle.pack(
            pady=5
        )


        # Create the description
        description = ctk.CTkLabel(
            self,
            text="Learn new words and improve your vocabulary.",
            font=("Arial", 14)
        )

        # Position the description
        description.pack(
            pady=(5, 30)
        )


        # Create the learning section
        learning_frame = ctk.CTkFrame(
            self,
            corner_radius=15
        )

        # Position the learning section
        learning_frame.pack(
            padx=40,
            pady=10,
            fill="x"
        )


        # Create the learning title
        learning_title = ctk.CTkLabel(
            learning_frame,
            text="Start Learning",
            font=("Arial", 20, "bold")
        )

        # Position the learning title
        learning_title.pack(
            pady=(25, 10)
        )


        # Create the learning description
        learning_text = ctk.CTkLabel(
            learning_frame,
            text="Search for words and discover their meanings.",
            font=("Arial", 14)
        )

        # Position the learning description
        learning_text.pack(
            pady=(5, 20)
        )


        # Create the dictionary button
        dictionary_button = ctk.CTkButton(
            learning_frame,
            text="Go to Dictionary",
            width=220,
            height=45,
            command=lambda: self.show_page("home")
        )

        # Position the dictionary button
        dictionary_button.pack(
            pady=10
        )


        # Create the quiz button
        quiz_button = ctk.CTkButton(
            learning_frame,
            text="Take a Quiz",
            width=220,
            height=45,
            command=lambda: self.show_page("quiz")
        )

        # Position the quiz button
        quiz_button.pack(
            pady=10
        )


        # Create the Home button
        home_button = ctk.CTkButton(
            self,
            text="← Home",
            width=150,
            height=40,
            command=lambda: self.show_page("home")
        )

        # Position the Home button
        home_button.pack(
            pady=30
        )