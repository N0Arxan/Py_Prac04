nums = input("numeros separat per , :").split(",")
nums= list(map(int,nums))
suma = 0
for num in nums:
    suma += num

print(suma)