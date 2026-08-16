import customtkinter as ctk
import sqlite3

# window = ctk.CTk()
# window.geometry("700x600")
# window.resizable(False, False)
# window.title("Word Desk")

#class to make the homepage a frame that lives inside the main application
class HomePage(ctk.CTkFrame):

  def __init__(self, parent, show_page, get_current_user, set_current_user):
               
        super().__init__(parent)

        self.show_page = show_page

        self.get_current_user = get_current_user
        self.set_current_user = set_current_user

        #search function getting from the database

        def search_function():

          word = search_word.get().lower()

          connection = sqlite3.connect("WordDesk.db")
          cursor = connection.cursor()

          cursor.execute("""
          SELECT part_of_speech, definition, example
          FROM words
          WHERE word = ?
          """, (word,))

          results = cursor.fetchall()

          connection.close()

          if results:

             word_label.configure(text=word.capitalize())

             part_of_speech_label.configure(
               text="Part of speech: " + results[0][0]
              )

             definition_label.configure(
              text="Definition: " + results[0][1]
              )

          else:

               word_label.configure(text="Word not found")

               part_of_speech_label.configure(text="")

               definition_label.configure( text="This word is not available in the offline dictionary." )


#heading
        header_frame = ctk.CTkFrame(self, fg_color="transparent")
        header_frame.pack(pady=(30, 15))

        title = ctk.CTkLabel(header_frame, text="WORD DESK", font=("Arial", 32, "bold"))
        title.pack()

        title2 = ctk.CTkLabel(header_frame, text="Words, available offline. Right on your desk.", font=("Arial", 14))
        title2.pack(pady=(5, 0))

        username = self.get_current_user()

        welcome_label = ctk.CTkLabel( header_frame,text=f"Welcome, {username}!",font=("Arial", 18, "bold"))
        welcome_label.pack(pady=(10, 0))

#search
        search_frame = ctk.CTkFrame(self, corner_radius=15)
        search_frame.pack(padx=40, pady=15, fill="x")

        search_word_label = ctk.CTkLabel(search_frame, text="Search for a word", font=("Arial", 14, "bold"))
        search_word_label.grid(row=0, column=0, padx=(20, 10), pady=20)

        search_word = ctk.CTkEntry(search_frame, width=300, height=40, placeholder_text="Enter a word...")
        search_word.grid(row=0, column=1, padx=10, pady=20)

        search_btn = ctk.CTkButton(search_frame, text="SEARCH", width=100, height=40,command=search_function)
        search_btn.grid(row=0, column=2, padx=(10, 20), pady=20)

#frame with the section of word, parts of speech and definition
        info_frame = ctk.CTkFrame(self, corner_radius=15)
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

#Quiz button
        quiz_button = ctk.CTkButton(self,text="Go to Quiz",width=150,command=lambda: self.show_page("quiz"))

        quiz_button.pack(pady=10)

# Logout button

        logout_button = ctk.CTkButton(self,text="Logout",width=150,command=self.logout)
        logout_button.pack(pady=(5, 15))      