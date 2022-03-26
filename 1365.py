nums = [8,1,2,2,3]
temp = sorted(nums)
mapping = {}
result = []
for i in range(len(temp)):
    if temp[i] not in mapping:
        mapping[temp[i]] = i
for i in range(len(nums)):
    result.append(mapping[nums[i]])
print(result)


