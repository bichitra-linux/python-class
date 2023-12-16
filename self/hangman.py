import tkinter as tk
from tkinter import messagebox
from collections import Counter

# Define the Hangman game class
class HangmanGame:
    def __init__(self, word, difficulty="medium"):
        self.word = word
        self.guesses = []
        self.difficulty = difficulty
        self.remaining_attempts = {"easy": 9, "medium": 6, "hard": 3}[difficulty]
        self.letter_frequency = Counter(word)

    def guess_letter(self, letter):
        self.guesses.append(letter)
        if letter not in self.word:
            self.remaining_attempts -= 1

    def is_game_over(self):
        return self.remaining_attempts == 0 or self.is_word_guessed()

    def is_word_guessed(self):
        return all(letter in self.guesses for letter in self.word)

    def get_hint(self):
        known_word = [letter if letter in self.guesses else None for letter in self.word]
        possible_words = [word for word in self.word_list if len(word) == len(known_word)]
        for i, letter in enumerate(known_word):
            if letter is not None:
                possible_words = [word for word in possible_words if word[i] == letter]
        remaining_letters = [letter for word in possible_words for letter in word if letter not in self.guesses]
        return Counter(remaining_letters).most_common(1)[0][0] if remaining_letters else None


# Create the GUI window
window = tk.Tk()
window.title("Hangman Game")

# Create the hangman game instance
hangman_game = HangmanGame("python")

# Create the GUI elements
word_label = tk.Label(window, text="_ " * len(hangman_game.word))
word_label.pack()

attempts_label = tk.Label(window, text=f"Remaining attempts: {hangman_game.remaining_attempts}")
attempts_label.pack()

guessed_label = tk.Label(window, text="Guessed letters: ")  # New label for guessed letters
guessed_label.pack()

hint_button = tk.Button(window, text="Hint", command=lambda: messagebox.showinfo("Hint", f"Try guessing: {hangman_game.get_hint()}"))
hint_button.pack()

input_entry = tk.Entry(window)
input_entry.pack()

def guess_letter(event=None):
    letter = input_entry.get()
    hangman_game.guess_letter(letter)
    word_label.config(text=" ".join(letter if letter in hangman_game.guesses else "_ " for letter in hangman_game.word))
    attempts_label.config(text=f"Remaining attempts: {hangman_game.remaining_attempts}")
    guessed_label.config(text=f"Guessed letters: {', '.join(hangman_game.guesses)}")  # Update the guessed letters label
    input_entry.delete(0, tk.END)

    if hangman_game.is_game_over():
        if hangman_game.is_word_guessed():
            messagebox.showinfo("Game Over", "Congratulations, you won!")  # New win message
        else:
            messagebox.showinfo("Game Over", "You lost!")

guess_button = tk.Button(window, text="Guess", command=guess_letter)
guess_button.pack()

# Bind the enter key to the guess_letter function
window.bind('<Return>', guess_letter)

def restart_game():  # New function to restart the game
    hangman_game.__init__("python", difficulty="medium")
    word_label.config(text="_ " * len(hangman_game.word))
    attempts_label.config(text=f"Remaining attempts: {hangman_game.remaining_attempts}")
    guessed_label.config(text="Guessed letters: ")
    input_entry.delete(0, tk.END)

restart_button = tk.Button(window, text="Restart", command=restart_game)  # New restart button
restart_button.pack()

# Start the GUI event loop
window.mainloop()
