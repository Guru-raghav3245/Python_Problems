import random

number = random.randrange(1, 20)
print(number)

while True:

    given = int(input("What's your guess - "))

    if given != number:
        if given < number:
            print("Too low")

        elif given > number:
            print("Too high")

    else:
        print("You got it right!!!")
        break

