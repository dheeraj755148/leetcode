def sumation(x):
    if x<1:
        return x
    return x +sumation(x-1)

x = int(input("Enter an integer => "))

print(sumation(x))