import random 

print("Number Guessing Game")

num = random.randint(1,9)
chances = 0

print("Enter a number between 1 and 9")

while chances < 5:
    guess = int(input("Enter your guess"))
    if guess == num:
        print("Congratulations!! You won!!!!")
        break
    
    elif guess < num:
        print("Your guess was too low. Guess a number greater than ", guess)
    else: 
        print("Your guess was too high. Guess a number less than ", guess)
    
    chances = chances + 1

if not chances < 5:
    print("You Lose!!! The correct number is ", num)
    
 