import customtkinter as ctk
import sqlite3
import random

# WINDOW
quiz_window = ctk.CTk()
quiz_window.geometry("750x700")
quiz_window.resizable(False, False)
quiz_window.title("WordDesk - Vocabulary Quiz")

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


# VARIABLES
score = 0
round_number = 0
correct_answer = ""


# DATABASE
def get_words():

    connection = sqlite3.connect("WordDesk.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT word, definition
        FROM words
    """)

    results = cursor.fetchall()

    connection.close()

    return results


# START QUIZ
def start_quiz():

    global score
    global round_number

    score = 0
    round_number = 0

    score_label.configure(text="Score: 0")

    welcome_frame.pack_forget()

    quiz_frame.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=30
    )

    next_question()


# NEXT QUESTION
def next_question():

    global round_number
    global correct_answer

    if round_number >= 10:

        show_final_score()

        return

    round_number += 1

    round_label.configure(
        text=f"Question {round_number} of 10"
    )

    words = get_words()

    if len(words) < 4:

        question_label.configure(
            text="Not enough words in the database."
        )

        return

    # Choose correct word
    correct_word, definition = random.choice(words)

    correct_answer = correct_word

    # Get 3 wrong answers
    wrong_answers = []

    while len(wrong_answers) < 3:

        wrong_word, wrong_definition = random.choice(words)

        if (
            wrong_word != correct_word
            and wrong_word not in wrong_answers
        ):

            wrong_answers.append(wrong_word)

    # Combine answers
    options = wrong_answers + [correct_word]

    random.shuffle(options)

    # Display definition
    question_label.configure(
        text=f"Which word matches this definition?\n\n"
             f"{definition}"
    )

    # Display options
    option1.configure(
        text=options[0],
        value=options[0]
    )

    option2.configure(
        text=options[1],
        value=options[1]
    )

    option3.configure(
        text=options[2],
        value=options[2]
    )

    option4.configure(
        text=options[3],
        value=options[3]
    )

    selected_answer.set("")

    feedback_label.configure(
        text=""
    )


# CHECK ANSWER
def check_answer():

    global score

    answer = selected_answer.get()

    if answer == "":

        feedback_label.configure(
            text="Please select an answer.",
            text_color="orange"
        )

        return

    if answer == correct_answer:

        score += 1

        score_label.configure(
            text=f"Score: {score}"
        )

        feedback_label.configure(
            text=f"✓ Correct!\n\n"
                 f"Correct answer: {correct_answer}",
            text_color="green"
        )

    else:

        feedback_label.configure(
            text=f"✗ Incorrect!\n\n"
                 f"Your answer: {answer}\n"
                 f"Correct answer: {correct_answer}",
            text_color="red"
        )

    # Hide the submit button
    submit_button.pack_forget()

    # Show the next question button
    next_button.pack(
        pady=10
    )

# FINAL SCORE
def show_final_score():

    question_label.configure(
        text=f"🎉 QUIZ COMPLETE!\n\n"
             f"You scored {score} out of 10."
    )

    round_label.configure(
        text="Quiz Finished"
    )

    option1.pack_forget()
    option2.pack_forget()
    option3.pack_forget()
    option4.pack_forget()

    feedback_label.configure(
        text=""
    )

    submit_button.configure(
        text="Play Again",
        command=restart_quiz
    )


# RESTART QUIZ

def restart_quiz():

    global score
    global round_number

    score = 0
    round_number = 0

    score_label.configure(
        text="Score: 0"
    )

    round_label.configure(
        text="Question 0 of 10"
    )

    question_label.configure(
        text="Which word matches this definition?"
    )

    option1.pack(pady=7)
    option2.pack(pady=7)
    option3.pack(pady=7)
    option4.pack(pady=7)

    feedback_label.configure(
        text=""
    )

    submit_button.configure(
        text="Submit Answer",
        command=check_answer
    )

    next_question()


# GO BACK HOME

def back_to_home():

    quiz_frame.pack_forget()

    welcome_frame.pack(
        fill="both",
        expand=True
    )


# WELCOME SCREEN
welcome_frame = ctk.CTkFrame(
    quiz_window,
    fg_color="transparent"
)

welcome_frame.pack(
    fill="both",
    expand=True
)


# title
welcome_title = ctk.CTkLabel(
    welcome_frame,
    text="WORD DESK",
    font=("Arial", 38, "bold")
)

welcome_title.pack(
    pady=(120, 5)
)


welcome_subtitle = ctk.CTkLabel(
    welcome_frame,
    text="Vocabulary Quiz",
    font=("Arial", 24, "bold")
)

welcome_subtitle.pack(
    pady=5
)


welcome_description = ctk.CTkLabel(
    welcome_frame,
    text="Test your vocabulary and see how many words you know!",
    font=("Arial", 16),
    wraplength=500
)

welcome_description.pack(
    pady=(15, 40)
)


get_started_button = ctk.CTkButton(
    welcome_frame,
    text="Get Started",
    width=220,
    height=55,
    corner_radius=12,
    font=("Arial", 18, "bold"),
    command=start_quiz
)

get_started_button.pack(
    pady=10
)

# QUIZ SCREEN
quiz_frame = ctk.CTkFrame(
    quiz_window,
    corner_radius=20
)

# Top section
top_frame = ctk.CTkFrame(
    quiz_frame,
    fg_color="transparent"
)

top_frame.pack(
    fill="x",
    padx=20,
    pady=(15, 5)
)

back_button = ctk.CTkButton(
    top_frame,
    text="← Home",
    width=90,
    height=35,
    command=back_to_home
)

back_button.pack(
    side="left"
)

quiz_title = ctk.CTkLabel(
    top_frame,
    text="VOCABULARY QUIZ",
    font=("Arial", 25, "bold")
)

quiz_title.pack(
    side="left",
    expand=True
)

# Score and round

info_frame = ctk.CTkFrame(
    quiz_frame,
    fg_color="transparent"
)

info_frame.pack(
    pady=(15, 5)
)


round_label = ctk.CTkLabel(
    info_frame,
    text="Question 0 of 10",
    font=("Arial", 15, "bold")
)

round_label.grid(
    row=0,
    column=0,
    padx=40
)


score_label = ctk.CTkLabel(
    info_frame,
    text="Score: 0",
    font=("Arial", 15, "bold")
)

score_label.grid(
    row=0,
    column=1,
    padx=40
)


# Question card
question_card = ctk.CTkFrame(
    quiz_frame,
    corner_radius=15
)
question_card.pack(
    fill="x",
    padx=40,
    pady=20
)

question_label = ctk.CTkLabel(
    question_card,
    text="Which word matches this definition?",
    font=("Arial", 18, "bold"),
    wraplength=580,
    justify="center"
)

question_label.pack(
    padx=30,
    pady=35
)

# Answers

answers_frame = ctk.CTkFrame(
    quiz_frame,
    fg_color="transparent"
)

answers_frame.pack(
    pady=5
)

selected_answer = ctk.StringVar()

option1 = ctk.CTkRadioButton(
    answers_frame,
    text="",
    variable=selected_answer,
    value="",
    font=("Arial", 15),
    width=450
)

option1.pack(
    pady=7
)

option2 = ctk.CTkRadioButton(
    answers_frame,
    text="",
    variable=selected_answer,
    value="",
    font=("Arial", 15),
    width=450
)

option2.pack(
    pady=7
)


option3 = ctk.CTkRadioButton(
    answers_frame,
    text="",
    variable=selected_answer,
    value="",
    font=("Arial", 15),
    width=450
)

option3.pack(
    pady=7
)

option4 = ctk.CTkRadioButton(
    answers_frame,
    text="",
    variable=selected_answer,
    value="",
    font=("Arial", 15),
    width=450
)

option4.pack(
    pady=7
)

# Feedback

feedback_label = ctk.CTkLabel(
    quiz_frame,
    text="",
    font=("Arial", 14, "bold")
)

feedback_label.pack(
    pady=(10, 0)
)

# Submit button

submit_button = ctk.CTkButton(
    quiz_frame,
    text="Submit Answer",
    width=220,
    height=45,
    corner_radius=10,
    font=("Arial", 16, "bold"),
    command=check_answer
)

submit_button.pack(
    pady=20
)
#next question button
next_button = ctk.CTkButton(
    quiz_frame,
    text="Next Question",
    width=220,
    height=45,
    corner_radius=10,
    font=("Arial", 16, "bold"),
    command=next_question
)

next_button.pack(
    pady=10
)

next_button.pack_forget()

# RUN

quiz_window.mainloop()