def processArray():
    for i in range(len(a)):
        char = str(a[i])
        if char[-1]=="4" and int(a[i])<53:
            a[i]=-9
        elif char[-1]=="4":
            a[i] = -7
        elif int(a[i])<53:
            a[i]= -1

a=[]
while(True):
 x=int(input())
 if x>0:
  a.append(str(x))
 else:
  break

for i in range(len(a)):
 print(int(a[i]))