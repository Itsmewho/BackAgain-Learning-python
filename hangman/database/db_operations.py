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


def update_score(collection_name, player_name, new_score):
    # Update: Update a player's score

    try:
        result = db[collection_name].update_one(
            {"name": player_name}, {"$set": {"score": new_score}}, upsert=True
        )
        if result.modified_count > 0:
            print(
                Fore.GREEN
                + f"Successfully updated score for {player_name}{Style.RESET_ALL}"
            )
        else:
            print(Fore.MAGENTA + f"No update needed for {player_name}{Style.RESET_ALL}")
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
