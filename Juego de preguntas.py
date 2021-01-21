# Juego de preguntas
def check_guess(guess, answer):
    global score   # Es una variable local y lo convertimos a global
    still_gressing = True
    attempt = 0
    while still_gressing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Respuesta correcta')
            score += 1
            still_gressing = False
        else:
            if attempt < 2:
                guess = input('Respuesta equivocada, trata de nuevo')
            attempt += 1
    if attempt == 3:
        print('La respuesta correcta es: ',answer)
score = 0
print('Adivina el animal')
guess1= input('¿Que oso vive en el polo norte?')
check_guess(guess1, 'Oso polar')
guess2= input('¿Cual es el animal mas rapido de la tierra?')
check_guess(guess2, 'Leopardo')
guess3= input('¿Cual es el animal mas grande?')
check_guess(guess3, 'Ballena azul')
print('Tu resultado es: ' + str(score))