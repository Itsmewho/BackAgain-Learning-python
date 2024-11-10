import random

# coin = random.choice(["Heads", "Tails"])

# player = input("What is your choice? \n")
# print(coin)


cards = ["Jack", "Queen", "King", "Ace"]
random.shuffle(cards)
for card in cards:
    print(card)
