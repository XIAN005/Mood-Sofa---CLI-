
# Mood Sofa


#### Description:
> A modular command-line productivity & well-being application built in Python.

Mood Sofa is a structured CLI application that combines mood tracking, productivity tools, and personal notes in one clean interface.

During the development of Mood Sofa, one of the main technical challenges was ensuring a clean user experience within a minimalist CLI. I decided to separate the logic into multiple modules like advice.py and history.py to follow the Single Responsibility Principle. This makes the code easier to debug and allows for future expansion, such as adding a SQL database or a graphical interface. I chose to use the time and os libraries for the Pomodoro timer to ensure it runs efficiently on low-resource hardware like my Arch Linux setup. The advice engine uses a combination of energy levels and emotions to provide a more nuanced response than a simple mood picker.

Built as a CS50x Final Project.

---

## Features

### Mood Tracker
- Select daily:
  - Energy level
  - Emotion
  - Mental state
- Optional personal note
- Data stored in CSV format
- Personalized advice based on mood combination
- Full mood history viewer

### Pomodoro Timer
- 25 min work + 5 min break
- Short break (5 min)
- Long break (15 min)
- Live countdown in terminal
- Keyboard interrupt support

### Notes System
- Add notes
- View all notes
- Independent note management

---

## Architecture

Mood Sofa follows a modular design principle:
- main.py → Application entry point
- mood.py → Mood input logic
- advice.py → Advice engine
- history.py → Mood history viewer
- pomodoro.py → Timer system
- notes.py → Notes management
- user.py → User handling
- utils.py → Utility functions
- data/ → CSV storage


### Design Principles

- Single Responsibility Functions
- Separated Menus per Feature
- Clean CLI Navigation
- Expandable Architecture
- Reusable Timer Engine

---

## How to Run

Make sure Python 3 is installed.

 ```bash
python main.py
```

## Data Storage

Mood data is stored in:
- data/moods.csv

The file is automatically created if it does not exist.

### Future Improvements

- Mood streak tracking

- Statistics & analytics dashboard

- Calendar view

- Pomodoro session counter

- Export data to JSON

- Enhanced advice engine

### What I Learned

Through this project, I practiced:

- Modular program design

- CLI user experience structuring

- File handling with CSV

- Timer logic implementation

- Clean architecture thinking

- Code organization across multiple files


### Author

Nicolas Christian Toussaint

---

## License

This project is licensed under the MIT License.

See the `LICENSE` file for more details.