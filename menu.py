from user import get_user_name
from history import show_history
import csv
import os
from datetime import date
from pomodoro import pomodoro_menu
from notes import add_note, show_notes
import time
from mood import mood_menu
from utils import clear_screen
from notes import note_menu

file_path = "data/moods.csv"


def main_menu():
    clear_screen()
    name = get_user_name()
    print("----------------------------")
    print(" Mood Sofa ")
    print(f" Welcome {name} ")
    print("----------------------------")
    while True:
        # Menu options
        print("\n Menu:")
        print("----------------------------")
        print(" 1.Mood")
        print(" 2.Pomodoro")
        print(" 3.Notes")
        print(" 4.Quit")
        print("----------------------------")
        choice = input(" Choose an option: ")
        print("\n")
        

        if choice == "1":
            mood_menu()
        elif choice == "2":
            pomodoro_menu()
        elif choice == "3":
            note_menu()
        elif choice == "4":
            clear_screen()
            print("----------------------------")
            print(f" Goodbye {name}!")
            print("----------------------------")
            break
        else:
            print("Invalid option. Please choose 1-4.")
        
    
