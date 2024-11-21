import random


question_one = "You are at a crossroad, where do you wanna go? \n (left or right)"
question_two = "A pirate ask you; You need to go right to find the tressure! \n Where do you go? (left or right?)"
question_three = "If you have 25 items and multiply then 3 time's. How many items do you have? (Enter a number)"
question_four = "You have 100coins. If you remove 50 and add 10. How many do you have now? (Enter a number)"
question_five = "Do you want to have the treasure? "
question_six = "Do you want to swim across the ocean?"

question_list = [
    question_one,
    question_two,
    question_three,
    question_four,
    question_five,
    question_six,
]
print(len(question_list))


while len(question_list) != 0:
    question = random.choice(question_list)
    print(question)
    question_list.remove(question)
    print(len(question_list))
