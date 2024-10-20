def romanToInt(s):
    d = {
        'I': '1',
        'V': '5',
        'X': '10',
        'L': '50',
        'C': '100',
        'D': '500',
        'M': '1000',
        'IV': '4',
        'IX': '9',
        'XL': '40',
        'XC': '90',
        'CD': '400',
        'CM': '900'
    }
    answer = 0
    if 'IV' in s:
        answer += int(d['IV'])
        s = s.replace('IV', '', 1)
    if 'IX' in s:
        answer += int(d['IX'])
        s = s.replace('IX', '', 1)
    if 'XL' in s:
        answer += int(d['XL'])
        s = s.replace('XL', '', 1)
    if 'XC' in s:
        answer += int(d['XC'])
        s = s.replace('XC', '', 1)
    if 'CD' in s:
        answer += int(d['CD'])
        s = s.replace('CD', '', 1)
    if 'CM' in s:
        answer += int(d['CM'])
        s = s.replace('CM', '', 1)

    for i in s:
        answer += int(d[i])
    return answer


print(romanToInt('MCMXCIV'))