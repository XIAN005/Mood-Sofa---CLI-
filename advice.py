import csv
import os

def give_advice(file_path="data/moods.csv"):
    import csv, os
    #advice dictionnary
    advice_dict = {
    # Happy
    ("Happy", "Productive", "Confused"): "Take a few minutes to clarify your thoughts before starting tasks.",
    ("Happy", "Productive", "Focused"): "Use your energy to make progress on your most important projects.",
    ("Happy", "Productive", "Creative"): "Let your imagination flow—write or draw what comes to mind.",
    ("Happy", "Productive", "Distracted"): "Jot down your ideas in a notebook to avoid getting scattered.",
    ("Happy", "Exhausted", "Confused"): "Take a short nap or break to recharge.",
    ("Happy", "Exhausted", "Focused"): "Prioritize simple and easy tasks to maintain momentum.",
    ("Happy", "Exhausted", "Creative"): "Let inspiration come naturally—meditate or listen to music.",
    ("Happy", "Exhausted", "Distracted"): "Take deep breaths and refocus on one activity.",
    ("Happy", "Dynamic", "Confused"): "Brainstorm to channel your energy toward a clear solution.",
    ("Happy", "Dynamic", "Focused"): "Use your dynamism to complete a project or challenge.",
    ("Happy", "Dynamic", "Creative"): "Start an artistic or innovative project while inspiration is high.",
    ("Happy", "Dynamic", "Distracted"): "Organize your schedule to avoid distractions.",
    
    # Anxious
    ("Anxious", "Productive", "Confused"): "Write down your worries to get them out of your mind before working.",
    ("Anxious", "Productive", "Focused"): "Turn your anxiety into motivation to finish what matters.",
    ("Anxious", "Productive", "Creative"): "Draw or write to express your feelings.",
    ("Anxious", "Productive", "Distracted"): "Break tasks into small, clear steps.",
    ("Anxious", "Exhausted", "Confused"): "Breathe deeply and take a restorative break.",
    ("Anxious", "Exhausted", "Focused"): "Focus on a very simple, calming task.",
    ("Anxious", "Exhausted", "Creative"): "Let your mind wander with music or writing.",
    ("Anxious", "Exhausted", "Distracted"): "Step away from screens and take a short walk to calm down.",
    ("Anxious", "Dynamic", "Confused"): "Write down your ideas and worries to organize them.",
    ("Anxious", "Dynamic", "Focused"): "Use your energy to plan and structure your work.",
    ("Anxious", "Dynamic", "Creative"): "Turn restlessness into an artistic or inventive project.",
    ("Anxious", "Dynamic", "Distracted"): "Do breathing exercises to refocus.",
    
    # Calm
    ("Calm", "Productive", "Confused"): "Take time to define your priorities before acting.",
    ("Calm", "Productive", "Focused"): "This is the perfect time to work efficiently.",
    ("Calm", "Productive", "Creative"): "Use your calmness to explore new ideas.",
    ("Calm", "Productive", "Distracted"): "Make a list and proceed step by step.",
    ("Calm", "Exhausted", "Confused"): "Take a nap or meditate to clear your mind.",
    ("Calm", "Exhausted", "Focused"): "Choose a simple but satisfying task to complete.",
    ("Calm", "Exhausted", "Creative"): "Engage in relaxing and imaginative activities.",
    ("Calm", "Exhausted", "Distracted"): "Breathe, stretch, and gently refocus.",
    ("Calm", "Dynamic", "Confused"): "Plan a bit to channel your energy clearly.",
    ("Calm", "Dynamic", "Focused"): "Use your energy to complete a project methodically.",
    ("Calm", "Dynamic", "Creative"): "Explore an artistic project or a new idea.",
    ("Calm", "Dynamic", "Distracted"): "Alternate between physical activity and mental tasks to stay focused.",
    
    # Irritable
    ("Irritable", "Productive", "Confused"): "Write down your thoughts before starting to avoid impulsive decisions.",
    ("Irritable", "Productive", "Focused"): "Complete tasks you can finish quickly to relieve stress.",
    ("Irritable", "Productive", "Creative"): "Channel your irritation into creating—paint, write, or design.",
    ("Irritable", "Productive", "Distracted"): "Break tasks into pieces and alternate with short breaks.",
    ("Irritable", "Exhausted", "Confused"): "Rest or change your environment to calm down.",
    ("Irritable", "Exhausted", "Focused"): "Do a simple, rewarding task to relieve tension.",
    ("Irritable", "Exhausted", "Creative"): "Let your irritation express itself through art or music.",
    ("Irritable", "Exhausted", "Distracted"): "Breathe deeply, step away from distractions, and meditate.",
    ("Irritable", "Dynamic", "Confused"): "Organize your ideas to turn energy into positive action.",
    ("Irritable", "Dynamic", "Focused"): "Channel your energy into a constructive task.",
    ("Irritable", "Dynamic", "Creative"): "Turn irritation into creative force—write or draw.",
    ("Irritable", "Dynamic", "Distracted"): "Move, exercise, and release tension to refocus."
    }
    if not os.path.exists(file_path):
        print("No mood data found.")
        return

    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        if not rows:
            print("No mood data found.")
            return
        last_mood = rows[-1]

    emotion = last_mood["Emotion"]
    energy = last_mood["Energy"]
    mental = last_mood["Mental"]

    advice = advice_dict.get((emotion, energy, mental), "Take care of yourself today.")
    print(f"Advice based on your mood: {advice}")

