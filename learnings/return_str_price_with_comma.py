# Write a function named 'format_number' that takes a non-negative number as its only parameter.
# Your function should convert the number to a string and add commas as a thousand separators.
# For example, calling format_number(1000000) should return "1,000,000".

def format_number(number):
    if isinstance(number, int) == False:
        return 'Invalid Variable, its not numeric'

    str_number = str(number)[::-1]

    print("initial number:", number)
    print("converted number:",str_number)

    if '-' in str_number:
        return 'Invalid number, its negative number'

    f_str = ""
    ctr = 0

    for i in str_number:
        if ctr == 3:
            f_str += ',' + i
            ctr = 0
        else:
            f_str += i
        ctr += 1
    return f_str[::-1]


print(format_number(2500000))
