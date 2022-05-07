'''This is a program that allows the user to play rock, paper, scissors with the computer.'''
import random

user_input = input('Enter a choice (rock, paper, scissors): ')

actions = ['rock', 'paper', 'scissors']
computer_choice = random.choice(actions)

# used for debugging in case of errors
print(f'\nYou chose {user_input}, computer chose {computer_choice}.\n')

if user_input == computer_choice:
    print('Tie!')
elif user_input == 'rock':
    if computer_choice == 'scissors':
        print('You win! Rock (player) smashes Scissors (computer)!')
    else:
        print('You lose! Paper (computer) covers Rock (player)!')
elif user_input == 'paper':
    if computer_choice == 'rock':
        print('You win! Paper (player) covers Rock (computer)!')
    else:
        print('You lose! Scissors (computer) cuts Paper (player)!')
elif user_input == 'scissors':
    if computer_choice == 'paper':
        print('You win! Scissors (player) cuts Paper (computer)!')
    else:
        print('You lose! Rock (computer) smashes Scissors (player)!')