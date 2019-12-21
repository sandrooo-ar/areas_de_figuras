def cuadrado():
    lado = int(input("Introduce cuanto mide un lado: "))     
    print(" ") 
    return lado**2

def rectangulo():
    lado_corto = int(input("Introduce cuanto mide el lado corto: "))
    lado_largo = int(input("Introduce cuanto mide el lado largo: ")) 
    print(" ")   
    return lado_corto*lado_largo

def triangulo():
    altura = int(input("Introduce cuanto mide la altura: "))
    base = int(input("Introduce cuanto mide la base: "))
    print(" ") 
    return altura*base/2

def rombo():
    diagonal_grande = int(input("Introduce cuanto mide la diagonal grande: "))
    diagonal_pequeña = int(input("Introduce cuanto mide la diagonal pequeña: "))
    print(" ") 
    return diagonal_grande*diagonal_pequeña/2

def romboide():
    base = int(input("Introduce cuanto mide la base: "))
    altura = int(input("Introduce cuanto mide la altura: "))
    print(" ") 
    return base*altura

def poligono_regular():
    perimetro = int(input("Introduce el perímetro del polígono: "))
    apotema = int(input("Introduce cuanto mide el apotema: "))
    print(" ") 
    return perimetro*apotema/2

def circulo():
    radio = int(input("Introduce cuanto mide el radio: "))
    print(" ") 
    return 3.1416*radio**2

n = 0

while n == 0:
    status = int(input("Introduce el número de la figura de la cual quieres medir el área:\n1.Cuadrado\n2.Rectángulo\n3.Triángulo\n4.Rombo\n5.Romboide\n6.Polígono regular\n7.Círculo\n"))
    print(" ")
    if status == 1:
        print(cuadrado())
        n = 1
    
    elif status == 2:
        print(rectangulo())
        n = 1
    
    elif status == 3:
        print(triangulo())
        n = 1

    elif status == 4:
        print(rombo())
        n = 1

    elif status == 5:
        print(romboide())
        n = 1

    elif status == 6:
        print(poligono_regular())
        n = 1

    elif status == 7:
        print(circulo())
        n = 1

    else:
        print("\nNo has introducido el número bien.\n")

