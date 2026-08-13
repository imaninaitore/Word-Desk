#SQLITE DATABASE STORAGE
import requests
import sqlite3

connection = sqlite3.connect("WordDesk.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word TEXT,
    part_of_speech TEXT,
    definition TEXT,
    example TEXT
)
""")


url = "https://raw.githubusercontent.com/mhollingshead/open-dictionary/contents/api"

letters ="abcdefghijklmnopqrstuvwxyz"

for letter in letters:

    folder_url = f"{url}/{letter}"

    response = requests.get(folder_url)

if response.status_code == 200:

    data = response.json()

    print("Dictionary data downloaded!")

    for word in data:
     
     word_data = data[word]

     word = word_data["word"]

     for etymology in word_data["etymologies"]:

       for details in etymology["partsOfSpeech"]:

        part_of_speech = details["partOfSpeech"]

        for definition in details["senses"]:

            definition_text = definition["sense"]

            examples = definition.get("examples", [])

            example_text = " | ".join(examples)

            cursor.execute("""
            INSERT INTO words
            (word, part_of_speech, definition, example)
            VALUES (?, ?, ?, ?)
            """, (
                word,
                part_of_speech,
                definition_text,
                example_text
            ))

    connection.commit()

    print("Dictionary data saved to SQLite!")        

else:

    print("Could not download dictionary data.")

connection.close()