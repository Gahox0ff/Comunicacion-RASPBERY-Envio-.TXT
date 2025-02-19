import machine
import utime
from machine import UART, Pin

# Configuración del UART
uart = UART(0, baudrate=16000, tx=Pin(0), rx=Pin(1))

# Configuración del LED
led = machine.Pin("LED", machine.Pin.OUT)  # LED integrado en la Raspberry Pi Pico

def Envio_TXT(DATOS):
    # Abrir el archivo en modo lectura
    with open(DATOS, 'r') as Datos_Random:
        mensaje = Datos_Random.read()  # Leer todo el contenido del archivo
        led.on()  # Encender el LED
        uart.write(mensaje)  # Enviar el contenido por UART
        utime.sleep(2)  # Esperar 2 segundos para asegurar que todos los datos sean enviados
        led.off()  # Apagar el LED
        print("Archivo enviado")

# Llamar a la función para enviar el archivo
Envio_TXT('DATOS.txt')
