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

""" def isValid(s):
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

print(isValid(")(")) """

def valid(s):
    stack = []
    ans =[]
    for i in range(len(s)):
        if (s[i]=="(") or (s[i]=="[") or (s[i]=="{"):
            stack.append(s[i])
            print(stack)
        else:
            if(len(stack)==0):
                return False
            else:
                temp = stack.pop()
                print(temp)
                if (s[i]==")" and temp == "(") or (s[i]=="]" and temp == "[") or (s[i]=="}" and temp == "{"):
                    ans.append(True)
                else:
                    return False
    if len(stack) == 0:
        return True

print(valid("(){}}{"))    
