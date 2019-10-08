# Project Black Jack
# First player - casino, second player - you
# How to play Black Jack?
# Each player starts with two cards, one of the dealer's cards is hidden until the end. To 
#'Hit' is to ask for another card. To 'Stand' is to hold your total and end your turn. 
# If you go over 21 you bust, and the dealer wins regardless of the dealer's hand.

import random

card_deck = [['2 Hearts', 2], ['3 Hearts', 3], ['4 Hearts', 4], ['5 Hearts', 5], ['6 Hearts', 6], 
             ['7 Hearts', 7], ['8 Hearts', 8], ['9 Hearts', 9], ['10 Hearts', 10],  ['Jack Hearts', 10], ['Queen Hearts', 10], 
             ['King Hearts', 10], ['Ace Hearts', 11], ['2 Clubs', 2], ['3 Clubs', 3], ['4 Clubs', 4], ['5 Clubs', 5], 
             ['6 Clubs', 6], ['7 Clubs', 7],  ['8 Clubs', 8], ['9 Clubs', 9], ['10 Clubs', 10], ['Jack Clubs', 10], 
             ['Queen Clubs', 10], ['King Clubs', 10], ['Ace Clubs', 11], ['2 Diamonds', 2], ['3 Diamonds', 3], 
             ['4 Diamonds', 4], ['5 Diamonds', 5], ['6 Diamonds', 6], ['7 Diamonds', 7], ['8 Diamonds', 8], ['9 Diamonds', 9], 
             ['10 Diamonds', 10], ['Jack Diamonds', 10], ['Queen Diamonds', 10], ['King Diamonds', 10], ['Ace Diamonds', 11], 
             ['2 Spades', 2], ['3 Spades', 3], ['4 Spades', 4], ['5 Spades', 5], ['6 Spades', 6], ['7 Spades', 7], 
             ['8 Spades', 8], ['9 Spades', 9], ['10 Spades', 10], ['Jack Spades', 10], ['Queen Spades', 10], 
             ['King Spades', 10], ['Ace Spades', 11]]

# random cards
def card_choice(list1):
    return random.choice(list1)

# get a card from card_deck         
def game(num): # number of cards we need
    player = [] # list of cards
    for i in range(num):
        last_card = card_choice(card_deck)
        player.append(last_card)
        card_deck.remove(last_card)
    return player

# The beginning of game
def begin_game():
    while True:
        try:
            choice = input('Do you want to play? Yes/No')
        except ValueError:
            print("Sorry, I didn't understand that.")
        if choice == 'Yes':
            total1 = 0 # count for Casino's cards
            total2 = 0 # count for our cards
            
            first_player = game(1)
            total1 = first_player[0][1]
            second_player = game(2)
            total1 = first_player[0][1]
            total2 = second_player[0][1] + second_player[1][1]
            
            print("Casino's card: ", first_player[0][0])
            print("Casino's total: ", total1)
            print("Your first two cards: ", second_player[0][0]+",",second_player[1][0])
            print('Your total: ', total2)
            
            while True:
                try:
                    choice1 = input('Do you want more cards? ')
                except ValueError:
                    print("Sorry, I didn't understand that.")
                
                if choice1 == 'Yes':
                    second_player = game(1)
                    total2 += second_player[0][1]
                    
                    print('Your new card is: ', second_player[0][0])
                    print('Your total: ', total2)     
                    
                    if total2 > 21:
                        print('You lost!')
                        break
                elif choice1 == 'No':
                    first_player = game(1)
                    total1 += first_player[0][1]
                    
                    print("The second casino's card: ", first_player[0][0])
                    print("Casino's total: ", total1)
                    
                    if (total1 == 21) and (total2 <21):
                        print('You lost!')
                        break
                    elif (total1 == total2) and (total1 == 21):
                        print('Friendship won!')
                        break
                        
                    while total1 < total2:
                        first_player = game(1)
                        total1 += first_player[0][1]
                        
                        print("Casino's new card is: ", first_player[0][0])
                        print("Casino's total: ", total1)
                                                
                        if total1 > 21:
                            print('You won!')
                            break
                        elif total1 == total2:
                            print('Friendship won!')
                            break                        
                        elif total1 > total2:
                            print('You lost!')
                            break                            
                    break
                else:
                    continue
            break
        elif choice == 'No':
            break
        else:
            continue
begin_game()