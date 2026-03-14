import random
number=random.randint(1,10)
print("I am thinking of a number between 1 to 10")
guess=int(input("Guess The Number Between 1 to 10"))
attempt=1

while guess!=number:
    attempt+=1
    if guess>number:
        print("try lesser number")
    elif guess<number:
        print("try bigger number")
    guess=int(input("guess again(1-10)"))
if guess==number:
    print("your guess is correct")
    print("you guessed the number in ",attempt,"attempts")
