import utime
import machine
import time
from machine import UART, Pin


# Configuración del UART
uart = UART(0, baudrate=16000,tx=Pin(0), rx=Pin(1))

led = machine.Pin("LED", machine.Pin.OUT)
# Función para recibir el archivo
def Recivir_TXT(Datos_Recibidos):
    with open(Datos_Recibidos, 'w') as archivo:
        while True:
            contenido = uart.read()
            if contenido:
                mensajeTX=contenido
                archivo.write(mensajeTX)
                led.on()
                utime.sleep(0.1)
                led.off()
                utime.sleep(2)
                print("Archivo TXT recibido.")
Recivir_TXT('Datos_Recibidos.txt')
