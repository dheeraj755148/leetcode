operations = ["++X","++X","X++"]
X = 0
for i in operations:
    if(i.startswith("-") or i.endswith("-")):
        X-=1
    else:
        X+=1

print(X)