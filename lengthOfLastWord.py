s = "    day"
print(s)
k = s.strip()
value = ""
if len(k) == 1:
    print("1")
else:
    for i in range(1, len(k)+1):
        if ord(k[-i]) != 32:
            value += k[-i]
        else:
            break
    print(len(value))
