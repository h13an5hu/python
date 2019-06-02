import random

print("rule: \npress enter when your chance....\n")
player1 = input("player1 enter your name: ")
player2 = input("player2 enter your name: ")
input2 = int(input("\npress 1 for play sequancially and 2 for know winner directly: "))
input3 = int(input("enter the range from 1 to '?' to play game: "))

while True:
     lucky_number = int(input(f"okay, now choose lucky number between '1 to {input3}': "))
     if lucky_number > input3:
          print(f"lucky number is out of range.......choose again")
     else:

          break
          
chance = random.randint(1, 2)
if input2 == 1:
          print(f"\ntossing: ..........and player{chance} won the toss so it's, ", end="")

while True:
    roll = random.randrange(1, input3 +1)
    if input2 == 1:
        print(f"player{chance}'s chance: ",end="")
        input1 = input("> ")
        print(f"you got: {roll}....try again")
    if roll == lucky_number:
        if chance == 1:
            print(f"          yeahh, {player1} won!")
        else:
            print(f"          yeahh, {player2} won!")
        break
    else:
        if chance == 1:
            chance = 2
        else:
            chance = 1
