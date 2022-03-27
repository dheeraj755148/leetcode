nums = [0,1,2,3,4]
index = [0,1,2,2,1]
ans = []
for i in range(len(nums)):
    ans.insert(index[i],nums[i])

print(ans)