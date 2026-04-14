import csv
import os
from datetime import date
from utils import clear_screen

file_path = "data/notes.csv"

def add_note():
    title = input("Title: ").strip()
    content = input("Content: ").strip()
    today = date.today().isoformat()
    row = [today, title, content]

    file_exists = os.path.exists(file_path)

    with open(file_path, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Date", "Title", "Content"])
        writer.writerow(row)

    print("\nNote saved successfully!\n")

def show_notes():
    if not os.path.exists(file_path):
        print("No notes found.")
        return

    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        if not rows:
            print("No notes found.")
            return

    print("\nYour Notes:\n")
    for row in rows:
        print(f"Date   : {row['Date']}")
        print(f"Title  : {row['Title']}")
        print(f"Content: {row['Content']}")
        print("-" * 30)

def note_menu():
    while True:
        clear_screen()
        print("\nNotes Menu:")
        print("----------------------------")
        print(" 1. Add note")
        print(" 2. Show all notes")
        print(" 3. Back to main menu")
        print("----------------------------")
        n_choice = input("Choose an option: ")
                
        if n_choice == "1":
            add_note()
        elif n_choice == "2":
            show_notes()
        elif n_choice == "3":
            clear_screen()
            break
        else:
            print("Invalid option. Choose 1-3.")


                