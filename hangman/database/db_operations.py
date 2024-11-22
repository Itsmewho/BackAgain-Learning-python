from pymongo import MongoClient
from dotenv import load_dotenv
from colorama import Style, Fore
import os

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["hangman"]


def create_collection(collection_name, data):
    # Create: Insert new data into a collection
    try:
        db[collection_name].insert_many(data)
        print(
            Fore.GREEN
            + f"Successfully added data to {collection_name}{Style.RESET_ALL}"
        )
    except Exception as e:
        print(
            Fore.RED + f"Error inserting into {collection_name}: {e}{Style.RESET_ALL}"
        )


def read_collection(collection_name):
    # Read: Fetch all documents from a collection
    try:
        return list(db[collection_name].find())
    except Exception as e:
        print(Fore.RED + f"Error reading from {collection_name}: {e}{Style.RESET_ALL}")
        return []


def update_score(highscore_collection, player_name, new_score):
    # Update: Updates a player's score, keeps the high score list to 5 players
    try:
        # Check if player exists in the highscore list
        player = db[highscore_collection].find_one({"name": player_name})

        if player:
            # Player exists, update the score
            result = db[highscore_collection].update_one(
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
            db[highscore_collection].insert_one(
                {"name": player_name, "score": new_score}
            )
            print(
                Fore.GREEN
                + f"Added new player {player_name} with score {new_score}{Style.RESET_ALL}"
            )

        # Keep only the top 5 high scores
        high_scores = list(db[highscore_collection].find().sort("score", -1))
        if len(high_scores) > 5:
            # Remove the player with the lowest score
            db[highscore_collection].delete_one({"_id": high_scores[-1]["_id"]})
            print(
                Fore.RED
                + "Removed the lowest score to keep top 5 high scores."
                + Style.RESET_ALL
            )

    except Exception as e:
        print(
            Fore.RED + f"Error updating score for {player_name}: {e}{Style.RESET_ALL}"
        )


def delete_from_collection(collection_name, player_name):
    # Delete: Remove a player from a collection

    try:
        result = db[collection_name].delete_one({"name": player_name})
        if result.deleted_count > 0:
            print(
                Fore.GREEN
                + f"Successfully deleted {player_name} from {collection_name}{Style.RESET_ALL}"
            )
        else:
            print(
                Fore.MAGENTA
                + f"{player_name} not found in {collection_name}{Style.RESET_ALL}"
            )
    except Exception as e:
        print(Fore.RED + f"Error deleting from {collection_name}: {e}{Style.RESET_ALL}")
