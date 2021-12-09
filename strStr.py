def hay():
    haystack = "mississippi"
    needle = "issip"
    if needle == "":
        return 0
    if len(needle) > len(haystack):
        return -1
    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            temp = i+1
            x=i
            for j in range(1, len(needle)):
                if haystack[temp] == needle[j]:
                    print(temp)
                    temp += 1
                else:
                    break
    return x
    return -1


print(hay())
