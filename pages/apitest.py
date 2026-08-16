import requests #library that allows communication with websites and APIs

#word = "home"#later on i can make this the users input section
word = input("Search for a word: ")

url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

#exception handling of errors
try:
    response = requests.get(url, timeout=15)# get the info on the word from the api and set timeout to avoid waiting forever

    if response.status_code == 200: #success
        data= response.json() #api sends all data in json format
        #MOVING THROUGH NESTED JSON DATA TO GET THE INFORMATION I NEED
         # Get the word
        print("Word:", data[0]["word"]) #[0]-give first item in the list

        # Get all meanings using a for loop
        for details in data[0]["meanings"]: #meanings contains a list of dictionaries

            # Get the part of speech
            part_of_speech = details["partOfSpeech"]

            print("Part of speech:", part_of_speech)

            # Get all definitions for this meaning
            for definition in details["definitions"]:

                definition_text = definition["definition"]

                print("Definition:", definition_text)
                print()

    elif response.status_code == 404: #not found
        print("Word not found.")

    else:
        print(f"API request failed with status code {response.status_code}")

except requests.RequestException as error: #specifically catching errors related to the HTTP request.
    print("Could not connect to the dictionary service.")
    print(error)

