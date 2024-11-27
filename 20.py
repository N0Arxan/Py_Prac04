types = input("enter types of car seprated with * :").split("*")
contH = 0
print(types)
for type in types:
    for char in type:
        if char == "H":
            contH+=1

mitjana = contH / len(types)

print(f"mitjana is {mitjana}")

for type in types:
    contH = 0
    for char in type:
        if char == "H":
            contH+=1
    if contH > mitjana :
        print(type)

#Exm : DEGH*EEGGHHH*HDG*HHDGEG
#Result : EEGGHHH , HHDGEG