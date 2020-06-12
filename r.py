import random
num = random.randint(1,35)
print("Guess a number between 1 and 35")
guess = input()
guess = int()
if guess < num :
    print("too low")
if guess > num :
    print("too high")
if guess == num :
    print("nice")
if guess != num :
    print("start")
