# loops and loops -> Don't make infinite loops.

# count = 3
# while count > 0:
#     print("meow")
#     count = count - 1

# print("Let's C\n" * 3, end="")
# # with the "end"- param you do not skit a line or have a space on the end.


count = int(input("Give me a number between 0 and 50: \n"))
if 0 < count <= 50:
    for _ in range(count):
        print("meow")
else:
    print("You have not given me the right number", end="")
