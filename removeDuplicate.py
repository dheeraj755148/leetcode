nums = [0,0,1,1,1,2,2,3,3,4]
unique = 1

for i in range(1,len(nums)):
    if nums[i] == nums[i-1]:
        continue
    else:
        nums[unique] = nums[i]
        unique +=1
for k in range(unique,len(nums)):
    nums[k]="_"

print(str(unique)+", nums = "+str(nums))