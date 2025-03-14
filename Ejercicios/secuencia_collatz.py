# secuencia de collatz


def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


def call_collatz():
    while True:
        try:
            number = int(input("Input the number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    while number != 1:
        print(number, end=" -> ")
        number = collatz(number)
    return 1

print(call_collatz())