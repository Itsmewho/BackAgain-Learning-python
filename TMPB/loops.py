# for _ in range(5, 10):
#     print(_)

# for _ in range(8, 0, -2):
#     print(_)
# x = 0
# for n in range(10, 21):
#     if n % 2 != 0:
#         x += n

# print(x)

for num in range(1, 21):
    if num == 4 or num == 13:
        print(f"{num} is unlucky")
    elif num % 2 == 0:
        print(f"{num} is even")
    else:
        print("Thats odd")

# A more elegant solution:

for num in range(1, 21):
    if num == 4 or num == 13:
        state = "unlucky"
    elif num % 2 == 0:
        state = "even"
    else:
        state = "odd"
    print(f"{num} is {state}")
