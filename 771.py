jewels = "aA"
stones = "aAAbbbb"
c=0
for i in range(len(jewels)):
    for j in stones:
        if jewels[i]==j:
            c+=1
print(c)