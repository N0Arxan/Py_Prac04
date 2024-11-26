nums = input("enter 10 numeros separat per spai : ").split()
nums = list(map(int,nums))
ultim = nums.pop()
cont = 0
for e in nums :
    if (e % 10) + (e // 10) == (ultim % 10) + (ultim // 10):
        cont += 1 
print(nums)
print(cont)