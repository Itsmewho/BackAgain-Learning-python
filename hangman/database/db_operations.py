from pymongo import MongoClient
from dotenv import load_dotenv
from colorama import Style, Fore
import os

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["hangman"]


def read_collection(collection_name):
    # Read: Fetch all documents from a collection
    try:
        return list(db[collection_name].find())
    except Exception as e:
        print(Fore.RED + f"Error reading from {collection_name}: {e}{Style.RESET_ALL}")
        return []


def update_score(highscore, player_name, new_score):
    # Update: Updates a player's score, keeps the high score list to 5 players
    try:
        # Check if player exists in the highscore list
        player = db[highscore].find_one({"name": player_name})

        if player:
            # Player exists, update the score
            result = db[highscore].update_one(
                {"name": player_name}, {"$set": {"score": new_score}}
            )
            if result.modified_count > 0:
                print(
                    Fore.GREEN
                    + f"Successfully updated score for {player_name}{Style.RESET_ALL}"
                )
            else:
                print(
                    Fore.MAGENTA
                    + f"No update needed for {player_name}{Style.RESET_ALL}"
                )
        else:
            # Player does not exist, add to the highscore collection
            db[highscore].insert_one({"name": player_name, "score": new_score})
            print(
                Fore.GREEN
                + f"Added new player {player_name} with score {new_score}{Style.RESET_ALL}"
            )

        # Keep only the top 5 high scores
        high_scores = list(db[highscore].find().sort("score", -1))
        if len(high_scores) > 5:
            # Remove the player with the lowest score
            db[highscore].delete_one({"_id": high_scores[-1]["_id"]})
            print(
                Fore.RED
                + "Removed the lowest score to keep top 5 high scores."
                + Style.RESET_ALL
            )

    except Exception as e:
        print(
            Fore.RED + f"Error updating score for {player_name}: {e}{Style.RESET_ALL}"
        )


def get_top_score(highscore):
    try:
        top_player = db[highscore].find_one(sort=[("score", -1)])
        return top_player
    except Exception as e:
        print(Fore.RED + f"Error fetching top score: {e}{Style.RESET_ALL}")
        return None


def display_top_scorer(highscore):
    # Fetch and display the player with the highest score.

    try:
        # Query the database for the player with the highest score
        top_scorer = db[highscore].find_one(sort=[("score", -1)])

        if top_scorer:
            print(
                Fore.CYAN
                + f"🏆 Top Scorer: {top_scorer['name']} with {top_scorer['score']} points! 🏆"
                + Style.RESET_ALL
            )
        else:
            print(Fore.YELLOW + "No top scorer yet!" + Style.RESET_ALL)
    except Exception as e:
        print(
            Fore.RED
            + f"Error fetching top scorer from {highscore}: {e}{Style.RESET_ALL}"
        )
