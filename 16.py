nums = []
suma = 0
num = int(input("entera el num : "))
maxim = num
while num != -1 :
     nums.append(num)
     if num >= maxim:
          maxim = num
     num = int(input("entera el num : "))
     
div = []
for e in nums :
     if (maxim % e == 0) and (e != maxim):
          div.append(e)
print(f"{maxim} is the biggest and have divisors {div}")
     