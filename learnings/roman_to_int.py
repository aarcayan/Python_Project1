# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# example: MCMXCIV

def romanToInt(s):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                 'CD': 400, 'CM': 900}
        num = 0
        ctr = 0

        while ctr < len(s):
            if s[ctr:ctr+2] in roman:
                num += roman[s[ctr:ctr+2]]
                ctr += 2
            else:
                num += roman[s[ctr:ctr + 1]]
                ctr += 1
        print(num)


romanToInt("MCMXCIV")