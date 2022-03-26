n=234
multpl = 1
sum_temp = 0

while(n>0):
    r = n%10
    multpl = multpl * r
    sum_temp = sum_temp + r
    n=n//10
print(multpl-sum_temp)