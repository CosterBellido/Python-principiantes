# Creando acrononimos con la primera letra de cada palabra

user_imput = str(input("Escriba una frase"))
text = user_imput.split()
a = ''
for i in text:
    a = a + str(i[0].upper())
print(a)
