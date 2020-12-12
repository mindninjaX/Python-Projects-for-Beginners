import random

def guess(num):
    low = 1
    high = num
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        # guess = random.randint(low, high)
        feedback = input(f"Is it {guess}? Is it too low (L), too high (H) or its just correct (C)?").lower()
        if feedback == 'l':
            low = guess + 1
        elif feedback == 'h':
            high = guess - 1
    print(f"I got it! Its {guess}")

guess(1000)