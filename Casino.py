# Please make sure you have Blackjack.py, Roulette.py, and Slotmachine.py, all together.
# Please make sure this file name is Casino.py (with capital C)

print("           Welcome to Casino")
print("   |||What would you like to play?|||")
#The startchoice input command will let you select which game you would like to play.
startchoice = input('[B]lack Jack, [R]oulette, or [S]lot machine\n')
if startchoice == 'b' or startchoice == 'B': #B will start the blackjack game.
    from Blackjack import *
    bjgame()
if startchoice == 'S' or startchoice == 's': #S will start the slot machine game.
    from Slotmachine import *
    smgame()
if startchoice == 'R' or startchoice == 'r': #R will start the roulette game.
    from Roulette import *
    start_Game()