# word = input("Search for a word: ").lower()

# first_letter = word[0]
# first_two_letters = word[:2]

# url = f"https://raw.githubusercontent.com/mhollingshead/open-dictionary/main/api/{first_letter}/{first_two_letters}.json"

# response = requests.get(url)

# #print(response.status_code)#no need to print the status code, this is for testing 

# if response.status_code == 200:

#     data = response.json()

#     #print(data[word])# removed this to print in the proper layout

# else:

#     print("Could not find the dictionary file.")

# #extraction section
# data = response.json() 
# word_data = data[word]
# word = word_data["word"]
# print(f"Word:{word}")
# print()


# for etymology in word_data["etymologies"]:
#   for details in etymology["partsOfSpeech"]:
#     print()

#     part_of_speech = details["partOfSpeech"]
#     print(f"part_of_speech:{part_of_speech}")

#     for definition in details["senses"]:

#       definition_text = definition["sense"]
#       print(f"Definition:{definition_text}")

#     for example in definition["examples"]:

#       print(f"Example:{example}")    


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

connection.commit()


url = "https://raw.githubusercontent.com/mhollingshead/open-dictionary/main/api/a/ab.json"

response = requests.get(url)

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

else:

    print("Could not download dictionary data.")


