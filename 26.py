cadena = input("enter las sequencies seperat per . :").split(".")
maximA = 0

for seq in cadena:
    contA = 0
    for char in seq:
        if char == "A":
            contA+=1
    if contA > maximA :
        maximA = contA
        seq_con_mas_A = seq

print(seq_con_mas_A)

#Exm: ABCAA.AAAASGA.ASCD.AAA
#Result : AAAASGA