import tkinter as tk
import random

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("600x400")
root.configure(bg="white")

user_choice = ""
computer_choice = ""
result = ""
start_screen = True

WHITE = "white"
BLUE = "#0078D7"
BLACK = "black"
GREEN = "#00C800"
RED = "#C80000"
PLUM="plum"
CRIMSON="crimson"

result_label = tk.Label(root, text="", font=("Arial", 16), bg=WHITE)
result_label.place(x=250, y=270)

user_label = tk.Label(root, text="", font=("Arial", 14), bg=WHITE)
comp_label = tk.Label(root, text="", font=("Arial", 14), bg=WHITE)

user_label.place(x=50, y=300)
comp_label.place(x=50, y=330)

def get_result(user, comp):
    if user == comp:
        return "Draw"
    elif (user == "Rock" and comp == "Scissors") or \
         (user == "Paper" and comp == "Rock") or \
         (user == "Scissors" and comp == "Paper"):
        return "You Win!"
    else:
        return "You Lose!"

def start_game():
    global start_screen
    start_screen = False
    start_button.place_forget()
    rock_button.place(x=50, y=150)
    paper_button.place(x=225, y=150)
    scissors_button.place(x=400, y=150)

def play(choice):
    global user_choice, computer_choice, result
    user_choice = choice
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = get_result(user_choice, computer_choice)

    user_label.config(text=f"You: {user_choice}")
    comp_label.config(text=f"Computer: {computer_choice}")
    result_label.config(
        text=result,
        fg=RED if "Lose" in result else "orange"
    )

start_button = tk.Button(root, text="START", font=("Arial", 20), bg=BLUE, fg=WHITE, command=start_game)
start_button.place(x=200, y=150, width=200, height=80)


rock_button = tk.Button(root, text="Rock", font=("Arial", 16), bg="orange", fg=BLACK, command=lambda: play("Rock"))
paper_button = tk.Button(root, text="Paper", font=("Arial", 16), bg="orange", fg=BLACK, command=lambda: play("Paper"))
scissors_button = tk.Button(root, text="Scissors", font=("Arial", 16), bg="orange", fg=BLACK, command=lambda: play("Scissors"))

root.mainloop()