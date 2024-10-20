def isPolindrome(x):
    flag = False
    line_of_x = str(x)
    lenght = len(line_of_x)
    count = 1
    for i in range(lenght):
        if line_of_x[i] == line_of_x[lenght - count]:
            flag = True
            count += 1
        else:
            flag = False
            return flag
    return flag
