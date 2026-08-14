import tkinter as tk
from tkinter import messagebox

# MAIN WINDOW
window = tk.Tk()
window.title("Word Desk - Instructions")
window.geometry("500x900")


# MAIN FRAME

main_frame = tk.Frame(window)
main_frame.pack(pady=20)


# TITLE
title = tk.Label(
    main_frame,
    text="WORD DESK",
    font=("Arial", 28, "bold")
)
title.pack(pady=10)


subtitle = tk.Label(main_frame,text="Your Vocabulary Learning Space",font=("Arial", 16))
subtitle.pack(pady=5)


# WELCOME MESSAGE

welcome = tk.Label(main_frame,text="Welcome! Let's learn new words and improve your vocabulary.",font=("Arial", 12))
welcome.pack(pady=15)

# INSTRUCTIONS FRAME
instructions_frame = tk.Frame(main_frame)
instructions_frame.pack(pady=10)

# SEARCH SECTION
search_title = tk.Label(instructions_frame,text="1. SEARCH FOR A WORD",font=("Arial", 14, "bold"))
search_title.grid(row=0, column=0, sticky="w", pady=5)

search_text = tk.Label(instructions_frame,text="Use the search feature to find a word and learn its definition,",font=("Arial", 11))
search_text.grid(row=1, column=0, sticky="w")

search_text2 = tk.Label(instructions_frame,text="part of speech and example of how the word is used.",font=("Arial", 11))
search_text2.grid(row=2, column=0, sticky="w", pady=(0, 15))


# RANDOM WORD SECTION
random_title = tk.Label(instructions_frame,text="2. DISCOVER A RANDOM WORD",font=("Arial", 14, "bold"))
random_title.grid(row=3, column=0, sticky="w", pady=5)

random_text = tk.Label( instructions_frame,text="Use Random Word to discover a new word and learn something new.",font=("Arial", 11))
random_text.grid(row=4, column=0, sticky="w", pady=(0, 15))


# WORD OF THE DAY SECTION
day_title = tk.Label(instructions_frame,text="3. WORD OF THE DAY",font=("Arial", 14, "bold"))
day_title.grid(row=5, column=0, sticky="w", pady=5)

day_text = tk.Label(instructions_frame,text="Learn one new word each day and build your vocabulary over time.",font=("Arial", 11))
day_text.grid(row=6, column=0, sticky="w", pady=(0, 15))


# QUIZ SECTION

quiz_title = tk.Label(instructions_frame,text="4. TEST YOUR KNOWLEDGE",font=("Arial", 14, "bold"))
quiz_title.grid(row=7, column=0, sticky="w", pady=5)

quiz_text = tk.Label(instructions_frame,text="Take vocabulary quizzes to test what you have learned.",font=("Arial", 11))
quiz_text.grid(row=8, column=0, sticky="w", pady=(0, 15))


#IMPORTANT TIP

note_frame = tk.Frame(main_frame)
note_frame.pack(pady=10)

note = tk.Label(note_frame,text="TIP: The more words you learn, the stronger your vocabulary becomes!",font=("Arial", 11, "italic"))
note.pack()

# START BUTTON

def start_learning():
    messagebox.showinfo("Word Desk","Let's start learning!" )

start_button = tk.Button(main_frame,text="START LEARNING",font=("Arial", 12, "bold"),command=start_learning)
start_button.pack(pady=20)

# MAIN LOOP
window.mainloop()