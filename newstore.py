import requests
import sqlite3

word = input("Search for a word: ").lower()

first_letter = word[0]
first_two_letters = word[:2]

url = f"https://raw.githubusercontent.com/mhollingshead/open-dictionary/main/api/{first_letter}/{first_two_letters}.json"

response = requests.get(url)

print(response.status_code)

if response.status_code == 200:

    data = response.json()

    print(data[word])

else:

    print("Could not find the dictionary file.")