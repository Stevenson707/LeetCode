def addBinary(a, b):
    a = int(a, 2)
    b = int(b, 2)
    sum = a + b
    return bin(sum)[2:]


print(addBinary("11", "1"))