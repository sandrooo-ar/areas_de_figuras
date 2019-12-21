def cuadrado():
    lado = int(input("Enter the measure of one side: "))     
    print(" ") 
    return lado**2

def rectangulo():
    lado_corto = int(input("Enter the measurement of the short side:"))
    lado_largo = int(input("Enter the measurement of the long side: ")) 
    print(" ")   
    return lado_corto*lado_largo

def triangulo():
    altura = int(input("Enter the height measurement: "))
    base = int(input("Enter the measure of the base: "))
    print(" ") 
    return altura*base/2

def rombo():
    diagonal_grande = int(input("Enter the large diagonal measurement: "))
    diagonal_pequeña = int(input("Enter the small diagonal measurement: "))
    print(" ") 
    return diagonal_grande*diagonal_pequeña/2

def romboide():
    base = int(input("Enter the measure of the base: "))
    altura = int(input("Enter the height measurement: "))
    print(" ") 
    return base*altura

def poligono_regular():
    perimetro = int(input("Enter the perimeter of the polygon: "))
    apotema = int(input("Enter how much the apothem measures: "))
    print(" ") 
    return perimetro*apotema/2

def circulo():
    radio = int(input("Enter how much the radius measures: "))
    print(" ") 
    return 3.1416*radio**2

n = 0

while n == 0:
    status = int(input("Enter the number of the figure from which you want to measure the area: \n1.Square \n2.Rectangle \n3.Triangle \n4.Rhombus \n5.Rhomboid \n6.Regular polygon \n7.Circle \n"))
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
        print("\nYou have not entered the number well.\n")

xyz = 0

while xyz == 0:
    x = input("Press enter to exit:  ")
    xyz = 1