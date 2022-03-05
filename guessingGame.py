import random

number = random.randint(0,9)

guesses = 0

while(guesses < 5):
    askNumber = int(input("Guess a number between 0-9: "))

    guesses += 1

    if(askNumber > number):
        print("Number is too high!")
    elif(askNumber < number):
        print("Number is too low!")
    elif(askNumber == number):
        print("You got the number!")
        break
    if(guesses == 5 and number != askNumber):
        print("The number was " + str(number))