import random

choices=[1,2,3]
names={1:"snake",2:"water",3:"gun"}

while True:

    comp=random.choice(choices)

    p=int(input("enter 1 for snake,2 for water,3 for gun: "))

    print("you chose",names[p])
    print("computer chose",names[comp])

    match p:
      case 1:
        if comp==1:
          print("draw")
        elif comp==2:
          print("you win")
        else:
          print("you lose")

      case 2:
        if comp==1:
          print("you lose")
        elif comp==2:
          print("draw")
        else:
          print("you win")

      case 3:
        if comp==1:
          print("you win")
        elif comp==2:
          print("you lose")
        else:
          print("draw")

      case _:
        print("invalid input")

    print("do you want to play again?")
    choice=input("enter yes or no: ")

    if choice=="no":
        print("game over")
        break