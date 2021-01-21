# Generador de historias
import random
when = ['Hace algunos años', 'Ayer', 'La noche pasada', 'Hace un largo tiempo', 'El 20 de junio']
who = ['un conejo', 'un elefante', 'un raton', 'una tortuga', 'un gato']
name = ['Ali', 'Miriam', 'Daniel', 'Hoouk', 'Starwalker']
residence = ['Barcelona', 'India', 'Alemania', 'Venecia', 'Inglaterra']
went = ['cine', 'universidad', 'seminario', 'colegio', 'lavanderia']
happened = ['hizo muchos amigos', 'comio una amburguesa', 'encontro una clave secreta', 'resolvio un misterio', 'escribio un libro']
print(random.choice(when) + ', ' + random.choice(who) + ' vivio en ' + random.choice(residence) + ', fue a la ' + random.choice(went) + ' y ' + random.choice(happened))