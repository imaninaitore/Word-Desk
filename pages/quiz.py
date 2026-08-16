# Import CustomTkinter for the interface
import customtkinter as ctk

# Import SQLite for the WordDesk database
import sqlite3

# Import random for generating random questions
import random

# Import os for finding the database location
import os

# QUIZ PAGE

# Create the QuizPage that will live inside the main application
class QuizPage(ctk.CTkFrame):

    # Create the quiz page
    def __init__(self, parent, show_page):

        # Initialize the parent frame
        super().__init__(parent)

        # Store the page manager function
        self.show_page = show_page

        # Store the user's score
        self.score = 0

        # Store the current question number
        self.round_number = 0

        # Store the correct answer
        self.correct_answer = ""

        # Store the database location
        self.database_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "WordDesk.db"
        )

        # Create the welcome screen
        self.create_welcome_screen()

        # Create the quiz screen
        self.create_quiz_screen()


    # DATABASE

    # Get words from the WordDesk database
    def get_words(self):

        # Try to connect to the database
        try:

            # Connect to the correct WordDesk database
            connection = sqlite3.connect(self.database_path)

            # Create a cursor
            cursor = connection.cursor()

            # Get words and definitions
            cursor.execute("""
                SELECT word, definition
                FROM words
                WHERE word IS NOT NULL
                AND definition IS NOT NULL
            """)

            # Get all database results
            results = cursor.fetchall()

            # Close the database connection
            connection.close()

            # # Print database information for testing
            # print("Database:", self.database_path)
            # print("Words found:", len(results))
            # print("Data:", results)

            # Return the results
            return results

        # Handle database errors
        except sqlite3.Error as error:

            # Print the database error
            print("DATABASE ERROR:", error)

            # Display the error on the screen
            self.question_label.configure(
                text=f"Database error:\n\n{error}"
            )

            # Return an empty list
            return []


    # WELCOME SCREEN

    # Create the quiz welcome screen
    def create_welcome_screen(self):

        # Create the welcome frame
        self.welcome_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        # Place the welcome frame
        self.welcome_frame.place(
              x=0,
              y=0,
              relwidth=1,
              relheight=1
          )
        # Create the WordDesk title
        welcome_title = ctk.CTkLabel(
            self.welcome_frame,
            text="WORD DESK",
            font=("Arial", 38, "bold")
        )

        # Position the title
        welcome_title.pack(
            pady=(120, 5)
        )

        # Create the quiz title
        welcome_subtitle = ctk.CTkLabel(
            self.welcome_frame,
            text="Vocabulary Quiz",
            font=("Arial", 24, "bold")
        )

        # Position the quiz title
        welcome_subtitle.pack(
            pady=5
        )

        # Create the description
        welcome_description = ctk.CTkLabel(
            self.welcome_frame,
            text="Test your vocabulary and see how many words you know!",
            font=("Arial", 16),
            wraplength=500
        )

        # Position the description
        welcome_description.pack(
            pady=(15, 40)
        )

        # Create the Get Started button
        get_started_button = ctk.CTkButton(
            self.welcome_frame,
            text="Get Started",
            width=220,
            height=55,
            corner_radius=12,
            font=("Arial", 18, "bold"),
            command=self.start_quiz
        )

        # Position the Get Started button
        get_started_button.pack(
            pady=10
        )

        # Create a Home button
        home_button = ctk.CTkButton(
            self.welcome_frame,
            text="← Home",
            width=150,
            command=lambda: self.show_page("home")
        )

        # Position the Home button
        home_button.pack(
            pady=20
        )


    # QUIZ SCREEN

    # Create the actual quiz interface
    def create_quiz_screen(self):

        # Create the quiz frame
        self.quiz_frame = ctk.CTkFrame(
            self,
            corner_radius=20
        )

        # Create the top navigation frame
        top_frame = ctk.CTkFrame(
            self.quiz_frame,
            fg_color="transparent"
        )

        # Position the top frame
        top_frame.pack(
            fill="x",
            padx=20,
            pady=(15, 5)
        )

        # Create the Home button
        back_button = ctk.CTkButton(
            top_frame,
            text="← Home",
            width=90,
            height=35,
            command=lambda: self.show_page("home")
        )

        # Position the Home button
        back_button.pack(
            side="left"
        )

        # Create the quiz title
        quiz_title = ctk.CTkLabel(
            top_frame,
            text="VOCABULARY QUIZ",
            font=("Arial", 25, "bold")
        )

        # Position the quiz title
        quiz_title.pack(
            side="left",
            expand=True
        )

        # Create the information frame
        info_frame = ctk.CTkFrame(
            self.quiz_frame,
            fg_color="transparent"
        )

        # Position the information frame
        info_frame.pack(
            pady=(15, 5)
        )

        # Create the question counter
        self.round_label = ctk.CTkLabel(
            info_frame,
            text="Question 0 of 10",
            font=("Arial", 15, "bold")
        )

        # Position the question counter
        self.round_label.grid(
            row=0,
            column=0,
            padx=40
        )

        # Create the score label
        self.score_label = ctk.CTkLabel(
            info_frame,
            text="Score: 0",
            font=("Arial", 15, "bold")
        )

        # Position the score label
        self.score_label.grid(
            row=0,
            column=1,
            padx=40
        )

        # Create the question card
        question_card = ctk.CTkFrame(
            self.quiz_frame,
            corner_radius=15
        )

        # Position the question card
        question_card.pack(
            fill="x",
            padx=40,
            pady=20
        )

        # Create the question label
        self.question_label = ctk.CTkLabel(
            question_card,
            text="Your question will appear here.",
            font=("Arial", 18, "bold"),
            wraplength=580,
            justify="center"
        )

        # Position the question label
        self.question_label.pack(
            padx=30,
            pady=35
        )

        # Create the answers frame
        answers_frame = ctk.CTkFrame(
            self.quiz_frame,
            fg_color="transparent"
        )

        # Position the answers frame
        answers_frame.pack(
            pady=5
        )

        # Create the variable that stores the selected answer
        self.selected_answer = ctk.StringVar(
            value=""
        )

        # Create the first answer
        self.option1 = ctk.CTkRadioButton(
            answers_frame,
            text="Answer 1",
            variable=self.selected_answer,
            value="",
            font=("Arial", 15),
            width=450
        )

        # Position the first answer
        self.option1.pack(
            pady=7
        )

        # Create the second answer
        self.option2 = ctk.CTkRadioButton(
            answers_frame,
            text="Answer 2",
            variable=self.selected_answer,
            value="",
            font=("Arial", 15),
            width=450
        )

        # Position the second answer
        self.option2.pack(
            pady=7
        )

        # Create the third answer
        self.option3 = ctk.CTkRadioButton(
            answers_frame,
            text="Answer 3",
            variable=self.selected_answer,
            value="",
            font=("Arial", 15),
            width=450
        )

        # Position the third answer
        self.option3.pack(
            pady=7
        )

        # Create the fourth answer
        self.option4 = ctk.CTkRadioButton(
            answers_frame,
            text="Answer 4",
            variable=self.selected_answer,
            value="",
            font=("Arial", 15),
            width=450
        )

        # Position the fourth answer
        self.option4.pack(
            pady=7
        )

        # Create the feedback label
        self.feedback_label = ctk.CTkLabel(
            self.quiz_frame,
            text="",
            font=("Arial", 14, "bold"),
            wraplength=600,
            justify="center"
        )

        # Position the feedback label
        self.feedback_label.pack(
            pady=(10, 0)
        )

        # Create the Submit Answer button
        self.submit_button = ctk.CTkButton(
            self.quiz_frame,
            text="Submit Answer",
            width=220,
            height=45,
            font=("Arial", 16, "bold"),
            command=self.check_answer
        )

        # Position the Submit button
        self.submit_button.pack(
            pady=20
        )

        # Create the Next Question button
        self.next_button = ctk.CTkButton(
            self.quiz_frame,
            text="Next Question",
            width=220,
            height=45,
            font=("Arial", 16, "bold"),
            command=self.next_question
        )

        # Keep the Next Question button hidden initially
        self.next_button.pack_forget()

        # Hide the quiz screen initially
        self.quiz_frame.pack_forget()


    # START QUIZ

    # Start the quiz
    def start_quiz(self):

        # Reset the score
        self.score = 0

        # Reset the question number
        self.round_number = 0

        # Update the score
        self.score_label.configure(
            text="Score: 0"
        )

        # Hide the welcome screen
        self.welcome_frame.pack_forget()

        # Show the quiz screen
        self.quiz_frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=30
        )

        # Generate the first question
        self.next_question()


    # NEXT QUESTION

    # Generate the next question
    def next_question(self):

        # Check if 10 questions have been completed
        if self.round_number >= 10:

            # Show the final score
            self.show_final_score()

            # Stop
            return

        # Increase the question number
        self.round_number += 1

        # Update the question counter
        self.round_label.configure(
            text=f"Question {self.round_number} of 10"
        )

        # Get words from the database
        words = self.get_words()

        # Check that there are at least four words
        if len(words) < 4:

            # Display the database problem
            self.question_label.configure(
                text="Not enough words in the database.\n\n"
                     f"Only {len(words)} word(s) were found.\n"
                     "You need at least 4 words."
            )

            # Hide the answer buttons
            self.option1.pack_forget()
            self.option2.pack_forget()
            self.option3.pack_forget()
            self.option4.pack_forget()

            # Hide the submit button
            self.submit_button.pack_forget()

            # Stop
            return

        # Choose a random correct word
        correct_word, definition = random.choice(words)

        # Store the correct answer
        self.correct_answer = correct_word

        # Create the wrong answers list
        wrong_answers = []

        # Continue until three wrong answers are found
        while len(wrong_answers) < 3:

            # Choose another random word
            wrong_word, unused_definition = random.choice(words)

            # Check that it isn't the correct word
            if wrong_word != correct_word:

                # Check that it isn't already used
                if wrong_word not in wrong_answers:

                    # Add it to the wrong answers
                    wrong_answers.append(wrong_word)

        # Combine all answers
        options = wrong_answers + [correct_word]

        # Shuffle the answers
        random.shuffle(options)

        # Display the definition
        self.question_label.configure(
            text=f"Which word matches this definition?\n\n"
                 f"{definition}"
        )

        # Configure answer one
        self.option1.configure(
            text=options[0],
            value=options[0]
        )

        # Configure answer two
        self.option2.configure(
            text=options[1],
            value=options[1]
        )

        # Configure answer three
        self.option3.configure(
            text=options[2],
            value=options[2]
        )

        # Configure answer four
        self.option4.configure(
            text=options[3],
            value=options[3]
        )

        # Clear the selected answer
        self.selected_answer.set("")

        # Clear previous feedback
        self.feedback_label.configure(
            text=""
        )

        # Show all answer choices
        self.option1.pack(pady=7)
        self.option2.pack(pady=7)
        self.option3.pack(pady=7)
        self.option4.pack(pady=7)

        # Show the submit button
        self.submit_button.pack(
            pady=20
        )

        # Hide the next button
        self.next_button.pack_forget()


    # CHECK ANSWER

    # Check whether the user's answer is correct
    def check_answer(self):

        # Get the selected answer
        answer = self.selected_answer.get()

        # Check whether the user selected anything
        if answer == "":

            # Ask the user to select an answer
            self.feedback_label.configure(
                text="Please select an answer.",
                text_color="orange"
            )

            # Stop the function
            return

        # Check whether the answer is correct
        if answer == self.correct_answer:

            # Add one point
            self.score += 1

            # Update the score
            self.score_label.configure(
                text=f"Score: {self.score}"
            )

            # Show correct feedback
            self.feedback_label.configure(
                text=f"✓ Correct!\n\n"
                     f"Correct answer: {self.correct_answer}",
                text_color="green"
            )

        # Handle an incorrect answer
        else:

            # Show incorrect feedback and correct answer
            self.feedback_label.configure(
                text=f"✗ Incorrect!\n\n"
                     f"Your answer: {answer}\n"
                     f"Correct answer: {self.correct_answer}",
                text_color="red"
            )

        # Hide the submit button
        self.submit_button.pack_forget()

        # Show the next question button
        self.next_button.pack(
            pady=10
        )


    # FINAL SCORE

    # Display the final quiz score
    def show_final_score(self):

        # Display the final score
        self.question_label.configure(
            text=f"QUIZ COMPLETE!\n\n"
                 f"You scored {self.score} out of 10."
        )

        # Update the question counter
        self.round_label.configure(
            text="Quiz Finished"
        )

        # Hide all answer options
        self.option1.pack_forget()
        self.option2.pack_forget()
        self.option3.pack_forget()
        self.option4.pack_forget()

        # Clear the feedback
        self.feedback_label.configure(
            text=""
        )

        # Hide the Next Question button
        self.next_button.pack_forget()

        # Turn Submit into Play Again
        self.submit_button.configure(
            text="Play Again",
            command=self.restart_quiz
        )

        # Show Play Again
        self.submit_button.pack(
            pady=20
        )

    # RESTART
    # Restart the quiz
    def restart_quiz(self):

        # Reset the score
        self.score = 0

        # Reset the question number
        self.round_number = 0

        # Reset the score display
        self.score_label.configure(
            text="Score: 0"
        )

        # Reset the question counter
        self.round_label.configure(
            text="Question 0 of 10"
        )

        # Change the button back to Submit Answer
        self.submit_button.configure(
            text="Submit Answer",
            command=self.check_answer
        )

        # Start the quiz again
        self.next_question()