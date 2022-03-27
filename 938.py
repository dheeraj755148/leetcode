root = [10,5,15,3,7,"null",18]
low = 7
high = 15
c= 0
for i in root:
    if i>=low and i<=high:
        c += i
print(c)
