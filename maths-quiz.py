import random

score=0

questions=[
    ("5+7",12),
    ("56+90",146),
    ("20/5",4),
    ("769/3",256.33)
    ("9+8",17)
]
print("==== Math Quiz ====")

for question,answer in questions:
    print("\n What is",question,"?")

    user_answer =int(input("Your answer:"))

    if user_answer == answer:
        print("Correct!")
        score += 1

    else:
        print("Wrong! Correct answer:",answer)

print("\n ==== Quiz Finished ====")
print("Your Score:",score,"/",len(questions))