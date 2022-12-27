import random

guess=random.randint(1,20)

cha = 0
while cha < 5:
    x = int(input())
    if x == guess:
        print("winner winner")
        break
    elif x < guess:
        print("you guess the less than")
    elif x > guess:
        print("you guess a greater tha number")
    cha+=1
if not cha < 5:
    print("you lose")