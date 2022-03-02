import random
number = random.randrange(0, 10)
while True:
    guess = input("Can you guess which number I'm thinking of in range of 0 to 10? ")
    if float(guess) == number:
        print("Well done!")
        break
    elif float(guess) <= number:
        print("That's too low! Try again")
    elif float(guess) >= number:
        print("That's too high! Try again!")