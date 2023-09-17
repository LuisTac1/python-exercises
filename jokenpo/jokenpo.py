"""
Jokenpo (Rock, Paper n Scissors )
"""
import random

moves = ['rock', 'paper', 'scissors']
computer = random.choice(moves)
game_on = True

while game_on:
    player = str(input('\n[rock - paper - scissors]\n JOKENPO:')).lower()

    print('Computer: ',computer)
    
    if player not in moves:
        print('[Invalid option.\njust type "rock", "paper" or "scissors"]')
        
    if player == computer:
        print('Tie!')
    
    elif player == 'rock':
        if computer != 'paper':
            print('PLAYER WON!')
        else:
            print('Computer Won.')
        print('The game has ended.')
        game_on = False
    
    elif player == 'paper':
        if computer != 'scissors':
            print('PLAYER WON!')
        else:
            print('Computer Won.')
        print('The game has ended.')
        game_on = False

    elif player == 'scissors':
        if computer != 'rock':
            print('PLAYER WON!')
        else:
            print('Computer Won.')
        print('The game has ended.')
        game_on = False
