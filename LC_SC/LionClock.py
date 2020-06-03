#Autor: Israel Zapata
#Fecha: 29/Mayo/2020
#Versión: 0.0.1
#Descripción: Manda los datos de Hora, Minuto y Segundo en tiempo real hacia el cuentametros/display RedLion mediante comunicación RS232
#v0.0.1 - 29/Mayo/2020 - Creación del programa

#********************CONFIGURACIÓN REDLION***********************
#Baudrate: 9600
#Paridad: NONE
#Bits: 8
#Auto: NO (Para evitar que el RedLion mande datos sin que se le pidan)
#SOLO mandar la cuenta a la salida serial del canal A o B
#Salida de datos: RS232
#*****************************************************************
#********************CONFIGURACIÓN RASPBERRY**********************
#os: Raspbian
#Serial Ports: ttyUSB0
#HDMI: No
#Ethernet: Solo para comunicación remota SSH
#IP Dinámica: Actualmente con: 169.254.87.163
#Detectar puerto tty: pi$: dmesg | grep tty
#Enlistar puertos: python -m serial.tools.list_ports
#Autorun: sudo nano home/pi/.bashrc -> python3 Reloj353.py
#****************************************************************

import serial
import time
import datetime

checkSerial = False

def openSerial():
    try:
        port_usb0 = serial.Serial(
            # usar port = '/dev/ttyUSB0 en linux
            port = 'COM1',
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits = serial.STOPBITS_ONE,
            bytesize = serial.EIGHTBITS
            )

        checkSerial = True
        print("\033[1;32;40mAdaptador serial hacia RedLion OK")
        print("\033[1;37;40m")
    except:
        print("\033[1;31;40mAdaptador serial hacia RedLion no conectado, primero conecta el cable y luego reinicia la Raspberry. Para reiniciar presiona Ctrl+Alt++Supr")
        print("\033[1;37;40m")

def main():
    openSerial()
    while checkSerial:
        FechaActual = datetime.datetime.now()
        Horas = FechaActual.strftime("%H")
        Minutos = FechaActual.strftime("%M")
        Segundos = FechaActual.strftime("%S")
        HoraCompletaString = 'VA%s.%s.%s*' % (Horas, Minutos, Segundos)
        HoraCompletaBytes = bytes(HoraCompletaString.encode())
        print(HoraCompletaString)
        port_usb0.write(HoraCompletaBytes)
        time.sleep(.2)

if __name__=="__main__":
    main()



