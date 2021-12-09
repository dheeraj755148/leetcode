#kadanes algorithm
nums = [5,4,-1,7,8]
currentSum = nums[0]
maxSum = currentSum

for i in range(1,len(nums)):
    currentSum = max(currentSum + nums[i],nums[i])
    maxSum = max(currentSum,maxSum)
print(maxSum)