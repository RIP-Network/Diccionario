from selenium import webdriver
import time
import smtplib, ssl
import os
import time
import getpass

#colores
negro = '\033[30m'
rojo = '\033[31m'
verde = '\033[32m'
amarillo = '\033[33m'
azul = '\033[34m'
rosado = '\033[35m'
calipso= '\033[36m'
blanco = '\033[37m'
cierre = '\033[39m'

print(rojo+"Se requiere Firefox!")
print(blanco+"Si no tienes Firefox pulsa CTRL+C para cerrar el programa y instalar firefox e volver")
time.sleep(5)
os.system("clear")

web = webdriver.Firefox ()
web.get('https://raw.githubusercontent.com/hackingyseguridad/diccionarios/master/diccionario.txt')
web = webdriver.Firefox ()
web.get('https://raw.githubusercontent.com/hackingyseguridad/diccionarios/master/usuarios.txt')


print(blanco+"Gracias por usar mi script ! , atte RIP-Network")