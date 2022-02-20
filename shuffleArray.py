nums = [2, 5, 1, 3, 4, 7]
n = 3

ans = [0]*len(nums)
for i in range(len(nums)):
    if(i % 2 == 0):
        ans[i] = nums[i//2]
    else:
        ans[i] = nums[n+i//2]

print(ans)
