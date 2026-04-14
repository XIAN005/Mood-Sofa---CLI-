import os
import csv
import time
from datetime import date
from utils import clear_screen
from history import show_history
from advice import give_advice


def get_mood():
    energy_options = ["Productive", "Exhausted", "Dynamic", "Calm"]
    emotion_options = ["Happy", "Anxious", "Calm", "Irritable"]
    mental_options = ["Confused", "Focused", "Creative", "Distracted"]

    # Energy
    while True:
        clear_screen()
        print("Energy:")
        print("----------------------------")
        for i, option in enumerate(energy_options, start=1):
            print(f"{i}. {option}")
        print("----------------------------")
        choice = input("Choose a number: ")

        if choice.isdigit() and 1 <= int(choice) <= len(energy_options):
            energy = energy_options[int(choice) - 1]
            break
        print("Invalid choice, try again.\n")

    # Emotion
    while True:
        clear_screen()
        print("Emotion:")
        print("----------------------------")
        for i, option in enumerate(emotion_options, start=1):
            print(f"{i}. {option}")
        print("----------------------------")
        choice = input("Choose a number: ")

        if choice.isdigit() and 1 <= int(choice) <= len(emotion_options):
            emotion = emotion_options[int(choice) - 1]
            break
        print("Invalid choice, try again.\n")

    # Mental
    while True:
        clear_screen()
        print("Mental:")
        print("----------------------------")
        for i, option in enumerate(mental_options, start=1):
            print(f"{i}. {option}")
        print("----------------------------")
        choice = input("Choose a number: ")

        if choice.isdigit() and 1 <= int(choice) <= len(mental_options):
            mental = mental_options[int(choice) - 1]
            break
        print("Invalid choice, try again.\n")

    return energy, emotion, mental




file_path = "data/moods.csv"

def save_mood(energy, emotion, mental):
    today = date.today().isoformat()
    note = input("Add a note (optional): ")

    row = [today, energy, emotion, mental, note]
    file_exists = os.path.exists(file_path)

    with open(file_path, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["Date", "Energy", "Emotion", "Mental", "Note"])

        writer.writerow(row)
    

def mood_menu():
    while True:
        clear_screen()
        print("----------------------------")
        print(" Mood Menu ")
        print("----------------------------")
        print(" 1. Enter today's mood")
        print(" 2. Show mood history")
        print(" 3. Back to main menu")
        print("----------------------------")

        choice = input(" Choose an option: ")

        if choice == "1":
            enter_mood()
        elif choice == "2":
            show_history(file_path)
            input("\nPress Enter to continue...")
        elif choice == "3":
            clear_screen()
            break
        else:
            print("Invalid option. Choose 1-3.")
            time.sleep(1)

# Function to handle mood entry
def enter_mood():
    energy, emotion, mental = get_mood()
    time.sleep(0.5)
    clear_screen()
    note = input("Add a note (optional): ")
    today = date.today().isoformat()
    row = [today, energy, emotion, mental, note]

    # Check if file exists
    file_exists = os.path.exists(file_path)

    with open(file_path, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Date", "Energy", "Emotion", "Mental", "Note"])
        writer.writerow(row)
    clear_screen()
    print("\nMood saved successfully! \n")
    time.sleep(1.5)
    clear_screen()
    give_advice(file_path)
    time.sleep(7.5)
