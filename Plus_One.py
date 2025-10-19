def plusOne(digits):
    s = ""
    for i in digits:
        s += str(i)
    s = str(int(s) + 1)
    lst = []
    for i in s:
        lst.append(int(i))
    return lst


print(plusOne([1, 2, 3]))
