cadena = input("enter la cadena : ")
longitud = len(cadena)
canti = cadena.count("U")
if (longitud/2) < canti:
    print("Si")
else :
    print("No")