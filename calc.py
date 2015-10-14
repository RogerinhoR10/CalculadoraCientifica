def suma(a, b):
    return a + b

opcion = eval(input("Ingresa opcion"))
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
    opcion = eval(input("Ingresa opcion"))
