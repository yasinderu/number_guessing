from random import randint

lower_num, higher_num = 1, 10
random_num: int = randint(lower_num, higher_num)

print(f"Guess the number in the range from {lower_num} to {higher_num}.")

count = 0

while count < 3:
    try:
        user_guess: int = int(input("Guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    count+=1

    if user_guess > random_num:
        print("The number is lower")
    elif user_guess < random_num:
        print("The number is higher")
    else:
        print("You guess it right!")
        break

    if count == 3:
        print("You have guessed three times, better luck next time.")
    else:
        print(f"you can guess {3 - count} time(s)")