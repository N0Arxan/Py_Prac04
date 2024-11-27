trp = input("enter tripletes separat amb * : ").split("*")
print(trp)
trp.sort(key=str.upper)
print(trp)
cadena =""
for e in trp :
    cadena += e
    cadena += " "
print(cadena)