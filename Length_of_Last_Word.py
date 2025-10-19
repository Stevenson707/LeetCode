def lengthOfLastWord(s):
    lst = s.split()
    return len(lst[-1])


print(lengthOfLastWord("   fly me   to   the moon  "))