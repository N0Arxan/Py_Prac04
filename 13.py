nums = []
num = input("enter num: ")
while num != "*":
    nums.append(num)
    num = input("enter num: ")

nums = list(map(int,nums))
print(nums)
ultim = nums[-1]

i = 0 
multiple = 0
while (i != len(nums)-1) and (not(multiple)):
     if nums[i] % ultim == 0:
          multiple = nums.pop(i)
     i += 1

print(nums , multiple)