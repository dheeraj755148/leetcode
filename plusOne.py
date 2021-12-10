digits = [1,2,9]

count = 0
if digits[-1]<9:
    digits[-1]+=1
else:
    for i in range(1,len(digits)+1):
        if digits[-i]>=9:
            digits[-i]=0
            count = count + 1
            if count == len(digits):
                digits.insert(0,1) 
            else:
                temp = digits[-i-1]
                digits[-i-1]+=1
                if temp<9:
                    break
                else:continue

print(digits)