candies = [4,2,1,1,2]
extraCandies = 1
ans = []
for i in range(len(candies)):
    candies[i] = candies[i] + extraCandies
    temp = max(candies)
    if(temp==candies[i]):
        ans.append(True)
    else:
        ans.append(False)
    candies[i] = candies[i] - extraCandies
print(ans)