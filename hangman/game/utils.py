from database.db_operations import read_collection
import time
import os
import random


def clear():
    time.sleep(0.35)
    os.system("cls" if os.name == "nt" else "clear")


def handle_quit():
    typing_effect("Goodbye, thanks for playing Hangman! 🏴‍☠️")
    pauze_clear(message=None)
    exit()


def typing_effect(message, delay=0.035):

    for char in message:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def input_typing_effect(prompt, delay=0.035):
    for char in prompt:
        print(char, end="", flush=True)
        time.sleep(delay)
    user_input = input().strip().lower()

    if user_input == "quit":
        handle_quit()  # Call the quit handler if the user types "quit"

    return user_input  # Return the input for other uses


def pauze_clear(delay=0.35, message=None, typing_delay=0.075):
    time.sleep(delay)
    clear()
    if message:
        for char in message:
            print(char, end="", flush=True)
            time.sleep(delay)
        print()


def get_valid_response(prompt, valid_response, quit_response):
    # Will delete this one ?
    while True:
        response = input_typing_effect(prompt).lower()
        if response in valid_response:
            return response
        elif response in quit_response:
            return "quit"
        typing_effect("Invalid response. Please try again")
        pauze_clear(message=None)


def validate_input():

    while True:
        user_input = input_typing_effect(
            "Enter a letter! type 'hint' for a hint (costing 100points)\ntype 'life' for adding 2 letters to the word (costs 300points) \n  : "
        ).lower()
        if len(user_input) == 1 and user_input.isalpha():
            return user_input
        elif user_input == "hint" or user_input == "life":
            return user_input
        else:
            typing_effect(
                "Invalid input! Please enter a single letter from the Latin alphabet."
            )


def random_word(difficulty=None):
    words = read_collection(difficulty)
    return random.choice(words)


def give_lifeline(word, guessed_letters):
    # Reveals two random letters from the word that haven't been guessed yet.
    unrevealed_letters = [letter for letter in word if letter not in guessed_letters]
    if len(unrevealed_letters) <= 2:
        # If fewer than 2 letters remain, reveal all of them
        guessed_letters.extend(unrevealed_letters)
    else:
        # Randomly select 2 letters to reveal
        lifeline_letters = random.sample(unrevealed_letters, 2)
        guessed_letters.extend(lifeline_letters)

    print("Lifeline used!")


def display_word(word, guessed_letters):

    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display
