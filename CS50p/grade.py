# Assignment make a grading programe
#### a is between 100 and 90 b is between 80 and 70 so forth

score = int(input("What is you'r score?:\n"))

if score >= 90 and score <= 100:
    score = "A"
elif score <= 80:
    score = "B"
elif score <= 70:
    score = "C"
elif score <= 60:
    score = "D"
elif score <= 50:
    score = "E"
elif score <= 40:
    score = "F"
else:
    score = "you are a dumb motherfucker"

print(score)
