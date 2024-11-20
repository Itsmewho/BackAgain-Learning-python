import random


# artist = {
#     "first": "Neil",
#     "last": "Young",
# }

# full_name = artist["first"] + " " + artist["last"]

# print(full_name)

# Accessing data from a dict.

# instructor = {
#     "name": "ItsMe",
#     "owns_dog": "False",
#     "num_curs": "2",
#     "code": "python",
#     "humor": None,
#     "poept": "graag",
#     "items": [1, 2, 3, 4, 5, 6],
# }

# # For looping over the values:

# for v in instructor.values():
#     print(v)

# # For the keys:
# for key in instructor.keys():
#     print(key)

# # for both: remember it will return a tuple
# for item in instructor.items():
#     print(item)

# # different way to do so:

# for k, v in instructor.items():
#     print(k, v)

# donations = dict(
#     sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0
# )
# totaldon = sum(donations.values())

# food = random.choice(
#     ["cheese pizza", "quiche", "morning bun", "gummy bear", "tea cake"]
# )

# bakery_stock = {
#     "almond croissant": 12,
#     "toffee cookie": 3,
#     "morning bun": 1,
#     "chocolate chunk cookie": 9,
#     "tea cake": 25,
# }

# qty = bakery_stock.get(food)
# if qty:
#     print(f"{qty} left")
# else:
#     print("we dont make that")

# game_properties = [
#     "current_score",
#     "high_score",
#     "number_of_lives",
#     "items_in_inventory",
#     "power_ups",
#     "ammo",
#     "enemies_on_screen",
#     "enemy_kills",
#     "enemy_kill_streaks",
#     "minutes_played",
#     "notifications",
#     "achievements",
# ]
# initial_game_state = dict.fromkeys(game_properties, 0)

# print(initial_game_state)

# inventory = {"croissant": 19, "bagel": 4, "muffin": 8, "cake": 1}

# stock_list = inventory.copy()
# stock_list["cookie"] = 18  # no addition needed for aading to a dict.
# stock_list.pop(
#     "cake"
# )  # pop is not the same as pop with a list you need to specify the item that you wanna pop.

# print(stock_list)


# instructor = {
#     "name": "ItsMe",
#     "owns_dog": "False",
#     "num_curs": "2",
#     "code": "python",
#     "poept": "graag",
# }

# y_instuctor = {
#     k.upper(): v.upper() for k, v in instructor.items()
# }  # Only works if there is no list in de the dict.

# print(y_instuctor)


# num_list = [1, 2, 3, 4, 5, 6]

# bull = {num: ("even" if num % 2 == 0 else "odd") for num in range(1, 100)}

# print(bull)

# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]

# answer = {list1[i]: list2[i] for i in range(0, 3)}


# print(answer)
