import sys
import random
# from enum import Enum


# class RPS(Enum):
#     ROCK = 1
#     PAPER = 2
    # SCISSORS = 3


print("")
playerchoice = input(
    "Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")

computerchoice = random.choice("123")
# choice = {"1","2","3"}
# computerchoice=choice(1)


computer = int(computerchoice)

if player==1:
    b="rock"
elif player==2:
    b="paper"
elif player==3:
    b="scissors"

if computer==1:
    a="rock"
elif computer==2:
    a="paper"
elif computer==3:
    a="scissors"

print("")
# print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
# print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
print("you choose",b)
print("python choose",a)
print("")

if player == 1 and computer == 3:
    print("🎉 You win!")
elif player == 2 and computer == 1:
    print("🎉 You win!")
elif player == 3 and computer == 2:
    print("🎉 You win!")
elif player == computer:
    print("😲 Tie game!")
else:
    print("🐍 Python wins!")
