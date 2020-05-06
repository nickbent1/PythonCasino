# Please make sure this file name is "Roulette.py" (with capital R)
# Please make sure you have Casino.py

import random

red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36] #red defines a set of winning numbers as well as the Red color variant on the roulette wheel.
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]#black defines a set of winning numbers as well as the Black color variant on the roulette wheel.
bankaccount = 36 #The bank account variable is the starting balance in chips the user has.
bet = 0 #The bet variable is the amount a user can bet. The user cannot bet more than their bankaccount balance, and cannot continue to bet once their balance has reached 0.

def quit(): #The quit function will take the user back to the main menu.
    stream = open("Casino.py")
    read_file = stream.read()
    exec(read_file)

def betchoice(number): #The betchoice function defines the winning amounts for the array numbers.
    global bankaccount
    global bet
    global red
    global black
    playerchoice = (number)
    spin = random.randint(1,36) #This will select a random number between 1-36.
    if playerchoice == spin:
        betaddition = int(35 * bet)
        bankaccount = bankaccount + betaddition #If your choice matches the random spin number you will win 35 times the original bet amount.
        print("The ball lands on :", spin)
        print("You win:", betaddition)
        print("You have", bankaccount)
        start_Game()
    else:
        print("The ball lands on :", spin) #If your choice does not match the random spin number you will lose your original bet amount.
        print(playerchoice)
        print("You lose ", bet, "chips.")
        start_Game()
    return playerchoice



def Welcome(): #The welcome message defines the rules of the game.
    print("Welcome to high-stakes python roulette!", "\n", "Minimum 1 chip per spin", "\n", "Match a number and a color combination to win!", "\n", "You may only bet on the listed numbers, so the odds are 1 in 36 chances of winning.", "\n", "The payout is 35 to 1! So get spinning and best of luck!", "\n")

def start_Game(): #The start_Game function allows the user to place their bet as well as select their winning numbers and color.
    global bankaccount
    global bet
    global red
    global black
    print("\n You have:",bankaccount, "chips")
    question1 = input("Would you like to start game [Y]es or [N]o \n")
    if question1 == "Y" or question1 == "y":
        bet = int(input("How many chips would you like to bet: "))
        if bet == 0 or bet > bankaccount:
            print("You don't have enough chips.\n")
            start_Game()
        bankaccount = bankaccount - bet
        print( "\nPlace your bet! ")
        print("The numbers for {RED} are 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36")
        print("The numbers for {BLACK} are 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35\n")
        number = int(input("Type a number between 1 and 36: ")) #Pick a number 1 - 36 as listed.
        betchoice(number) #Your choice will be registered here.
    else:
        print("Thank you come again ")
        quit()

Welcome()
start_Game()