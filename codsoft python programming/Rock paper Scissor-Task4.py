import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        self.title_label = tk.Label(root, text="Rock-Paper-Scissors Game", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.instructions_label = tk.Label(root, text="Choose rock, paper, or scissors:")
        self.instructions_label.pack()

        self.choice_buttons = [
            tk.Button(root, text="Rock", command=lambda: self.play_game("rock")),
            tk.Button(root, text="Paper", command=lambda: self.play_game("paper")),
            tk.Button(root, text="Scissors", command=lambda: self.play_game("scissors"))
        ]

        for button in self.choice_buttons:
            button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        self.score_label = tk.Label(root, text="")
        self.score_label.pack()

    def play_game(self, user_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            result = "You win!"
            self.user_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1

        self.result_label.config(text=f"You chose {user_choice}, Computer chose {computer_choice}\n{result}")

        self.update_score()

    def update_score(self):
        self.score_label.config(text=f"Your Score: {self.user_score} | Computer Score: {self.computer_score}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()
