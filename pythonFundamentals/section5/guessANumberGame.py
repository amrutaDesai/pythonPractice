# This is guess a number game

import random
# Ask for name
print('Hello, what is your name?')

# Take the name from console
name = input()

# Choose some random number between 1 - 20
secretNumber = random.randint(1,20)
print('Debug the secret number is '+ str(secretNumber))

# Let the player know about range of a number to guess
print('Well '+ name + ' I am thinking of a number between 1 to 20')

# Ask a player to guess the number for 6 times
for guessTaken in range(1,6):
    print('Take a guess')
    guess = int(input())
    if guess < secretNumber :
        print('Your guess is too low')
    elif guess > secretNumber :
        print('Your guess is too high')
    else:
        break # This condition id a correct guess

if guess == secretNumber :
    print('Good job ' + name + '! you guessed my number in ' + str(guessTaken) +' guess')
else:
    print('Nope ! the number I was thinking of was '+ str(secretNumber))
