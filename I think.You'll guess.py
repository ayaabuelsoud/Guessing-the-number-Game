'''
 I think.You'll guess.
 This is a guess the number game.
 I think of the number, and let the user guess it.
'''
import random

# User's name
print("Hello! What is your name?")
username = input()

#the range of numbers to guess from
print(username +" ,tell me the range of numbers to think from")
low = int(input("the minimum is: "))
high = int(input("the maximum is: "))

#chooseing a number by random
SecretNumber = random.randint(low,high)

#starting the game
print(username + ",Now I am thinking of a number between " +
        str(low) + " and " + str(high)+"\n can you guess it?")

print("Remember, you have only 5 attempt")
guessCounter = 0
for guessCounter in range(1, 5):
    print("take guess :")
    guess = int(input())

    if guess < SecretNumber:
        print("Your guess is too low.")

    elif guess > SecretNumber:
        print('Your guess is too high.')
        
    else: break   #This is for a correct guess
    
if guess == SecretNumber:
    print("Good job, "+ username + "! You guessed my number in " +
          str(guessCounter)+ " guesses!")
else:
    print("Nope. The number I was thinking of was " + str(SecretNumber))
    
