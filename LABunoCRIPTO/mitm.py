from termcolor import colored

# Función para descifrar un mensaje cifrado con un corrimiento específico
def descifrar_cesar(frase_cifrada, corrimiento):
    resultado = ""
    for caracter in frase_cifrada:
        if caracter.isalpha():
            if caracter.islower():
                nuevo_caracter = chr(((ord(caracter) - ord('a') - corrimiento) % 26) + ord('a'))
            else:
                nuevo_caracter = chr(((ord(caracter) - ord('A') - corrimiento) % 26) + ord('A'))
            resultado += nuevo_caracter
        else:
            resultado += caracter
    return resultado

# Obtener el mensaje cifrado desde el usuario
mensaje_cifrado = input("Ingrese el mensaje cifrado: ")

# Variables para rastrear la opción más probable
opcion_mas_probable = ""
corrimiento_mas_probable = 0
mayor_probabilidad = 0

# Realizar un ataque de fuerza bruta probando todas las combinaciones de corrimiento
for corrimiento in range(26):  # 26 letras en el alfabeto
    mensaje_descifrado = descifrar_cesar(mensaje_cifrado, corrimiento)
    
    # Calcular la probabilidad en función de la longitud de las palabras válidas
    palabras = mensaje_descifrado.split()
    probabilidad = sum(len(palabra) for palabra in palabras if palabra.isalpha())
    
    print(f"Corrimiento {corrimiento}: {mensaje_descifrado}")

    # Actualizar la opción más probable si es necesario
    if probabilidad > mayor_probabilidad:
        mayor_probabilidad = probabilidad
        opcion_mas_probable = mensaje_descifrado
        corrimiento_mas_probable = corrimiento

# Imprimir la opción más probable en verde
print("\nOpción más probable:")
print(colored(f"Corrimiento {corrimiento_mas_probable}: {opcion_mas_probable}", 'green'))
