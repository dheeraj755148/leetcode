nums = [1,2,3,4]
ans = [0]*len(nums)
for i in range(len(ans)):
    sum =0
    for j in range(i+1):
        sum = sum + nums[j]
    ans[i] = sum
print(ans)