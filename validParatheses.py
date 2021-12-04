""" paran = {"(":0,")":0,"{":0,"}":0,"[":0,"]":0}

x = input()
def valid(x):
    for i in range(len(x)):
        paran[x[i]] =  paran[x[i]] +1
    if ((paran["("]+paran[")"])%2 ==0) and ((paran["{"]+paran["}"])%2 ==0) and ((paran["["]+paran["]"])%2 ==0):
        return "true"
    else:
        return "false" 
print(valid(x)) """

def isValid(s):
    stack = []
    dict = {"]":"[", "}":"{", ")":"("}
    for char in s:
        if char in dict.values():
            stack.append(char)
            #print(stack)
        elif char in dict.keys():
            if stack == [] or dict[char] != stack.pop():
                return False
        else:
            return False
    return stack == []

print(isValid(")("))