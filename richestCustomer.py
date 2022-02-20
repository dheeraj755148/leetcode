account = [[2,8,7],[7,1,3],[1,9,5]]
maxSum = sum(account[0])
for i in range(1,len(account)-1):
    tempSum = max(sum(account[i]),sum(account[i+1]))
    maxSum = max(tempSum,maxSum)
print(maxSum)