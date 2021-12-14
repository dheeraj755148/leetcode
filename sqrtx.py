x=8
l=1
h=x
if (x==0 or x==1):
    print (x)
while(l<h):
    mid = (l+h)//2
    if (mid*mid == x):
        print(mid)
        break
    elif mid*mid >x:
        h=mid
    elif mid*mid<x:
        l=mid+1
print(l-1)