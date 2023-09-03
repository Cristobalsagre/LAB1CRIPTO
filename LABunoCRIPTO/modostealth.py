import os
import sys
import socket
import struct
import time
from scapy.all import *

# Función para enviar un paquete ICMP con secuencia y ID especificados
def enviar_paquete_icmp(destino, caracter, secuencia, id):
    ip = IP(dst=destino)
    icmp = ICMP()
    icmp.seq = secuencia  # Establecer la secuencia
    icmp.id = id  # Establecer el ID
    data = struct.pack('B', caracter)  # Empaqueta el caracter en un byte

    # Combinar IP, ICMP y datos
    paquete = ip / icmp / data

    send(paquete, verbose=False)
    print(f"Sent packet (ID: {id}, Seq: {secuencia})")

# Función para cifrar y enviar la frase
def cifrar_y_enviar_frase(frase, destino):
    secuencia = 1
    id = os.getpid() & 0xFFFF  # Usar el ID del proceso actual como ID ICMP
    for caracter in frase:
        caracter_ascii = ord(caracter)
        enviar_paquete_icmp(destino, caracter_ascii, secuencia, id)
        secuencia += 1
        time.sleep(0.1)  # Esperar un corto período para evitar sobrecargar la red

# Obtener la frase cifrada desde el usuario
frase_cifrada = input("Ingrese la frase cifrada: ")
destino = "8.8.8.8"  # Dirección IP de destino

# Llamar a la función para cifrar y enviar la frase
cifrar_y_enviar_frase(frase_cifrada, destino)
