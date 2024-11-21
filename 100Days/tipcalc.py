from colorama import Fore, Back, Style
import time
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def typing_effect(message, delay=0.075):
    # Prints a message with a typing effect.
    for char in message:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def input_typing_effect(prompt, delay=0.075):
    # Displays a prompt with a typing effect and waits for user input.
    for char in prompt:
        print(char, end="", flush=True)
        time.sleep(delay)
    return input()


def handle_quit():
    # Handles quiting the program.
    typing_effect("Goodbye")
    time.sleep(1)
    clear()


def get_number_input(prompt):
    while True:
        typing_effect(f"{prompt}")
        user_input = input()  # Get input after the typing effect
        try:
            # Try to convert to float (handles both int and float)
            return float(user_input)
        except ValueError:
            # If ValueError occurs (input is not a number)
            typing_effect(
                "Invalid input! Please enter a valid number (integer or float).",
                delay=0.1,
            )
            time.sleep(0.3)
            clear()


def get_valid_response(prompt, valid_responses, quit_responses):
    # Gets a validated response from the user.

    while True:
        response = input_typing_effect(prompt).lower()
        if response in valid_responses:
            return response
        elif response in quit_responses:
            return "quit"
        typing_effect("Invalid response. Please try again.", delay=0.3)
        time.sleep(1)
        clear()


def main():

    program_over = False

    bill = 0
    people_to_share = 0
    percent_tip = 0

    while not program_over:

        typing_effect("Welcome to the tip calculator!")

        bill = get_number_input("What was the total bill? ")
        time.sleep(0.3)
        clear()
        percent_tip = get_number_input(
            "What is the percentage of tip you like to give? 10 15 or 20% "
        )
        time.sleep(0.3)
        clear()
        people_to_share = get_number_input("How many people to split the bill?")
        time.sleep(0.3)
        clear()

        tip = percent_tip / 100
        total_tip = bill * tip
        total_bill = bill + total_tip

        share = total_bill / people_to_share

        typing_effect(
            f"The total bill = ${total_bill} The shared amount per person = ${share}"
        )

        # Give the possibility to exit the program or run again.
        response = get_valid_response(
            "Do you want to make another calculation? (y/n) or 'q' to quit: ",
            valid_responses=["y", "n"],
            quit_responses=["q"],
        )

        if response in ["n", "quit"]:
            handle_quit()
            program_over = True
        elif response == "y":
            typing_effect("Generating a new bill...")
            time.sleep(1)
            clear()


if __name__ == "__main__":
    main()
