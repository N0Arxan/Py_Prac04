nums = []
suma = 0
num = int(input("entera el num : "))
while num != -1 :
     nums.append(num)
     num = int(input("entera el num : "))
print(nums)
ultim = nums[-1]
nums = [num for num in nums if num % ultim != 0] 
nums.append(ultim)
print(nums)