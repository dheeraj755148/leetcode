s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
ans = [0]*len(indices)
print(ans)
for i in range(len(indices)):
    ans[indices[i]] = s[i]
print("".join(ans))