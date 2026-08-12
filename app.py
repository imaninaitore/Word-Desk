# import customtkinter as ctk

# window = ctk.CTk()
# window.geometry("600x400")
# window.resizable(False, False)

# header_frame= ctk.CTkFrame(window)
# header_frame.pack()

# title= ctk.CTkLabel(header_frame,text="WORD DESK", font=("Arial", 28, "bold"))
# title.pack(pady=10)
# title2= ctk.CTkLabel(header_frame,text="Words, available offline.Right on your desk.",font=("Arial", 18))
# title2.pack()

# #search section
# search_frame= ctk.CTkFrame(window)
# search_frame.pack()

# search_word=ctk.CTkLabel(search_frame,text="Search for a word: ",font=("Arial", 12)).grid(row=0,column=0)
# search_word=ctk.CTkEntry(search_frame).grid(row=0,column=1)

# search_btn=ctk.CTkButton(search_frame,text="search").grid(row=0,column=2)

# info_frame= ctk.CTkFrame(window)
# info_frame.pack()

# #word
# word_label = ctk.CTkLabel(info_frame, text="Word:",font=("Arial", 20, "bold"))
# word_label.pack(pady=15)

# #part of speech
# part_of_speech_label = ctk.CTkLabel( info_frame, text="Part of speech:")
# part_of_speech_label.pack(pady=5)

# #definition
# definition_label = ctk.CTkLabel( info_frame, text="Definition:", wraplength=600)

# definition_label.pack(pady=10)

# window.mainloop()

import customtkinter as ctk

window = ctk.CTk()
window.geometry("700x600")
window.resizable(False, False)
window.title("Word Desk")

#heading
header_frame = ctk.CTkFrame(window, fg_color="transparent")
header_frame.pack(pady=(30, 15))

title = ctk.CTkLabel(header_frame, text="WORD DESK", font=("Arial", 32, "bold"))
title.pack()

title2 = ctk.CTkLabel(header_frame, text="Words, available offline. Right on your desk.", font=("Arial", 14))
title2.pack(pady=(5, 0))

#search
search_frame = ctk.CTkFrame(window, corner_radius=15)
search_frame.pack(padx=40, pady=15, fill="x")

search_word_label = ctk.CTkLabel(search_frame, text="Search for a word", font=("Arial", 14, "bold"))
search_word_label.grid(row=0, column=0, padx=(20, 10), pady=20)

search_word = ctk.CTkEntry(search_frame, width=300, height=40, placeholder_text="Enter a word...")
search_word.grid(row=0, column=1, padx=10, pady=20)

search_btn = ctk.CTkButton(search_frame, text="SEARCH", width=100, height=40)
search_btn.grid(row=0, column=2, padx=(10, 20), pady=20)

#frame with the section of word, parts of speech and definition
info_frame = ctk.CTkFrame(window, corner_radius=15)
info_frame.pack(padx=40, pady=15, fill="both", expand=True)

#WORD
word_label = ctk.CTkLabel(info_frame, text="Word", font=("Arial", 28, "bold"))
word_label.pack(pady=(25, 5))

#PARTS OF SPEECH
part_of_speech_label = ctk.CTkLabel(info_frame, text="Part of speech", font=("Arial", 14))
part_of_speech_label.pack(pady=5)

#DEFINITION
definition_title = ctk.CTkLabel(info_frame, text="Definition", font=("Arial", 16, "bold"))
definition_title.pack(pady=(25, 5))

definition_label = ctk.CTkLabel(info_frame, text="Search for a word to see its definition.", font=("Arial", 14), wraplength=550)
definition_label.pack(padx=30, pady=5)

#search function getting from the api


window.mainloop()
