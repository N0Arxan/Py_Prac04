voltes = []
cont = 0
suma = 0
num = 0
while cont != 10:
     num = int(input("entera el volt : "))
     voltes.append(num)
     suma += num 
     cont += 1
 
x = suma / cont
print(f" {suma} / {cont} = {x} ")
suma = 0
for elem in voltes :
    dif = (elem - x)**2
    suma += dif
print(f"alpha2 = {suma} / {cont} = {suma / cont}")
