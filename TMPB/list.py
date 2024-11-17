# lists = ["a", "b", "c"]

# item = input("What do you want to append? : ")
# lists.append(item)

# print(lists)

# # nums = list(range(1, 100))  # Cool way to do it

# # print(nums)
# print(f"{lists[::-1]} I'm aspecting D")

# List with a while loop


# numbers = list(range(1, 10))
# item = 0

# while item < len(numbers):
#     print(numbers[item], end="")
#     item += 1

# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# result = ""

# for idx in sounds:
#     result += idx.upper()

# print(result)

# insert() append() extend() // pop() remove() // join()

# instructors = ["Colt", "Blue", "Lisa"]

# instructors.remove("Lisa")

# print(instructors)

# list = [1, 2, 3, 4]

# print(list[1:3])

# Let's have some fun

# number = [1, 2, 3, 4, 5, 6, 7, 8]

# evens = [num for num in number if num % 2 == 0]

# odd = [num for num in number if num % 2 != 0]

# print(odd)
# print(evens)

# Or you can do it this way:

# combi = [num * 2 if num % 2 == 0 else num / 2 for num in number]

# print(combi)


# whit_vowels = "This is so much fun!"

# without = (char for char in whit_vowels if char not in "aeiuo")

# print(whit_vowels)
# print("".join(without))

# answer = [
#     person[0] for person in ["Ëlie", "Tim", "Matt"]
# ]  # person has an idx of 0 and the list has 3. so for item in list print idx 0
# answer2 = [val for val in [1, 2, 3, 4, 5, 6] if val % 2 == 0]

# print(answer)
# print(answer2)


# answer = [val for val in [1, 2, 3, 4] if val in [3, 4, 5, 6]]
# print(answer)
# answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]
# print(answer2)
# answer = [num for num in range(1, 101) if num % 12 == 0]

# print(answer)

# answer = [char for char in "amazing" if char not in "aeiou"]

# print(answer)
