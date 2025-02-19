import random
import string

# Caracteres permitidos
caracteres = string.ascii_letters + string.digits + string.punctuation

# Crear archivo con 100 líneas de 60 caracteres aleatorios
with open('DATOS_RANDOM1.txt', 'w') as archivo:
    for _ in range(100):
        linea = ''.join(random.choice(caracteres) for _ in range(60))
        archivo.write(linea + '\n')

print("Archivo 'DATOS_RANDOM.txt' creado con éxito.")
