import time
from utils import clear_screen


# -----------------------------
# Generic timer function
# -----------------------------
def run_timer(minutes, label):
    clear_screen()
    print("----------------------------")
    print(f" {label} started ")
    print("----------------------------")

    try:
        for remaining in range(minutes * 60, 0, -1):
            mins, secs = divmod(remaining, 60)
            print(f"\r Time left: {mins:02d}:{secs:02d}", end="")
            time.sleep(1)

        print(f"\n\n{label} finished!")
        input("Press Enter to continue...")
    except KeyboardInterrupt:
        print("\nTimer stopped manually.")
        time.sleep(1)


# -----------------------------
# Full Pomodoro session
# -----------------------------
def start_pomodoro():
    run_timer(25, "Pomodoro Work Session")
    run_timer(5, "Short Break")


# -----------------------------
# Pomodoro menu
# -----------------------------
def pomodoro_menu():
    while True:
        clear_screen()
        print("----------------------------")
        print(" Pomodoro ")
        print("----------------------------")
        print(" 1. Start Pomodoro (25 min work + 5 min break)")
        print(" 2. Short Break (5 min)")
        print(" 3. Long Break (15 min)")
        print(" 4. Back to main menu")
        print("----------------------------")

        choice = input(" Choose an option: ")

        if choice == "1":
            start_pomodoro()
        elif choice == "2":
            run_timer(5, "Short Break")
        elif choice == "3":
            run_timer(15, "Long Break")
        elif choice == "4":
            clear_screen()
            break
        else:
            print("Invalid option. Choose 1-4.")
            time.sleep(1)
