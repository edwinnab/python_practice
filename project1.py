#imports random module
import random
#generates random number using the random method
num = random.randint(0,35)
print("randomly generated number:",num)
#inputs a number from the user
num1 = input("Guess a number:");
num1 = int()
#loop for wrong input
if num1 > 35 :
    print("number guessed is too high.")
elif num1 < 0 :
    print("number guessed is too low.")
else :
    print("start")
