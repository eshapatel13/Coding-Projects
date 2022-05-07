'''This program allows the user to play as many games of blackjack against the computer as they’d like.'''

import random


# Deals a card. Values range from 1 to 10
def deal_card(card_deck):
    # create a logic with which you can draw a card from the card deck
    # you draw one card from card_deck and assign it to card_val
    card_val = random.choice(card_deck)
    user_card = card_val
    card = card_val
    # remove card from the deck
    card_deck.remove(card_val)
    # need something to turn the cards into numeric values Ace=1, Jack,Queen,King=10
    if card_val[0] == 'Ace':
        user_card = 1
    elif card_val[0] == 'Jack':
        user_card = 10
    elif card_val[0] == 'Queen':
        user_card = 10
    elif card_val[0] == 'King':
        user_card = 10
    else:
        card_val = card_val[0]
        user_card = int(card_val)
    # return three things. Card is the card just drawn (e.g., ["Ace", "Hearts"])
    # card_val is its numeric value.
    return card_deck, card, user_card


# Handles the turn. Returns the point value for the player's hand.
def get_score(card_deck, scores):
    # First draw for the player
    card_deck, card, hand_val = deal_card(card_deck)
    # Get the player's carddeck, card, and score.
    # Update player's score and cards on hand
    scores['player']['score'] += hand_val
    scores['player']['cards'].append(card)

    # First draw for the dealer
    card_deck, card, hand_val = deal_card(card_deck)
    # Get the dealer's carddeck, card, and score.
    # Update dealer's score and cards on hand
    scores['dealer']['score'] += hand_val
    scores['dealer']['cards'].append(card)

    # Second draw for the player
    card_deck, card, hand_val = deal_card(card_deck)
    # Get the player's carddeck, card, and score.
    scores['player']['score'] += hand_val
    scores['player']['cards'].append(card)
    # Update player's score and cards on hand

    # Second draw for the dealer
    card_deck, card, hand_val = deal_card(card_deck)
    # Get the dealer's carddeck, card, and score.
    # Update dealer's score and cards on hand
    scores['dealer']['score'] += hand_val
    scores['dealer']['cards'].append(card)

    # Show cards on player's hand
    cards_on_hand = scores
    type_of_role = 'player'
    show_cards(cards_on_hand, type_of_role)
    # you should display the sum of the two cards
    score_of_player = scores['player']['score']
    print("The sum of the first two cards is:", score_of_player)
    # then, ask users whether they want to get another card
    user_response = input("Do you want to take another card?: (Y/N) ")
    # if either the user is busted or the user wants to stop, then you need to stop
    while user_response == "Y" or user_response == "y":
        # Get the player's carddeck, card, and score.
        card_deck, card, hand_val = deal_card(card_deck)
        # update card deck, score, and drawn cards accordingly
        scores['player']['score'] += hand_val
        scores['player']['cards'].append(card)
        show_cards(cards_on_hand, type_of_role)
        score_of_player = scores['player']['score']

        card_deck, card, hand_val = deal_card(card_deck)
        scores['dealer']['score'] += hand_val
        scores['dealer']['cards'].append(card)
        score_of_dealer = scores['dealer']['score']
        # Once you got the player_score, you have to check whether the player got busted
        # According to the result you should display different prompts.
        if score_of_dealer > 21:
            print("The dealer BUSTED with a total value of", score_of_dealer)
            print('\n', "** You Win! **", '\n')
            print('Your score:', score_of_player)
            break
        if score_of_player <= 21:
            print("Your hand now has a total value of:", score_of_player)
            user_response = input("Do you want to take another card?: (Y/N) ")
            if user_response == "N" or user_response == "n":
                print("You have stopped taking more cards with a hand value of:", score_of_player)
                show_cards(cards_on_hand, type_of_role)
                break
        else:
            break
    # return the score
    return scores


# Get two arguments (cards on hand, type of role (e.g., player, dealer))
# Display all cards on hands
def show_cards(cards, who):
    # complete this part
    if who == 'player':
        print("Your cards:")
        for cards in cards['player']['cards']:
            print(cards[0], ' of ', cards[1], sep="")
    elif who == 'dealer':
        print("Dealer's cards:")
        for cards in cards['dealer']['cards']:
            print(cards[0], ' of ', cards[1], sep="")


# Create a card deck from an input file (cards.txt).
# Then, return 52 cards saved in a list of lists
def set_card_deck():
    # Complete this function
    # iterate over each line, then split line by line
    cards = []
    file = open('cards.txt')
    for line in file:
        line = line.rstrip()
        cards.append(line.split(','))
    return cards


# The main function.  It repeatedly plays games of blackjack until the user decides to stop.
def main():
    # Prime the loop and start the first game.
    user_response = "Y"

    while user_response == "Y" or user_response == "y":
        # Set a card deck
        cards = set_card_deck()
        # Set a dictionary to manage scores of the player and dealer
        scores = {'player': {'score': 0, 'cards': []}, 'dealer': {'score': 0, 'cards': []}}
        # Get the scores.
        scores = get_score(cards, scores)
        player_score = scores['player']['score']
        dealer_score = scores['dealer']['score']
        # Once you got the player_score, you have to check whether the player got busted, whether player's score
        # is larger than the dealer's score. According to the result you should display different prompts.
        # ask user whether he/she wants to play another game
        if dealer_score > 21:
            cards_on_hand = scores
            type_of_role = 'player'
            show_cards(cards_on_hand, type_of_role)
        elif player_score > 21:
            print("You BUSTED with a total value of", player_score)
            print("The dealer was dealt a hand with a value of:", dealer_score)
            print('\n', "** You Lose! **", '\n')
        # player lose if they have equal value to the dealer
        elif player_score == dealer_score:
            print("The dealer was dealt a hand with a value of:", dealer_score)
            print('\n', "** You Lose! **", '\n')
        # player lose if the dealer has a higher score
        elif player_score < dealer_score:
            print("The dealer was dealt a hand with a value of:", dealer_score)
            print('\n', "** You Lose! **", '\n')
        # player win if they have a higher score than the dealer
        else:
            print("The dealer was dealt a hand with a value of:", dealer_score)
            print('\n', "** You Win! **", '\n')
        cards_on_hand = scores
        type_of_role = 'dealer'
        show_cards(cards_on_hand, type_of_role)
        user_response = input("Do you want to play another game?: (Y/N) ")


# Call the main function to start the blackjack program.
main()
