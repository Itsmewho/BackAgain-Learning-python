from database.db_operations import read_collection
import time
import os
import random


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def handle_quit():
    typing_effect("Till next time!")
    pauze_clear(message=None)


def typing_effect(message, delay=0.075):
    for char in message:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def input_typing_effect(prompt, delay=0.075):
    for char in prompt:
        print(char, end="", flush=True)
        time.sleep(delay)
    return input()


def pauze_clear(delay=0.35, message=None, typing_delay=0.075):
    if message:
        for char in message:
            print(char, end="", flush=True)
            time.sleep(delay)
        print()
    else:
        time.sleep(delay)
        clear()


def get_valid_response(prompt, valid_response, quit_response):
    # Will delete this one ?
    while True:
        response = input_typing_effect(prompt).lower()
        if response in valid_response:
            return response
        elif response in quit_response:
            return "quit"
        typing_effect("Invalid response. Please try again", delay=0.3)
        pauze_clear(message=None)


def random_word(difficulty=None):
    words = read_collection(difficulty)
    return random.choice(words)


def give_hint(word):
    return word[:2] + "_" * (len(word) - 2)


def validate_input():
    while True:
        user_input = input("Enter a letter: ").lower()
        if len(user_input) == 1 and user_input.isalpha():
            return user_input
        else:
            typing_effect(
                "Invalid input! Please enter a single letter from the Latin alphabet."
            )
