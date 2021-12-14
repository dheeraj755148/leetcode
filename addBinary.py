a = "11"
b = "1"
sum = ""
carry = 0
temp = max(len(a), len(b))
a = a.zfill(temp)
b = b.zfill(temp)
for i in range(1, temp+1):
    if(int(a[-i])+int(b[-i])+carry) % 2 == 0:
        if a[-i] == "1" and b[-i] == "1":
            carry = 1
        sum = sum + "0"
    else:
        if a[-i] == "1" and b[-i] == "1":
            carry = 1
        else:
            carry = 0
        sum = sum + "1"
if carry:
    print(str(carry)+sum[::-1])
else:
    print(sum[::-1])
