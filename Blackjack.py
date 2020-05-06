import os
import random

coins = 50
Bet = 0
def quit():
    stream = open("casino.py")
    read_file = stream.read()
    exec(read_file)
#Blackjack uses all 4 suits of cards, each deck is accounted for using number cards and face cards. Number cards are 2 - 10, face cards are variables 11 - 14.
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4

def deal(deck):
    hand = []
    for i in range(2): #Registers that only 2 cards will be drawn initially
        random.shuffle(deck)
        card = deck.pop()
        if card == 11: card = "J"
        if card == 12: card = "Q"
        if card == 13: card = "K"
        if card == 14: card = "A"
        hand.append(card)
    return hand

def play_again():
    global coins
    print("You have: ", coins, "coins.")
    again = input("Do you want to play again? (Y/N) : ").lower()
    if again == "y":
        dealer_hand = []
        player_hand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
        bjgame()
    else:
        print("Bye!\n")
        quit()


def total(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K": #This registers that the face cards will add 10 to your total.
            total += 10
        elif card == "A":
            if total >= 11: #So as to not cause an unwanted bust, the Ace card will register itself as either 1 or 11 depending on the total amount in your current hand.
                total += 1
            else:
                total += 11
        else:
            total += card
    return total


def hit(hand):
    card = deck.pop() #Picks a random card and returns it to your hand.
    if card == 11: card = "J"
    if card == 12: card = "Q"
    if card == 13: card = "K"
    if card == 14: card = "A"
    hand.append(card)
    return hand


def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')


def print_results(dealer_hand, player_hand): #This function prints the results of what's in your hand and the dealer's hand.
    clear()
    print("The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
    print("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))


def blackjack(dealer_hand, player_hand): #This function checks your cards to see if you've drawn a blackjack initially.
    global coins
    global Bet
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        coins = Bet * 5 + coins
        print("Congratulations! You got a Blackjack!\n", "+", Bet * 5)
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Sorry, you lose. The dealer got a blackjack.\n")
        play_again()

def bust(dealer_hand, player_hand): #This function checks your cards to see if you or the dealer has drawn over 21.
    global coins
    global Bet
    if total(player_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("Sorry. You busted. You lose.\n")
        play_again()
    elif total(dealer_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("Dealer busts. You win", Bet * 2, "coins!\n")
        coins = Bet * 2 + coins
        play_again()

def score(dealer_hand, player_hand): #This function checks to see if your cards are higher than the dealer's or vice versa. It also checks to see if 21 has been drawn.
    global coins
    global Bet
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        coins = Bet * 5 + coins
        print("Congratulations! You got a Blackjack!\n", "+", Bet * 5)
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Sorry, you lose. The dealer got a blackjack.\n")
        play_again()
    elif total(dealer_hand) > total(player_hand):
        print_results(dealer_hand, player_hand)
        print("The dealer has a greater hand than you, you lose!\n")
        play_again()
    elif total(player_hand) > total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("You have a greater hand than the dealer! Congrats! You win", Bet * 2,"coins.\n")
        coins = Bet * 2 + coins
        play_again()
    elif total(player_hand) == total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("Looks like a draw! No one wins! You get", Bet,"coins back. \n")
        coins = Bet + coins
        play_again()

def bjgame(): #This is the game function. The rules of the game are explained and your cards are drawn. Once drawn you have the option of hitting, standing, or qutting. If you hit you will draw an additional card in order to either reach 21 or get a score higher than the dealer.
    global Bet #Throughout the process, every time you hit, the game will check to see if you or the dealer busts. If you stand it will check for busts, as well as your score.
    global coins #If you win, the game will return back to the score function and process the winnings accordingly.
    choice = 0 #If you select quit, the game will return you to the main casino menu.
    clear()
    print("WELCOME TO BLACKJACK!\n", "\n", "Draw 21 in order to win!\n", "All number cards are worth their respective amounts. \n", "Face cards: J, Q, K are worth 10 points each\n", "Ace cards are worth 1 or 11 depending on the amount in your hand.\n", "Payout for a greater hand is 2 to 1, blackjacks are 5 to 1. \n")
    print("You have", coins, "coins\n")
    Bet = int(input("    How much would you like to bet?: "))
    coins = coins - Bet
    dealer_hand = deal(deck)
    player_hand = deal(deck)

    while choice != "q" and total(player_hand) < 21:
        print("\n The dealer is showing a " + "[" + str(dealer_hand[1]) + "]")
        print("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
        blackjack(dealer_hand, player_hand)
        choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
        clear()
        if choice == "h":
            hit(player_hand)
            print("\n You have" + str(player_hand) + " for a total of " + str(total(player_hand)))
            bust(dealer_hand, player_hand)
            if total(dealer_hand) < 17:
                print("The dealer hits.")
                hit(dealer_hand)
                bust(dealer_hand, player_hand)
                if choice != "q":
                    blackjack(dealer_hand, player_hand)
                    choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
                    if choice == "h":
                        hit(player_hand)
                        print("\n You have" + str(player_hand) + " for a total of " + str(total(player_hand)))
                        bust(dealer_hand, player_hand)
                        if total(dealer_hand) < 17:
                            print("The dealer hits again!")
                            hit(dealer_hand)
                            bust(dealer_hand, player_hand)
                            if total(dealer_hand) < 17:
                                print("The dealer hits three times!!!")
                                hit(dealer_hand)
                                bust(dealer_hand, player_hand)
                                if total(dealer_hand) < 17:
                                    print("The dealer hits FOUR TIMES!!!")
                                    hit(dealer_hand)
                                    bust(dealer_hand, player_hand)
                                    score(dealer_hand, player_hand)
                                    if total(player_hand) > 21 or total(dealer_hand) > 21:
                                        print("\n You have" + str(player_hand) + " for a total of " + str(total(player_hand)))
                                        bust(dealer_hand, player_hand)
                    elif choice == "s":
                        while total(dealer_hand) < 17:
                            hit(dealer_hand)
                        bust(dealer_hand, player_hand)
                        score(dealer_hand, player_hand)
                        play_again()
                    elif choice == "q":
                        print("Bye!\n")
                        quit()
        elif choice == "s":
            while total(dealer_hand) < 17:
                hit(dealer_hand)
            bust(dealer_hand, player_hand)
            score(dealer_hand, player_hand)
        elif choice == "q":
            print("Bye!\n")
            quit()


if __name__ == "__main__":
    bjgame()