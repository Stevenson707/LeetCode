def strStr(haystack, needle):
    if needle in haystack:
        for i in range(len(haystack)):
            if haystack[i:len(needle) + i] == needle:
                return i
    else:
        return -1


print(strStr("sadbutsad", "sad"))