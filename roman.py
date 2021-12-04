roman = {"M":1000,"D":500,"C":100,"X":10,"L":50,"V":5,"I":1}
s= input()
z=0
for i in range(0,len(s)-1):
    if(roman[s[i]]<roman[s[i+1]]):
        z = z - roman[s[i]]
    else:
        z= z + roman[s[i]]
z = z +roman[s[-1]]
print(z)