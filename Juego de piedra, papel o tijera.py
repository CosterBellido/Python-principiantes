# Juego de piedra, papel o tijera
import random
choice = ['Piedra', 'Papel', 'Tijera']
computer = random.choice(choice)
player = False
cpu_score = 0
player_score = 0

while True:
    player = input('Piedra, Papel o Tijera?').capitalize()
    if player == computer:
        print('Empate')
    elif player == 'Piedra':
        if computer == 'Papel':
            print('Tu perdiste!', computer, 'fue mejor')
        else:
            print('Tu ganaste', player, 'fue mejor')
            player_score += 1
    elif player == 'Papel':
        if computer == 'Tijera':
            print('Tu perdiste!', computer, 'fue mejor')
            cpu_score += 1
        else:
            print('Tu ganas', player, 'fue mejor')
            player_score += 1
    elif player == 'Tijera':
        if computer == 'Piedra':
            print('Tu perdiste', computer, 'fue mejor')
            cpu_score += 1
        else:
            print('Tu ganas', player, 'fue mejor')
            player_score += 1
    elif player == 'End':
        print('Final del resultado:')
        print(f"CPU:{cpu_score}")
        print(f"Player: {player_score}")
        break