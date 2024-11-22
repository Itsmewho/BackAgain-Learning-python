import json
from colorama import Fore, Style
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

# Connect to Mongo

client = MongoClient(MONGO_URI)
db = client["hangman"]


def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


easy = load_json("data/easy.json")
medium = load_json("data/medium.json")
hard = load_json("data/hard.json")
highscore = load_json("data/highscore.json")

# Insert the data collections

try:
    db["easy"].drop()
    db["easy"].insert_many(easy)

except Exception as e:
    print(Fore.RED + f"Error inserting easy words: {e}{Style.RESET_ALL}")


try:
    db["medium"].drop()
    db["medium"].insert_many(medium)

except Exception as e:
    print(Fore.RED + f"Error inserting medium words: {e}{Style.RESET_ALL}")


try:
    db["hard"].drop()
    db["hard"].insert_many(hard)

except Exception as e:
    print(Fore.RED + f"Error inserting hard words: {e}{Style.RESET_ALL}")

try:
    db["highscore"].drop()
    db["highscore"].insert_many(highscore)

except Exception as e:
    print(Fore.RED + f"Error inserting highscore words: {e}{Style.RESET_ALL}")


print(Fore.GREEN + f"Data successfully inserted! {Style.RESET_ALL}")
