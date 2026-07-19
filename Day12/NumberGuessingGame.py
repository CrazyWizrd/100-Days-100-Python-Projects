import art
import random
print(art.logo)
print("Welcome to Number Guessing Game!!\nI'm thinking of a Number between 1 and 100.")
random_number = random.randint(1,100)
difficulty = input("Choose your Difficulty. Type 'easy' or 'hard': ").lower()
attempts = 0
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
game_over = False
while not game_over:
    print(f"You have {attempts} attempts left")
    if attempts > 0:
        guess = int(input("Make a guess: "))
        if guess != random_number:
            if guess > random_number:
                print("Too High!")
            elif guess < random_number:
                print("Too Low!")
            attempts -= 1
        elif guess == random_number:
            print(f"You got it!! The answer was {random_number}")
            game_over = True
    elif attempts == 0:
        print("You run out of Guesses! You Lost!!")
        game_over = True
