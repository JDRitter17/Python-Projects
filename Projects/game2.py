import random

def guessing_game():
    num = random.randint(1, 100)
    count = 0
    guesses = []
    max_attempts = 6

    while count < max_attempts:
        try:
            guess = int(input(f"Guess a number 1-100 (Attempt {count + 1} of {max_attempts}): "))
            if guess < 1 or guess > 100:
                print("Please guess a number within 1 to 100.")
                continue
            guesses.append(guess)

            if guess < num:
                count += 1
                print("No. Guess higher.")

            elif guess > num:
                count += 1
                print("No. Guess lower.")

            else:
                if count == 0:
                    print("Correct! First Try!")
                else:
                    print(f"Correct! It took you {count + 1} tries!")
                print(f"Here are all of your guesses: {guesses}")
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

    else:
        print(f"You've used all {max_attempts} tries! The number was {num}. Better luck next time!")

while True:
    guessing_game()
    replay = input("Play again? (y/n): ").lower()
    if replay != 'y':
        print("Thanks for playing!")
        break
