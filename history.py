import csv
import os
from datetime import datetime
from utils import clear_screen

def show_history(file_path="data/moods.csv"):
    clear_screen()
    if not os.path.exists(file_path):
        print("No mood history found.")
        return
    
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        if not rows:
            print("No mood history found.")
            return
    
    print("\nYour Mood History:\n")
    for row in rows:
        # Formater la date joliment
        date_str = row["Date"]
        try:
            date_obj = datetime.fromisoformat(date_str)
            date_formatted = date_obj.strftime("%b %d, %Y")
        except:
            date_formatted = date_str
        
        print(f"  Date   : {date_formatted}")
        print(f"  Energy : {row['Energy']}")
        print(f"  Emotion: {row['Emotion']}")
        print(f"  Mental : {row['Mental']}")
        note = row['Note']
        if note:
            print(f"  Note   : {note}")
        print("-" * 30)
