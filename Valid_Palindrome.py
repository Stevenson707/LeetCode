def isPalindrome(s):
    # 0 ms
    import re
    s = s.lower()
    s = re.sub(r'[^A-Za-z0-9]', '', s)
    return s == s[::-1]

    # my solution (732 ms)
    # import string
    # s = s.lower()
    # for i in s:
    #     if i in string.punctuation + " ":
    #         s = s.replace(i, "")
    # if s == s[::-1]:
    #     return True
    # return False


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))