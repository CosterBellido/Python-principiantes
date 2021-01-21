# Calculadora de indice de masa corporal
height = float(input('Entrega tu talla en centrimetros: '))
weight = float(input('Entrega tu peso en kilogramos: '))
height = height/100
IMC = weight/(height*height)
print('El indice de tu masa corporal es:', IMC)
if(IMC > 0):
    if (IMC <= 16):
        print('Tienes muy bajo peso')
    elif (IMC <= 18.5):
        print('Tienes bajo peso')
    elif (IMC <= 25):
        print('Tu estas saludable')
    elif (IMC <= 30):
        print('Tu peso esta alto')
    else: print('Tu estas con sobrepeso')
else:
    print('Entregar detalles validos')