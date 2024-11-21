# Make a tressure eiland.
# Its a sequential game.
# Make the options for the player random. (random.range(1,3)? )
# Try to hold the style of the boiler plate.
# Give it let's say 2 options 6random questions. possible ways to experience the game).
# Lives === 3

import time
import os
import random

# Question dict:
questions = {
    "question_one": {
        "text": "You are at a crossroad, where do you wanna go? \n(left or right) ",
        "answer": "left",
    },
    "question_two": {
        "text": "A pirate asks you: 'You need to go right to find the treasure!' \nWhere do you go? (left or right) ",
        "answer": "left",
    },
    "question_three": {
        "text": "If you have 25 items and multiply them by 3, how many items do you have? (Enter a number) ",
        "answer": "75",
    },
    "question_four": {
        "text": "You have 100 coins. If you remove 50 and add 10, how many do you have now? (Enter a number) ",
        "answer": "60",
    },
    "question_five": {
        "text": "Do you want to have the treasure? (yes or no) ",
        "answer": "yes",
    },
    "question_six": {
        "text": "Do you want to swim across the ocean? (yes or no) ",
        "answer": "no",
    },
}

# Boiler plate ->


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause_and_clear(delay=0.35, preserve_message=None, typing_delay=0.075):
    time.sleep(delay)
    clear()
    if preserve_message:
        for char in preserve_message:
            print(char, end="", flush=True)
            time.sleep(typing_delay)
        print()


def handle_quit():
    # Game ending message
    typing_effect("Till next time! My old treasure hunter!")
    pause_and_clear(preserve_message=None)


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
        pause_and_clear(preserve_message=None)


def main():

    player_lives = 3
    game_over = False

    typing_effect("Let's find the treasure!")
    pause_and_clear(preserve_message=None)

    typing_effect("Rules of the game: Get the questions right! \nYou got 3 lives.")
    pause_and_clear(delay=1.25, preserve_message=None)

    while not game_over:

        # Checking if player wants to play
        while True:
            response = input_typing_effect(
                "Do you want to play? (y/n) or 'q' to quit: "
            ).lower()
            if response in ["y"]:
                break
            elif response == "n" or response == "q":
                typing_effect("Goodbye, treasure hunter!")
                time.sleep(0.5)
                clear()
                game_over = True
                break
            else:
                typing_effect("Invalid response. Please enter 'y', 'n', or 'q'.")
                pause_and_clear(preserve_message=None)

        if game_over:
            break

        typing_effect("Lets play!")
        pause_and_clear(preserve_message=None)

        player_name = input_typing_effect("What's my treasure hunters name?\n").title()
        # Keeps name and score on terminal.

        pause_and_clear(
            preserve_message=f"{player_name} you have {player_lives} lives left!"
        )

        # Convert the dict to a list for random:
        question_list = list(questions.keys())

        # Main game logic:
        while question_list or player_lives != 0:

            if not question_list:
                break  # For if the list is empty.

            question_key = random.choice(question_list)  # Pick a random question key
            question_data = questions[question_key]  # Get the question details
            question_text = question_data["text"]
            correct_answer = question_data["answer"]

            typing_effect(question_text)
            user_answer = input_typing_effect("Your answer: ").strip().lower()
            if user_answer == correct_answer.lower():
                typing_effect("That's right continue 🎉")
                question_list.remove(question_key)
                pause_and_clear(
                    preserve_message=f"{player_name} has {player_lives} lives left!"
                )
            else:
                typing_effect("Wrong you have lost a live")
                player_lives -= 1
                pause_and_clear(
                    preserve_message=f"{player_name} has {player_lives} lives left!"
                )

        if player_lives != 0:
            typing_effect("You have found the treasure 🎉🎉🎉")
            pause_and_clear(delay=2, preserve_message=None)
            response = get_valid_response(
                "Do you want to make another treasure hunt? (y/n) or 'q' to quit: ",
                valid_response=["y", "n"],
                quit_response=["q"],
            )

            if response in ["n", "quit"]:
                handle_quit()
                game_over = True
            elif response == "y":
                typing_effect("Generating a new treasure hunt")
                pause_and_clear(delay=1, preserve_message=None)
        else:
            typing_effect("You are dead 💀💀💀")
            pause_and_clear(delay=2, preserve_message=None)
            response = get_valid_response(
                "Do you want to make another treasure hunt? (y/n) or 'q' to quit: ",
                valid_response=["y", "n"],
                quit_response=["q"],
            )

            if response in ["n", "quit"]:
                handle_quit()
                game_over = True
            elif response == "y":
                typing_effect("Generating a new treasure hunt")
                pause_and_clear(delay=1, preserve_message=None)


if __name__ == "__main__":
    main()
