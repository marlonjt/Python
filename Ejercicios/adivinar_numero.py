import random

random_number = random.randint(1, 9)
attempts = 0
number = int(input("Enter a number from 1 to 9: "))

while True:
    if number == random_number:
        print(f"You guessed a number!!")
        break
    elif number > random_number:
        print(f"Oops, the number is greater than the random number!!")
    elif number < random_number:
        print(f"Oops, the number is less than the random number!!")

    txt = input("terminar juego? S/N ")
    if txt.lower() == "s":
        print(f"Thank for playing")
        break
    elif txt.lower() == "n":
        number = int(input("Enter a number again: "))
        attempts += 1
        if attempts == 3:
            print(f"Thank for playing, max attempts. Answer: {random_number}")
            break
