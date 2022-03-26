encoded = [1,2,3]
first = 1
ans = []

ans.append(first)

for i in range(len(encoded)):
    temp = first^encoded[i]
    ans.append(temp)
    first=temp

print(ans)
        
