import random
print("Welcome to the Random Guess Game!!!")

choice = int(input("Select a Level (1, 2 or 3): "))
if choice == 1:
    level = 50
elif choice == 2:
    level = 75
elif choice == 3:
    level = 100
else:
    print("Invalid level")
    exit()

guess_number = random.randint(1, level)
print(f"Welcome to Level {choice} of this Random Guess Game! Guess a number between 1 and {level}")
i = 1
while i < 6:
    user_guess = int(input("Enter a Guess Number: "))
    if user_guess == guess_number:
        print("Congratulations you have WON!")
        break
    else:
        if user_guess > guess_number:
            print("Too High, Try Again")
        else:
            print("Too Low, Try Again")
    i += 1
print("Game Ends")