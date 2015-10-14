import os
import math

def suma(num1, num2):
    try:
        print ('{:^16}'.format('SUMA'))
        print ('{} + {} = {}'.format(num1, num2, num1 + num2))
        input(" ")
    except ValueError:
        print ("Introduzca solo numeros ")

def resta():
        try:
                num01 = eval(input("Número 01: "))
                num02 = eval(input("Número 02: "))
                #aux = num01 - num02
                print ("La resta es: ", int(num01 - num02))
                #return nombres
        except NameError:
                print("Ha ocurrido un error!")


def div(num1, num2):
	try:
		res = num1 / num2
		print (" Resultado: ", res)
	except ZeroDivisionError:
		print ("Error: Divicion entre cero ")

def multi(a, b):
    return a * b

def exponente():
    try:
        num01 = eval(input("Número : "))
        num02 = eval(input("Exponente : "))
        print ("El resultado es: ", int(num01 ** num02))
    except NameError:
            print("Ha ocurrido un error!")

def tangente():
    try:
        num01 = eval(input("Tangente: "))
        aux = math.tan(num01)
        print ("El resultado es: ", float(aux))
    except NameError:
        print("Ha ocurrido un error!")

def logaritmo():
    try:
        num01 = eval(input("Logaritmo: "))
        num02 = eval(input("Base: "))
        aux = math.log(num01, num02)
        print ("El resultado es: ", float(aux))
    except NameError:
        print("Ha ocurrido un error!")

opcion = 0
while opcion != 11:
    os.system('clear')
    print ('{:^50}'.format('Calculadora'))
    print ('{:^50}'.format('1. Suma'))
    print ('{:^50}'.format('2. Resta'))
    print ('{:^50}'.format('3. Division'))
    print ('{:^50}'.format('4. Multiplicacion')))
    print ('{:^50}'.format('5. Exponente'))
    print ('{:^50}'.format('6. Log'))
    print ('{:^50}'.format('7. Seno'))
    print ('{:^50}'.format('8. Coseno'))
    print ('{:^50}'.format('9. Tangente'))
    print ('{:^50}'.format('10. Inverso'))
    print ('{:^50}'.format('11. Salir'))

    if opcion == 1:
        a = eval(input("Valor a: "))
        b = eval(input("Valor b: "))
        suma(a, b)

    if opcion == 2:
        resta()

    if opcion == 3:
        a = eval(input("Valor a: "))
        b = eval(input("Valor b: "))
        div(a, b)

    if opcion == 4:
        a = eval(input("Valor a: "))
        b = eval(input("Valor b: "))
        multi(a, b)

    if opcion == 5:
        exponente()

    if opcion == 6:
        logaritmo()

    if opcion == 7:
        grados = int(input("Ingresa grados "))
        im= math.sin(math.radians(grados))
        print (" Resultado: ", im)

    if opcion == 8:
        grados = int(input("Ingresa grados "))
        im= math.cos(math.radians(grados))
        print (" Resultado: ", im)

    if opcion == 9:
        tangente()

    if opcion == 10:

    opcion = eval(input("Ingresa opcion"))
