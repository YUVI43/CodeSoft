import tkinter as tk
import random

user_score = 0
computer_score = 0

def play_game(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(user_choice, computer_choice)
    if "win" in result:
        user_score += 1
    elif "win" in result:
        computer_score += 1
    update_scoreboard()
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    play_again_button.config(state=tk.NORMAL)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def update_scoreboard():
    scoreboard_label.config(text=f"User: {user_score} | Computer: {computer_score}")

def play_again():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    update_scoreboard()
    result_label.config(text="")
    play_again_button.config(state=tk.DISABLED)

# Create GUI
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")  # Set window size

# Create frames
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Create buttons
rock_button = tk.Button(frame, text="Rock", width=10, command=lambda: play_game("rock"))
rock_button.grid(row=0, column=0, padx=5, pady=5)

paper_button = tk.Button(frame, text="Paper", width=10, command=lambda: play_game("paper"))
paper_button.grid(row=0, column=1, padx=5, pady=5)

scissors_button = tk.Button(frame, text="Scissors", width=10, command=lambda: play_game("scissors"))
scissors_button.grid(row=0, column=2, padx=5, pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 12), justify="center")
result_label.pack(pady=5)

# Scoreboard label
scoreboard_label = tk.Label(root, text="User: 0 | Computer: 0", font=("Helvetica", 10))
scoreboard_label.pack()

# Play Again button
play_again_button = tk.Button(root, text="Play Again", command=play_again, state=tk.DISABLED)
play_again_button.pack(pady=5)

root.mainloop()
