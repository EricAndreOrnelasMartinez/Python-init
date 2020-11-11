angle1 = int(input("insert the first angle:     "))
angle2 = int(input("insert the second angle:    "))
angle3 = int(input("insert the last angle:      "))
add = angle1 + angle2 + angle3

if add == 180 :
    if angle1 == angle2 and angle1 == angle3 and angle3 == angle2 :
        print("Es equilatero")
    elif angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("Es rectangulo")
    elif angle1 == angle2 or angle1 == angle3 or angle3 == angle2 :
        print("Es isoseles")
    elif angle1 != angle2 and angle1 != angle3 and angle3 != angle2:
        print("Es escaleno")
else :
    print("no es un triangulo")
