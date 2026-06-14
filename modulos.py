# Un módulo es simplemente un archivo con extensión .py que contiene código de Python (funciones, clases, variables, etc.).
"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular 
  como un programa más pequeño que cumple una función específica. 
  La función se puede reutilizar con el simple hecho de invocarla o mandarla llamar.

  Sintaxis:

   def nombreFuncion(parametros):
      bloque de instrucciones

   nombreFuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Función que no recibe parámetros y no regresa valor
   3.- Función que recibe parámetros y no regresa valor
    
    Funciones de tipo "Función"
   2.- Función que no recibe parámetros y regresa valor
   4.- Función que recibe parámetros y regresa valor

"""


#1.- Funcion que no recibe parametros y no regresa valor
def saludo():

    usuario = input("Ingresa tu nombre: ").strip().upper()
    apellido_usuario = input("Ingresa tu apellido: ").strip().upper()

    print(f"Hola soy {usuario} {apellido_usuario}")

#3.- Funcion que recibe parametros y no regresa valor 
def presentar(nombre_persona, apellido_persona):

    nombre_texto = nombre_persona.strip().upper()
    apellido_texto = apellido_persona.strip().upper()

    print(f"Hola soy {nombre_texto} {apellido_texto}")

presentar("Juan", "Perez")

#2.- Funcion que no recibe parametros y regresa valor
def sumar():

    valor1 = int(input("Ingresa un numero: "))
    valor2 = int(input("Ingresa otro numero: "))

    resultado_suma = valor1 + valor2

    return resultado_suma

respuesta_suma = sumar()

print(f"La suma es: {respuesta_suma}")


#4.- Funcion que recibe parametros y regresa valor
def multiplicar(numero_a, numero_b):

    resultado_multi = numero_a * numero_b

    return resultado_multi

respuesta_multi = multiplicar(5, 4)

print(f"La multiplicacion es: {respuesta_multi}")


#Invocar las funciones
saludo()
presentar()
sumar()
multiplicar()