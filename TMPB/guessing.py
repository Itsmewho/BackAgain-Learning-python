import random
import time
import os


def clear():
    """Clears the console."""
    os.system("cls" if os.name == "nt" else "clear")


def typing_effect(message, delay=0.1):
    """Prints a message with a typing effect."""
    for char in message:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def input_with_typing_effect(prompt, delay=0.1):
    """Displays a prompt with a typing effect and waits for user input."""
    for char in prompt:
        print(char, end="", flush=True)
        time.sleep(delay)
    return input()


def get_player_choice():
    """Gets and validates the player's choice."""
    while True:
        try:
            choice = input_with_typing_effect("Guess a number (1-10) or 'q' to quit: ")
            if choice.lower() == "q":
                return "quit"
            choice = int(choice)
            if 1 <= choice <= 10:
                return choice
            print("Invalid choice. Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")


def game_result(player, ai):
    """Determines the game result based on the player and AI's choices."""
    return "You won!" if player == ai else "Wrong!"


def main():
    game_over = False

    typing_effect("Guessing Game")
    time.sleep(0.3)
    clear()

    while not game_over:
        response = input_with_typing_effect(
            "Do you want to play? (y/n) or 'q' to quit: "
        ).lower()
        if response in ["n", "q"]:
            typing_effect("Goodbye!")
            game_over = True
            break
        elif response != "y":
            print("Invalid response. Please enter 'y', 'n', or 'q'.")
            continue

        ai_number = random.randint(1, 10)  # Generate a new number each round
        player_choice = get_player_choice()
        if player_choice == "quit":
            typing_effect("Goodbye!")
            game_over = True
            break

        typing_effect(f"Computer chose: {ai_number}")
        typing_effect(f"Player chose: {player_choice}")
        time.sleep(1)
        clear()

        result = game_result(player_choice, ai_number)
        typing_effect(result)
        time.sleep(0.5)
        clear()


if __name__ == "__main__":
    main()
