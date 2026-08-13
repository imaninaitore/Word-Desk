import requests
# STORE DATA IN DATABASE- FOR THE OFFLINE FUNCTIONALITY
import sqlite3

connection = sqlite3.connect("WordDesk.db")

cursor = connection.cursor()

#create the table in the database
cursor.execute("""
CREATE TABLE IF NOT EXISTS words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word TEXT,
    part_of_speech TEXT,
    definition TEXT
)
""")

connection.commit()

connection.close()


word = input("Search for a word: ")

url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

try:

    response = requests.get(url, timeout=15)

    if response.status_code == 200:

        data = response.json()

        connection = sqlite3.connect("WordDesk.db")
        cursor = connection.cursor()

        word = data[0]["word"]

        for details in data[0]["meanings"]:

            part_of_speech = details["partOfSpeech"]

            for definition in details["definitions"]:

                definition_text = definition["definition"]

                cursor.execute("""
                INSERT INTO words
                (word, part_of_speech, definition)
                VALUES (?, ?, ?)
                """, (
                    word,
                    part_of_speech,
                    definition_text
                ))

        connection.commit()


        print("Word saved successfully!")

    elif response.status_code == 404:

        print("Word not found.")

    else:

        print(f"API request failed with status code {response.status_code}")

except requests.RequestException as error:

    print("Could not connect to the dictionary service.")

    print(error) 

word = input("Search database: ")

connection = sqlite3.connect("WordDesk.db")

cursor = connection.cursor()

cursor.execute(
    "SELECT * FROM words WHERE word = ?",
    (word.lower(),)
)

results = cursor.fetchall()

for result in results:

    print(result)

    connection.close()
