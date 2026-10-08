import random

print ("hello\n")
print("1.Rock, 2.Paper, or 3.Scissors?")

choice = int(input())
botChoice = random.randint(1,3)
#Rock = 1 
#Paper = 2
#Scissors = 3 


if botChoice == choice:
    print("TIE")

match choice:
    case 1:
        if botChoice == 2: 
            print("BOT PICKED PAPER, YOU LOSE")
        elif botChoice == 3:
            print("BOT PICKED SCISSORS, YOU WIN")

    case 2:
        if botChoice == 1:
            print("BOT PICKED ROCK, YOU WIN")
        elif botChoice == 3:
            print("BOT PICKED SCISSORS, YOU LOSE")

    case 3:
        if botChoice == 1:
            print("BOT PICKED ROCK, YOU LOSE")
        elif botChoice == 2:
            print("BOT PICKED PAPER, YOU WIN")

