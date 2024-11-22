from database.db_operations import update_score, display_top_scorer, read_collection
from art.ascii_art import stages, logo
from colorama import Fore, Style
from game.utils import *


def play_hangman():

    clear()
    players_name = input_typing_effect("What is your name? : ").title()
    difficulty = get_valid_response(
        "Choose difficulty (easy gets 500 starting points,\n medium 750,\n hard gets 1000): ",
        ["easy", "medium", "hard"],
        ["quit"],
    )

    if difficulty == "quit":
        handle_quit()
        return

    # Word and hint from the database
    chosen_data = random_word(difficulty)
    word = chosen_data["word"]
    hint = chosen_data["hint"]

    # Initialize game variables
    guessed_letters = []
    tries = 6
    score = 0

    if difficulty == "easy":
        score += 500
    elif difficulty == "medium":
        score += 750
    else:
        score += 1000

    typing_effect(Fore.GREEN + f"Welcome to hangman, {players_name}!{Style.RESET_ALL}")
    typing_effect(f"You will earn 10 points for each correct letter.")
    typing_effect(Fore.RED + "You lose 20 points for each incorrect guess.")
    typing_effect(Fore.RED + "No points left? Or if you hang! Game over! 💀")
    pauze_clear()

    while tries > 0 and score > 0:
        clear()

        display_top_scorer("highscore")

        print(Fore.GREEN + f"The word has {len(word)} letters.{Style.RESET_ALL}")
        print(display_word(word, guessed_letters))
        print(stages[tries])
        user_input = input_typing_effect(
            "Enter a letter, type 'hint' for a hint, or 'life' to reveal two letters: "
        ).lower()

        if user_input == "hint":
            typing_effect(f"Hint: {hint}")
            score -= 100
        elif user_input == "life":
            give_lifeline(word, guessed_letters)
            score -= 300
        elif user_input == "quit":
            handle_quit()
        elif user_input in guessed_letters:
            typing_effect("You already guessed that letter. Try again!")
        elif user_input in word:
            guessed_letters.append(user_input)
            typing_effect(Fore.GREEN + "Correct! Keep going!" + Style.RESET_ALL)
            score += 10
        else:
            tries -= 1
            score -= 20
            typing_effect(Fore.RED + "Incorrect guess. Try again." + Style.RESET_ALL)

        if all(letter in guessed_letters for letter in word):
            typing_effect(
                Fore.GREEN
                + "Congratulations, you've guessed the word!"
                + Style.RESET_ALL
            )
            break

    # End game logic
    if tries == 0 or score <= 0:
        typing_effect(Fore.RED + f"Game over! The word was: {word}" + Style.RESET_ALL)

    # Update and compare scores
    update_score("highscore", players_name, score)
    display_top_scorer("highscore")

    # Show final results and ask for next action
    print(
        Fore.YELLOW
        + f"\n{players_name}, your final score is: {score}"
        + Style.RESET_ALL
    )
    while True:
        next_action = get_valid_response(
            "Do you want to play again (y/n) or view the top 5 high scores (view)? ",
            ["y", "n", "view"],
            ["quit"],
        )

        if next_action == "y":
            play_hangman()
            break
        elif next_action == "view":
            show_top_5_scores("highscore")
            break
        elif next_action == "quit" or "q":
            handle_quit()
        typing_effect("Invalid response. Please try again")
        pauze_clear(message=None)


def show_top_5_scores(highscores):
    # Fetch and display the top 5 high scores.
    scores = read_collection(highscores)
    scores = sorted(scores, key=lambda x: x["score"], reverse=True)[:5]

    print(Fore.BLUE + "\nTop 5 High Scores:\n" + Style.RESET_ALL)
    for i, score in enumerate(scores, 1):
        print(f"{i}. {score['name']} - {score['score']} points")

    # Loop for next action after showing the top scores
    while True:
        next_action = get_valid_response(
            "Do you want to play again (y/n) or quit? ",
            ["y", "n"],
            ["quit"],
        )
        clear()

        if next_action == "y":
            play_hangman()
            break
        elif next_action == "n" or next_action == "quit":
            handle_quit()
            break
        else:
            typing_effect("Invalid response. Please try again.")
            pauze_clear(message=None)


def main():

    clear()
    typing_effect(Fore.GREEN + "Welcome to Hangman!" + Style.RESET_ALL)
    print(logo)
    typing_effect(
        Fore.BLUE + "\nType 'quit' to exit the game at any time." + Style.RESET_ALL
    )

    while True:
        response = input_typing_effect(
            "Do you want to play? (y/n) or 'q' to quit: "
        ).lower()
        if response == "y":
            play_hangman()
        elif response in ["n", "q", "quit"]:
            handle_quit()
            break
        else:
            typing_effect("Invalid response. Please enter 'y', 'n', or 'q'.")
            clear()


if __name__ == "__main__":
    main()
