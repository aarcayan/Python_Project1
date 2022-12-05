
def isPalindrome(x):
    num_orig = str(x)
    num_str = str(x)[::-1]
    if len(num_str) != 3:
        return False
    if '-' in num_str:
        return False
    if num_str == num_orig:
        return True
    else:
        return False

def reg_exp_matching(strA,strP):
    for strtemp in strA:
        print(strtemp)
        if '*' in strP:
            print(" * should find anything")
            return True
        if strtemp == strP:
            print('strP pattern in strA')
            return True
    return False


# check for palindrom string
def isPalindrome2(s):
    s2 = ""
    for c in s:
        if c.isalnum():
            s2 += c.lower()
    s = s.lower().replace(" ","").replace(",","").replace(":","")
    print(s)
    print(s2[::-1])
    return s2 == s2[::-1]

def my_palindrom(s):
    s2 = ""
    s = s.lower().replace(" ", "").replace(",", "").replace(":", "")
    ctr = len(s)
    while ctr > 0:
        s2 += s[ctr-1]
        ctr -= 1

    print("old string:",s)
    print("new string:",s2)
    if s2 == s:
        return True
    else:
        return False


strs = "A man, a plan, a canal: Panama"
# strs = "cat"

# print(isPalindrome2(strs))
# print(isPalindrome(-12))
print(my_palindrom(strs))