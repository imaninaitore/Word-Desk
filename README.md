# WordDesk

**WordDesk** is an offline desktop dictionary application built with Python and Tkinter. It provides a fast and simple way to search for words, view their definitions, and access vocabulary information without requiring an internet connection.

The application uses a local SQLite database to store dictionary data, allowing searches to be performed entirely on the user's device.

## Features

### Core Features

* Word Search — Search for words using the desktop interface.
* Definitions — View the definition of a searched word.
* Parts of Speech — Identify whether a word is a noun, verb, adjective, etc.
* Word Not Found Handling — Displays a clear message when a searched word is unavailable.
* Case-Insensitive Search — Search for words regardless of capitalization.
* Clear Search — Quickly clear the current search and results.
* Random Word — Discover a random word from the local dictionary.
* Word of the Day — Display a selected word when the application starts.

### Planned Features

The following features are planned for future versions of WordDesk:

* Favourites — Save frequently used words for quick access.
* Search History — Keep track of previously searched words.
* Example Sentences — Display example usage for dictionary entries.
* Vocabulary Quiz — Test vocabulary knowledge using questions generated from the dictionary database.
* Search Suggestions — Display matching words while typing.
* Keyboard Shortcuts — Provide shortcuts for common actions.

## Technology Stack

| Technology    | Purpose                            |
| ------------- | ---------------------------------- |
| Python        | Application logic                  |
| Tkinter       | Desktop graphical user interface   |
| SQLite        | Local dictionary database          |
| Requests      | Retrieving dictionary data         |
| BeautifulSoup | Extracting and processing web data |

## Application Architecture

WordDesk is separated into different components so that data collection, storage, and the desktop interface can be maintained independently.

```text
                Dictionary Source
                       |
                       v
                 Web Scraper
              Requests + BeautifulSoup
                       |
                       v
                SQLite Database
                 dictionary.db
                       |
                       v
                 WordDesk App
                    Tkinter
                       |
          +------------+------------+
          |            |            |
          v            v            v
       Search      Random Word   Word of Day
          |
          v
     Word Results
```

The dictionary data is collected separately and stored locally. Once the database has been populated, WordDesk can perform searches without needing an internet connection.

## Project Structure

```text
WordDesk/
|
├── app.py                  # Main Tkinter application
├── database.py             # Database connection and queries
├── scraper.py              # Dictionary data collection
├── dictionary.db           # Local SQLite database
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
|
└── assets/
    └── icons/              # Application icons and images
```

The exact structure may change as the application develops.

## Database

WordDesk uses SQLite to store dictionary entries locally.

A dictionary entry can contain information such as:

```text
id
word
definition
part_of_speech
example
```

The database allows WordDesk to search and retrieve information without repeatedly requesting data from an external website.

# future developments
Future versions may introduce additional tables for:

```text
favorites
search_history
quiz_results
```

## Data Collection

The initial dictionary database can be populated using a separate Python data collection script.

The scraper uses:

```text
Requests
    |
    v
HTML Response
    |
    v
BeautifulSoup
    |
    v
Extract Dictionary Data
    |
    v
Clean Data
    |
    v
SQLite
```

The scraper and desktop application are kept separate so that WordDesk itself does not need to access the internet every time a user searches for a word.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/imaninaitore/Word-Desk.git
```

### 2. Enter the project directory

```bash
cd Word-Desk
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv my_env
```

Activate it:

```bash
my_env\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv my_env
source my_env/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run WordDesk

```bash
python app.py
```

## Requirements- technologies used

* Python 3.10+
* Tkinter
* SQLite3
* Requests
* BeautifulSoup4

Tkinter and SQLite3 are included with most standard Python installations.

## How WordDesk Works

When a user searches for a word:

```text
User enters word
       |
       v
Tkinter Entry
       |
       v
Search function
       |
       v
SQLite query
       |
       v
Word found?
    /       \
  Yes        No
   |          |
   v          v
Display     Show
results     message
```

Because the dictionary data is stored locally, the search process does not depend on an active internet connection.

## Project Goals

WordDesk aims to provide:

* Fast local word searches
* A simple desktop interface
* Reliable offline access to dictionary data
* Organized local data storage
* Useful vocabulary tools
* A clean and maintainable Python codebase

## Future Development

WordDesk is designed to grow beyond basic dictionary functionality.

Future development may include:

* Favourites management
* Search history
* Example sentences
* Vocabulary quizzes
* Search autocomplete
* Improved database indexing
* More detailed word information
* Custom themes
* Application settings
* Exporting saved words
* Improved accessibility

## Offline Functionality

Once the dictionary database has been populated, the main WordDesk application does not require an internet connection to search the available dictionary data.

Internet access is only relevant to the separate data collection and update process.

## Contributing

Contributions, suggestions, and improvements are welcome.

To contribute:

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature/new-feature
```

3. Make your changes.
4. Commit your changes.

```bash
git commit -m "Add new feature"
```

5. Push the branch.

```bash
git push origin feature/new-feature
```

6. Open a Pull Request.

## License
this project is under the MIT license

## Author

**Imani Naitore**

GitHub: `https://github.com/imaninaitore`

---

**WordDesk — Your words, available offline.Right on your desk.**
