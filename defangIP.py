address = "1.1.1.1"
defang = ""
for i in address:
    if i == ".":
        defang += "[.]"
    else:
        defang += i
print(defang)