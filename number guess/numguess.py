import random

print("Welcome to the number guessing game! You have to guess a number between 1 and 100.")

option = input("Choose difficulty level: 'e' for easy and 'h' for hard.\n").lower()

def easy():
    life = 10
    number = random.randint(1, 100)
    while life > 0:
        guess = int(input("Make a guess: "))
        if guess == number:
            return "You got it!"
        elif number > guess:
            if (number - guess) > 10:
                print("Too low!")
            elif (number - guess) <= 10:
                print("Low but closer!")
        elif guess > number:
            if (guess - number) > 10:
                print("Too high!")
            elif (guess - number) <= 10:
                print("High but closer!")
            
        life -= 1
        print(f"You have {life} attempts remaining.")
    
    print(f"The correct number is {number}.")
    return "Game over!"

def hard():
    life = 5
    number = random.randint(1, 100)
    while life > 0:
        guess = int(input("Make a guess: "))
        if guess == number:
            return "You got it!"
        elif number > guess:
            if (number - guess) > 10:
                print("Too low!")
            elif (number - guess) <= 10:
                print("Low but closer!")
        elif guess > number:
            if (guess - number) > 10:
                print("Too high!")
            elif (guess - number) <= 10:
                print("High but closer!")
            
        life -= 1
        print(f"You have {life} attempts remaining.")
    
    print(f"The correct number is {number}.")
    return "Game over!"


if option == 'e':
    print(easy())
elif option=='h':
    print(hard())
