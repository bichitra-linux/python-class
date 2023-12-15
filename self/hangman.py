import tkinter as tk
from tkinter import messagebox

# Define the Hangman game class
class HangmanGame:
    def __init__(self, word):
        self.word = word
        self.guesses = []
        self.remaining_attempts = 6

    def guess_letter(self, letter):
        self.guesses.append(letter)
        if letter not in self.word:
            self.remaining_attempts -= 1

    def is_game_over(self):
        return self.remaining_attempts == 0 or self.is_word_guessed()

    def is_word_guessed(self):
        return all(letter in self.guesses for letter in self.word)

# Create the GUI window
window = tk.Tk()
window.title("Hangman Game")

# Create the hangman game instance
hangman_game = HangmanGame("python")

# Create the GUI elements
word_label = tk.Label(window, text="_ " * len(hangman_game.word))
word_label.pack()

input_entry = tk.Entry(window)
input_entry.pack()

def guess_letter():
    letter = input_entry.get()
    hangman_game.guess_letter(letter)
    word_label.config(text=" ".join(letter if letter in hangman_game.guesses else "_ " for letter in hangman_game.word))
    input_entry.delete(0, tk.END)

    if hangman_game.is_game_over():
        messagebox.showinfo("Game Over", "You lost!")

guess_button = tk.Button(window, text="Guess", command=guess_letter)
guess_button.pack()

# Start the GUI event loop
window.mainloop()
