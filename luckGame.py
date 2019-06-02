import random

print(""" about the game : this is two player game. in this player can select the range from 1 to as the want
then they have to select a number between 1 to that range, then computer automatically gives a number randomlly,
each player one by one. which player will get that lucky number first that will WINNER!
players can select plays game step by step and know winner directly.
rule: \npress enter when your chance....\n\n""")
player1 = input("player1 enter your name: ")
player2 = input("player2 enter your name: ")
input3 = int(input("enter the range from 1 to '?' to play game: "))

while True:
     lucky_number = int(input(f"okay, now choose lucky number between '1 to {input3}': "))
     if lucky_number > input3:
          print(f"lucky number is out of range.......choose again")
     else:
          break

input2 = int(input("\npress 1 for play sequancially and 2 for know winner directly: "))
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
