# Make a tressure eiland.
# Its a sequential game.
# Make the options for the player random. (random.range(1,3)? )
# Try to hold the style of the boiler plate.
# Give it let's say 2 options 3 random follow ups and again 3random. total of 18? possible ways to experience and 3 outcomes (ugly, beautiful, goat).
# Lives === 3

import time
import os
import random


# Boiler plate ->


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def handle_quit():
    # Game ending message
    typing_effect("Till next time! My old treasure hunter!")
    time.sleep(1)
    clear()


def typing_effect(message, delay=0.075):
    # Prints in typing effect
    for char in message:
        print(char, end="", flush=True)
        time.sleep(delay)
    print


def input_typing_effect(prompt, delay=0.075):
    # Gets input from user and using the typewriter effect
    for char in prompt:
        print(char, end="", flush=True)
        time.sleep(delay)
    return input()


def get_valid_response(prompt, valid_response, quit_response):
    # Check if there is a good response else -> message and run again.
    # May delete this later?!
    while True:
        response = input_typing_effect(prompt).lower()
        if response in valid_response:
            return response
        elif response in quit_response:
            return "quit"
        typing_effect("Invalid response. Please try again.", delay=0.3)
        time.sleep(1)
        clear()


def get_number_input(prompt):
    # Needed for if the answer to a question is a number.
    while True:
        typing_effect(f"{prompt}")
        user_input = input()
        try:
            return float(user_input)
        except ValueError:
            typing_effect(
                "Invalid input! Please enter a valid number (integer or float).",
                delay=0.1,
            )
            time.sleep(0.3)
            clear()


def get_player_choice():
    """Checks yes or no questions.
    Easer to do the number checking and sting checking sapperate.
    This is more bug / stupid proof at the moment.
    (till i find another way to this in one function)
    """
    while True:
        choice = input_typing_effect("What do you choose? ").lower()
        if choice in [""]