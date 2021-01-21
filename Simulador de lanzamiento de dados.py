# Simulador de lanzamiento de dados
import random
# rando de los valores de un dado
min_val = 1
max_val = 6
# bucle para la peticion
roll_again = 'yes'
# bucle
while roll_again == 'si' or roll_again == 'yes':
    print('Lanzando los dados')
    print('Los valores son:')
    # Generando el primer valor aleatorio entero del 1 al 6
    print(random.randint(min_val, max_val))
    # Generando el segundo valor aleatorio entero del 1 al 6
    print(random.randint(min_val, max_val))
    # Pidiendo al usuario si desea lanzar de nuevo
    roll_again = input('¿Desea lanzar nuevamente?')