import tkinter as tk
import random
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x250")
        self.number = random.randint(1, 100)
        self.attempts = 0

        tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 14)).pack(pady=20)

        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        tk.Button(root, text="Submit Guess", command=self.check_guess, font=("Arial", 12)).pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            if guess < self.number:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.number:
                self.result_label.config(text="Too high! Try again.")
            else:
                messagebox.showinfo("Congratulations!", f"You guessed it in {self.attempts} attempts!")
                self.reset_game()
        except ValueError:
            self.result_label.config(text="Enter a valid number!")

    def reset_game(self):
        self.number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
