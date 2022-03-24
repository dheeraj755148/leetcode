""" def findTarget(a,n):
    if(0<=a[0]):
        return a[0]
    if(0>=a[n-1]):
        return a[n-1]
    low = 0
    high = n
    mid = 0

    while(low<high):
        mid = (low+high)//2
        if(a[mid]==0):
            return a[mid]
        
        if(0<a[mid]):
            if(mid>0 and 0>a[mid-1]):
                return getClose(a[mid-1],a[mid])
            high =mid
        else:
            if(mid<n-1 and 0<a[mid+1]):
                return getClose(a[mid],a[mid+1])
            low = mid+1
    return mid+1

def getClose(val1,val2):
    if(0-val1 >=val2-0):
        return val2
    else:
        return val1

a = [0,2,3,4,5]
a.sort()
n = len(a)

print(findTarget(a,n)) """





""" a=[0,4,0,0,1,3,4,1,0,2]
t=a[:]
a.sort()
good = 0
bad = 0
for i in range(len(a)):
    if(t[i]==a[i]):
        good += t[i]
    else:
        bad += t[i]
print(good-bad) """


