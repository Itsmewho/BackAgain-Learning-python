import random
import time
import os


def clear():
    """Clears the console."""
    os.system("cls" if os.name == "nt" else "clear")


def print_typing_effect(message, delay=0.1):
    """Prints a message with a typing effect."""
    for char in message:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def get_player_choice():
    """Gets the player's choice, validates it, and returns it."""
    while True:
        choice = input(
            "What do you choose? (rock, paper, scissors) or 'q' to quit: "
        ).lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        elif choice == "q":
            return "quit"
        print("Invalid choice. Please try again.")


def game_result(player, ai):
    """Determines the game result based on player and AI choices."""
    if player == ai:
        return "draw"
    elif (
        (player == "rock" and ai == "scissors")
        or (player == "scissors" and ai == "paper")
        or (player == "paper" and ai == "rock")
    ):
        return "player"
    else:
        return "ai"


def main():
    ai_choices = ["rock", "paper", "scissors"]
    player_score = 0
    ai_score = 0
    game_over = False

    print_typing_effect("Let's play Rock, Paper, Scissors!")
    time.sleep(0.3)
    clear()

    print_typing_effect("Best of 3")
    time.sleep(0.5)
    clear()

    player_name = input("What is your name? : ").title()
    clear()

    while not game_over:
        # Ask if the player wants to play
        while True:
            response = input("Do you want to play? (y/n) or 'q' to quit: ").lower()
            if response in ["y", "n", "q"]:
                break
            print("Invalid response. Please enter 'y', 'n', or 'q'.")

        if response == "n" or response == "q":
            print_typing_effect("Goodbye!")
            game_over = True
            break

        player_choice = get_player_choice()
        if player_choice == "quit":
            print_typing_effect("Goodbye!")
            game_over = True
            break

        ai_choice = random.choice(ai_choices)
        print(f"Computer chose: {ai_choice}")
        print(f"{player_name} chose: {player_choice}")
        time.sleep(2)
        clear()

        # Determine the winner
        result = game_result(player_choice, ai_choice)
        if result == "draw":
            print("It's a draw!")
        elif result == "player":
            print(f"{player_name} wins this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            ai_score += 1

        # Display scores
        print(f"Scores -> {player_name}: {player_score}, Computer: {ai_score}")
        time.sleep(1.5)
        clear()

        # Check if someone has won Best of 3
        if player_score == 2:
            print(f"Congratulations {player_name}! You won the game!")
            game_over = True
        elif ai_score == 2:
            print("Computer wins the game! Better luck next time.")
            game_over = True


if __name__ == "__main__":
    main()
