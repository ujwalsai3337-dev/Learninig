import random

def guess_the_number():
    number = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == number:
        print("🎉 You got it right!")
    else:
        print(f"❌ Nope! The number was {number}")

guess_the_number()