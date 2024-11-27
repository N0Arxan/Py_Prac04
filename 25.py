nums = input("enter nums seperated with (,) : ").split(",")
nums = list(map(int,nums))
ultim = nums.pop()
cont = 0
for num in nums :
    if num > ultim:
        cont += 1
print(cont)