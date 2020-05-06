# Please make sure this file name is "Slotmachine.py" (with a capital S)
# Please make sure you have Casino.py

print("You have 20 coins.", "\n","1 coin = 1 spin", "\n", "Match 3 symbols in a row in order to win!", "\n", "[ 777 ] = 15x ","\n","[ Win ] = 2x","\n","[ BAR ] = 3x","\n","[ BANKRUPT ] = LOSE","\n","[ (8) ] = 8x","\n","[ $$$ ] = 18x")
B = 20 #B stands for Balance, so this is the starting balance.
Bet = 0 #Bet is the amount you can play per spin, your bet cannot exceed your balance and you cannot continue betting once you've reached 0 balance.
W = 0 #W stands for winnings.
def quit():
    stream = open("casino.py")
    read_file = stream.read()
    exec(read_file)

import random
def respin():#Respin will initiate after a user spins and wins or loses.
    global B
    global Bet
    user_input1 = input("Would you like to try another spin? Y or N?\n")
    if user_input1 == "Y" or user_input1 == "y" or user_input1 == "":
        print("How much would you like to bet?")
        Bet = int(input("Bet amount: "))
        if Bet == 0 or Bet > B:
            print("Insufficient Funds.\n")
            respin()
        spin()
    else:
        print("   Score: ", B)
        print("Thank you for playing!")
        quit()
def spin(): #The spin function defines the symbols and their winning variables. It spins 3 random symbols and based on their combination will determine whether or not the user wins or loses.
    global B
    global W
    global Bet
    B = B - Bet
    print("      | -", Bet," coins |  ")
    Slot1 = random.choice(["[ $$$ ]", "[ 777 ]", "[ BAR ]", "[ (8) ]", "[ Win ]", "[ BANKRUPT ]"])
    Slot2 = random.choice(["[ $$$ ]", "[ 777 ]", "[ BAR ]", "[ (8) ]", "[ Win ]", "[ BANKRUPT ]"])
    Slot3 = random.choice(["[ $$$ ]", "[ 777 ]", "[ BAR ]", "[ (8) ]", "[ Win ]", "[ BANKRUPT ]"])
    print("|",Slot1,Slot2,Slot3,"|","\n")

    while B >= 1: #While your balance is greater than or equal to 1, you are able to spin.
        if Slot1 == Slot2 == Slot3 == "[ $$$ ]":
            W = Bet * 18
            B = B + W
            print ("    ====!!!YOU WIN!!!====\n","        +",  W, "COINS\n","     Balance:",  B,"coins","\n","   =====================")
            respin()
        elif Slot1 == Slot2 == Slot3 == "[ 777 ]":
            W = Bet * 15
            B = B + W
            print ("    ====!!!YOU WIN!!!====\n","        +",  W, "COINS\n","     Balance:",  B,"coins","\n","   =====================")
            respin()
        elif Slot1 == Slot2 == Slot3 == "[ BAR ]":
            W = Bet * 3
            B = B + W
            print ("    ====!!!YOU WIN!!!====\n","        +",  W, "COINS\n","     Balance:",  B,"coins","\n","   =====================")
            respin()
        elif Slot1 == Slot2 == Slot3 == "[ (8) ]":
            W = Bet * 8
            B = B + W
            print ("    ====!!!YOU WIN!!!====\n","        +",  W, "COINS\n","     Balance:",  B,"coins","\n","   =====================")
            respin()
        elif Slot1 == Slot2 == Slot3 == "[ Win ]":
            W = Bet * 2
            B = B + W
            print ("    ====!!!YOU WIN!!!====\n","        +",  W, "COINS\n","     Balance:",  B,"coins","\n","   =====================")
            respin()
        elif Slot1 == Slot2 == Slot3 == "[ BANKRUPT ]": #The twist to our game comes from the bankrupt symbol which will cash out your entire winnings and account balance.
            W = Bet - Bet
            B = B - B
            print(" YOU STRUCK OUT\n")
        else:
            print("     ___ You Lose ___\n", "    Balance:", B,"coins", "\n", "    ________________")
            respin()

    else:
        print("   |||||You lost|||||\n", "  Balance: ",B," coins")
        print("   Score: ", B)
        print("  Thank you for playing!\n")
        respin()
#smgame is the starting function found in the Casino.py file, this function will trigger the program to run.
def smgame():
    global B
    global Bet
    user_input = input("Would you like to spin? Y or N?\n")
    if user_input == "Y" or user_input == "y" or user_input == "":
        print("How much would you like to bet?")
        Bet = int(input("    Bet: "))
        if Bet > B:
            print("Insufficient Funds.\n")
            respin()
        spin()
    else:
        print("   Score: ", B)
        print("   Thank you for playing!")
        respin()
