import customtkinter as ctk
import sqlite3
import random


# ==========================================
# WINDOW
# ==========================================

quiz_window = ctk.CTk()
quiz_window.geometry("750x700")
quiz_window.resizable(False, False)
quiz_window.title("WordDesk - Quiz")

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


# ==========================================
# VARIABLES
# ==========================================

score = 0
round_number = 0
correct_answer = ""


# ==========================================
# DATABASE
# ==========================================

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


# ==========================================
# HOME
# ==========================================

def go_home():

    # Hide quiz screen
    quiz_frame.pack_forget()

    # Show welcome screen
    welcome_frame.pack(
        fill="both",
        expand=True
    )


# ==========================================
# START QUIZ
# ==========================================

def start_quiz():

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

    welcome_frame.pack_forget()

    quiz_frame.pack(
        fill="both",
        expand=True,
        padx=25,
        pady=25
    )

    next_question()


# ==========================================
# NEXT QUESTION
# ==========================================

def next_question():

    global round_number
    global correct_answer

    # Check if quiz is finished
    if round_number >= 10:

        show_final_score()

        return

    round_number += 1

    round_label.configure(
        text=f"Question {round_number} of 10"
    )

    words = get_words()

    # Check database
    if len(words) < 4:

        question_label.configure(
            text="Not enough words in the database."
        )

        return

    # Select correct word
    correct_word, definition = random.choice(words)

    correct_answer = correct_word

    # Get wrong answers
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

    # Shuffle answers
    random.shuffle(options)

    # Show question
    question_label.configure(
        text=f"Which word matches this definition?\n\n"
             f"{definition}"
    )

    # Show answers
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

    # Clear previous selection
    selected_answer.set("")

    feedback_label.configure(
        text=""
    )


# ==========================================
# CHECK ANSWER
# ==========================================

def check_answer():

    global score

    answer = selected_answer.get()

    if answer == "":

        feedback_label.configure(
            text="Please select an answer first.",
            text_color="orange"
        )

        return

    if answer == correct_answer:

        score += 1

        score_label.configure(
            text=f"Score: {score}"
        )

        feedback_label.configure(
            text="✓ Correct!",
            text_color="green"
        )

    else:

        feedback_label.configure(
            text=f"✗ Incorrect! Answer: {correct_answer}",
            text_color="red"
        )

    # Wait before next question
    quiz_window.after(
        800,
        next_question
    )


# ==========================================
# FINAL SCORE
# ==========================================

def show_final_score():

    question_label.configure(
        text=f"QUIZ COMPLETE!\n\n"
             f"You scored {score} out of 10."
    )

    round_label.configure(
        text="Quiz Finished"
    )

    # Hide answers
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


# ==========================================
# RESTART
# ==========================================

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

    # Bring answers back
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


# ==========================================
# WELCOME PAGE
# ==========================================

welcome_frame = ctk.CTkFrame(
    quiz_window,
    fg_color="transparent"
)

welcome_frame.pack(
    fill="both",
    expand=True
)


# Main title

welcome_title = ctk.CTkLabel(
    welcome_frame,
    text="WORD DESK",
    font=("Arial", 40, "bold")
)

welcome_title.pack(
    pady=(120, 5)
)


# Quiz title
welcome_subtitle = ctk.CTkLabel(
    welcome_frame,
    text="Vocabulary Quiz",
    font=("Arial", 25, "bold")
)

welcome_subtitle.pack(
    pady=5
)

# Description

welcome_description = ctk.CTkLabel(
    welcome_frame,
    text="Test your vocabulary knowledge with 10 questions.",
    font=("Arial", 16)
)

welcome_description.pack(
    pady=(15, 35)
)


# Get Started

get_started_button = ctk.CTkButton(
    welcome_frame,
    text="Get Started",
    width=230,
    height=50,
    corner_radius=12,
    font=("Arial", 18, "bold"),
    command=start_quiz
)

get_started_button.pack(
    pady=10
)

# ==========================================
# QUIZ PAGE
# ==========================================

quiz_frame = ctk.CTkFrame(
    quiz_window,
    corner_radius=20
)


# ------------------------------------------
# Top bar
# ------------------------------------------

top_frame = ctk.CTkFrame(
    quiz_frame,
    fg_color="transparent"
)

top_frame.pack(
    fill="x",
    padx=20,
    pady=15
)


# Back Home button

back_home_button = ctk.CTkButton(
    top_frame,
    text="← Home",
    width=90,
    height=35,
    corner_radius=8,
    command=go_home
)

back_home_button.pack(
    side="left"
)


# Quiz title

quiz_title = ctk.CTkLabel(
    top_frame,
    text="VOCABULARY QUIZ",
    font=("Arial", 25, "bold")
)

quiz_title.pack(
    side="left",
    expand=True
)


# ------------------------------------------
# Question / Score
# ------------------------------------------

info_frame = ctk.CTkFrame(
    quiz_frame,
    fg_color="transparent"
)

info_frame.pack(
    pady=10
)


round_label = ctk.CTkLabel(
    info_frame,
    text="Question 0 of 10",
    font=("Arial", 15, "bold")
)

round_label.grid(
    row=0,
    column=0,
    padx=50
)


score_label = ctk.CTkLabel(
    info_frame,
    text="Score: 0",
    font=("Arial", 15, "bold")
)

score_label.grid(
    row=0,
    column=1,
    padx=50
)


# ------------------------------------------
# Question Card
# ------------------------------------------

question_card = ctk.CTkFrame(
    quiz_frame,
    corner_radius=15
)

question_card.pack(
    fill="x",
    padx=40,
    pady=15
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


# ------------------------------------------
# Answer Options
# ------------------------------------------

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
    font=("Arial", 15)
)

option1.pack(
    pady=7
)


option2 = ctk.CTkRadioButton(
    answers_frame,
    text="",
    variable=selected_answer,
    value="",
    font=("Arial", 15)
)

option2.pack(
    pady=7
)


option3 = ctk.CTkRadioButton(
    answers_frame,
    text="",
    variable=selected_answer,
    value="",
    font=("Arial", 15)
)

option3.pack(
    pady=7
)


option4 = ctk.CTkRadioButton(
    answers_frame,
    text="",
    variable=selected_answer,
    value="",
    font=("Arial", 15)
)

option4.pack(
    pady=7
)


# ------------------------------------------
# Feedback
# ------------------------------------------

feedback_label = ctk.CTkLabel(
    quiz_frame,
    text="",
    font=("Arial", 14, "bold")
)

feedback_label.pack(
    pady=5
)


# ------------------------------------------
# Submit
# ------------------------------------------

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
    pady=15
)


# ==========================================
# RUN APPLICATION
# ==========================================

quiz_window.mainloop()