from random import randint
t=('1','2', '3', '4', '5', '6')
computer=t[randint(0,5)]
player=False
while player == False:
    player=input("Press R to roll the dice.")
    if player == "R".lower():
        if computer == "1":
            print("1")
        if computer == "2":
            print("2")
        if computer == "3":
            print("3")
        if computer == "4":
            print("4")
        if computer == "5":
            print("5")
        if computer == "6":
            print("6")
    else:
        print("Try again.")
    player=False
    computer=t[randint(0,5)]

