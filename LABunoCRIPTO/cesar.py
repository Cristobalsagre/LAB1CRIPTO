def cifrar_cesar(frase, corrimiento):
         resultado = ""
for caracter in frase:
        if caracter.isalpha():
            if caracter.islower():
                nuevo_caracter = chr(((ord(caracter) - ord('a') + corrimiento) % 26) + ord('a'))
            else:
                 nuevo_caracter = chr(((ord(caracter) - ord('A') + corrimiento) % 26) + ord('A'))
             resultado += nuevo_caracter
            else:
            resultado += caracter
return resultado

# Pedir al usuario la frase y el corrimiento
frase = input("Ingrese la frase a cifrar: ")
corrimiento = int(input("Ingrese el valor de corrimiento (número entero): "))

# Llamar a la función de cifrado César
texto_cifrado = cifrar_cesar(frase, corrimiento)

print("Texto cifrado:", texto_cifrado)
