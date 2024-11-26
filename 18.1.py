nums = []
num = ""
conta_num = 0
conta_afins = 0
while conta_num < 10:
    num = input("enter num: ")
    nums.append(num)
    conta_num += 1 

nums = list(map(int,nums))
ultim = nums.pop()
for e in nums:
    if (e % 10) + (e // 10) == (ultim % 10) + (ultim // 10):
        conta_afins += 1
print(conta_afins) 