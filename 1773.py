items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"
c = 0
for i in range(len(items)):
    if ruleKey=="color":
        if items[i][1]==ruleValue:
            c +=1
    elif ruleKey=="type":
        if items[i][0]==ruleValue:
            c +=1
    elif ruleKey=="name":
        if items[i][2]==ruleValue:
            c +=1
print(c)
        