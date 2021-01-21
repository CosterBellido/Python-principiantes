# Generador de contraseñas
import random
passlen = int(input('Entrega la longitud de la contraseña'))
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = ''.join(random.sample(s, passlen))
print(p)