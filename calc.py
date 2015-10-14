def suma(a, b):
    return a + b

def resta():
        try:
                num01 = eval(input("Número 01: "))
                num02 = eval(input("Número 02: "))
                #aux = num01 - num02    
                print ("La resta es: ", int(num01 - num02))
                #return nombres
        except excepcion:
                print("Ha ocurrido un error!")


def div(num1, num2):
	try:
		res = num1 / num2
		print (" Resultado: ", res)
	except ZeroDivisionError:
		print ("Error: Divicion entre cero ")

def multi(a, b):
    return a * b

def logaritmo():
	try:
 		num01 = eval(input("Logaritmo: "))
        	num02 = eval(input("Base: "))
        	aux = math.log(num01, num02)
        	print ("El resultado es: ", float(aux))
	except error:
		print("Ha ocurrido un error!")

opcion = 0
while opcion != 12:
    print ('{:^16}'.format('Calculadora'))
    print ('{:^16}'.format('1. Suma'))
    print ('{:^16}'.format('2. Resta'))
    print ('{:^16}'.format('3. Division'))
    print ('{:^16}'.format('4. Multiplicacion'))
    print ('{:^16}'.format('5. Division'))
    print ('{:^16}'.format('6. Exponente'))
    print ('{:^16}'.format('7. Log'))
    print ('{:^16}'.format('8. Seno'))
    print ('{:^16}'.format('9. Coseno'))
    print ('{:^16}'.format('10. Tangente'))
    print ('{:^16}'.format('11. Inverso'))
    print ('{:^16}'.format('12. Salir'))
    if opcion == 1:
        a = eval(input("Valor a: "))
        b = eval(input("Valor b: "))
        suma(a, b)

    if opcion == 3:
        a = eval(input("Valor a: "))
        b = eval(input("Valor b: "))
        div(a, b)

    if opcion == 4:
        a = eval(input("Valor a: "))
        b = eval(input("Valor b: "))
        multi(a, b)
        
    opcion = eval(input("Ingresa opcion"))
