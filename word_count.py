import sys

archivo = sys.argv[1]

def contar_caracteres(texto):
    caracteres = set(texto)
    return len(caracteres)

def contar_palabras(texto):
    palabras = texto.split(" ")
    return len(set(palabras))

# Importar el texto del archivo
with open(archivo, "r") as file:
    texto = file.read()

# Contar la cantidad de caracteres distintos
numero_caracteres = contar_caracteres(texto)

# Contar la cantidad de palabras distintas
numero_palabras = contar_palabras(texto)

# Imprimir los resultados
print(f"El número de caracteres distintos es: {numero_caracteres}")
print(f"El número de palabras distintas es: {numero_palabras}")