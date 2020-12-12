import random

def guess(num):
    random_number = random.randint(1, num)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess the number between 1 & {num}: "))
        if guess < random_number:
            print("Wrong! Too low...")
        elif guess > random_number:
            print("Wrong! Too high...")
    print(f"Thats Right! Random number is {random_number}")

guess(10)