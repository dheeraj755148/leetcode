# pascal triangle


def pascalRow(key):

    p = [[1], [1, 1]]

    if key == 1:
        return [p[0]]
    if key == 2:
        return p
    else:
        ans = []
        temp = p[1]
        count = 2
        while(key != count):
            ans.append(1)
            for i in range(len(temp)-1):
                ans.append(temp[i]+temp[i+1])
            ans.append(1)
            p.append(ans)
            ans = []
            count += 1
            temp = p[count-1]
    return p[-1]


print(pascalRow(207))
