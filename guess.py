import random

#Generating a random number
number = random.randint(1, 35)
print('Guess a number between 1 and 35.')

#Taking user's input as guess
guess = input()
#Converting guess to int
guess = int(guess)

if guess < number:
    print('Your guess is too low.')
if guess > number:
    print('Your guess is too high.')
if guess == number:
    print('Good job, You guessed the right number!')
if guess != number:
    number = str(number)
    print('The random number was ' + number)
