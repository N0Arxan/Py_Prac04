nums = []
num = input("enter num: ")
while num != "*":
    nums.append(num)
    num = input("enter num: ")

nums = list(map(int,nums))
print(nums)

for i in range(0,len(nums)) :
    if nums[i] % 2 == 0:
        nums[i]= nums[i]**2
    else :
        nums[i] = nums[i]**3
print(nums)