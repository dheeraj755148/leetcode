n = 5
start = 0
temp = [0]*n
sol = 0
for i in range(n):
    temp[i] = start + 2*i
for i in range(n):
    sol = sol ^ i

print(sol)