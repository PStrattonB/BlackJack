"""
Assignment 5 - Blackjack
Peter Barry
"""

import random

player_hand = []
player_hit_card = []
dealer_hand = []
dealer_hit_card = []


def main():
    print('\nWelcome to Blackjack')
    while True:

        print(f'{"":-^50}\n')
        new_game = ''
        while new_game != 'y':  # Loop to ensure we're getting a valid input for new_game
            new_game = input('Type "Rules" to display game rules\nDo you wish to start a new game? (y/n): ').lower()

            if new_game == 'y':
                clear_hands()  # Calls the clear_hands function to reset hand variables for a new game
                deal_hands()  # Calls the deal_hands function to assign cards to player and dealer hands

                print(f'\nPlayer draws a {player_hand[0]} and a {player_hand[1]}. Your total is {sum(player_hand)}\n')
                print(f'The Dealer draws a {dealer_hand[0]} and a hidden card\n')
            elif new_game == 'n':
                print('Goodbye!')
                exit()
            elif new_game == 'rules':
                game_rules()
            else:
                print('Please enter a valid input\n')

        while sum(player_hand) != 21:  # Loop containing Player's turn

            player_hs = input('Hit or Stand? (h/s): ').lower()
            if player_hs == 'h':
                player_hit_card.append(random.randint(1, 10))
                player_hand.extend(player_hit_card)

                print(f'Player hits! Player draws {player_hit_card[0]} for a new total of {sum(player_hand)}\n')
                player_hit_card.clear()
                if sum(player_hand) > 21:  # If to check if player has 21 or busts.
                    print(f'Player total is {sum(player_hand)}, player busts!\n')
                    break
                elif sum(player_hand) == 21:
                    print(f'Player total is {sum(player_hand)}!, player automatically stands and passes turn to dealer.\n')
                    # If this condition is TRUE, we should break out of player turn loop next time it checks
                else:
                    pass
            elif player_hs == 's':
                print('Player stands!\n')
                break
            else:
                print('Please choose a valid input.\n')

        # Dealer's turn
        if sum(player_hand) <= 21:  # Check to see if we're starting dealer turn, skip this print otherwise
            print(f'Dealer reveals hidden card: {dealer_hand[1]} for a total of {sum(dealer_hand)}\n')
        while True:
            if sum(player_hand) <= 21:
                if sum(dealer_hand) <= 16:
                    dealer_hit_card.append(random.randint(1, 10))
                    dealer_hand.extend(dealer_hit_card)
                    print(f'Dealer hits! Dealer draws a {dealer_hit_card[0]} for a total of {sum(dealer_hand)}\n')
                    dealer_hit_card.clear()
                elif 17 <= sum(dealer_hand) < 21 and sum(dealer_hand) != 21:  # sum(dealer_hand) >= 17 and sum(dealer_hand) != 21 and sum(dealer_hand) < 21
                    print('Dealer Stands\n')
                    if sum(dealer_hand) >= sum(player_hand):
                        print(f'Dealer wins! Beating player hand of {sum(player_hand)} with a hand of {sum(dealer_hand)}\n')
                        break
                    elif sum(dealer_hand) < sum(player_hand):
                        print(f'Player wins! Beating Dealer hand of {sum(dealer_hand)} with a hand of {sum(player_hand)}\n')
                        break
                    else:
                        pass
                elif sum(dealer_hand) == 21:
                    print(f'Dealer has 21! Dealer wins\n')
                    break
                elif sum(dealer_hand) > 21:
                    print(f'Dealer busts with a total of {sum(dealer_hand)}\n'
                          f'Player wins!')
                    break
            else:
                print('Dealer wins!\n')
                break


def clear_hands():
    player_hand.clear()
    player_hit_card.clear()
    dealer_hand.clear()
    dealer_hit_card.clear()


def deal_hands():
    number_of_cards = 2
    while number_of_cards > 0:
        player_hand.append(random.randint(1, 10))
        dealer_hand.append(random.randint(1, 10))
        number_of_cards = number_of_cards - 1


def game_rules():
    print("\nWhen the game starts, both you and the dealer are dealt 2 cards. One of the dealer's cards will be hidden.\n"
          "You will win the game if the total of your cards is higher than the dealer's total without going over 21.\n"
          "Any ties with the dealer will result in a loss for the player. You can choose to 'hit' to be given another\n"
          "card, or you can 'stand' to keep the cards you have and allow the dealer to have their turn.\n")


if __name__ == '__main__':
    main()
