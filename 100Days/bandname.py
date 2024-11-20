import time
import os


def clear():
    # Clears the console.
    os.system("cls" if os.name == "nt" else "clear")


def typing_effect(message, delay=0.08):
    # Prints a message with a typing effect.
    for char in message:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def input_with_typing_effect(prompt, delay=0.08):
    # Displays a prompt with a typing effect and waits for user input.
    for char in prompt:
        print(char, end="", flush=True)
        time.sleep(delay)
    return input()


def handle_quit():
    # Handles quitting the game.
    typing_effect("Goodbye!")
    time.sleep(1)
    clear()


def get_valid_response(prompt, valid_responses, quit_responses):
    # Gets a validated response from the user.

    while True:
        response = input_with_typing_effect(prompt).lower()
        if response in valid_responses:
            return response
        elif response in quit_responses:
            return "quit"
        typing_effect("Invalid response. Please try again.")
        time.sleep(1)
        clear()


def main():

    game_over = False
    wrong_input = False

    while not game_over:

        typing_effect("Welcome to the Band Name Genarator!")
        time.sleep(0.3)
        clear()

        players_city = input_with_typing_effect(
            "What's the city you grew up in? \n"
        ).title()
        time.sleep(0.3)
        clear()

        players_name = input_with_typing_effect("What's your pet's name? \n").title()
        time.sleep(0.3)
        clear()

        typing_effect(f"Your band name could be {players_city}  {players_name} ")

        # Give the possibility to exit the program or run again.
        while not wrong_input:
            response = get_valid_response(
                "Do you want to make another band name? (y/n) or 'q' to quit: ",
                valid_responses=["y", "n"],
                quit_responses=["q"],
            )

        if response in ["n", "quit"]:
            handle_quit()
            game_over = True
        elif response == "y":
            # Logic for generating another band name goes here
            typing_effect("Generating another band name...")
            time.sleep(1)
            clear()


if __name__ == "__main__":
    main()
