list = input("enter una llista sperat per spai : ").split()
new_list=[]
for e in list :
    if not(e in new_list):
        new_list.append(e)
print(new_list)