'''
 You Think. I'll guess.
 This is a guess the number game.
 the user can think of a number and this program can guess it.
'''
#User's name
print("Hello! What is your name?")
username = input()

#the range of numbers to guess from
print(username + " ,Please Think of a number, and i will guess it")
print("Now, Tell me the range of numbers to guess from")
low = int(input("the minimum is: "))
high = int(input("the maximum is: "))

#Bisection Algorithm
medium =(low + high)//2
state = True

while state :
    print("Is your secret number is " + str(medium)+ "?!")
    guess = input("Enter 'H' if it was too high./nEnter 'l' if it was too low./n Enter'c' if it was correct :")
    if guess =='c' :
        print("Game over, your secrert number is "+ str(medium))
        state = False
    elif guess =='h' :
        high = medium
        medium =(low + high)//2

    elif guess == 'l' :
        low = medium
        medium =(low + high)//2
    else :
        print("Sorry, i can't understand you.")
        
