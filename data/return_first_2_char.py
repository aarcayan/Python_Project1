# def substring_copy(str, n):
#     flen = 2
#     if flen > len(str):
#         flen = len(str)
#     substr = str[:flen]
#
#     result = ""
#     for i in range(n):
#         result = result + substr
#     return result
#
#
# print(substring_copy('abcdef', 2))
# print(substring_copy('p', 3));
# print(substring_copy('abc', 1));


def atoi(s):
    rtr=0
    for c in s:
        rtr=rtr*10 + ord(c) - ord('0')
    return rtr

def add_2_strings(str1,str2):
    num1 = atoi(str1)
    print(num1)
    num2 = atoi(str2)
    print(num2)
    resultNum = num2 + num1
    print(resultNum)

def atoi2(str):
    ret_num = 0

    for c in str:
        if not c.isdigit():
            print("this is not a digit... invalid...")
            return None
        ret_num = ret_num*10 + ord(c) - ord('0')
        print(ret_num)
    return ret_num


# x = add_2_strings("100","20")
# print(x)

x2 = atoi2('201')
print("x2: ",x2)

