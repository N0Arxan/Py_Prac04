nums = []
num = input("enter num: ")
while num != "*":
    nums.append(num)
    num = input("enter num: ")

nums = list(map(int,nums))
print(nums)
ultim = nums.pop()


