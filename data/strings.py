
def remove_char_in_strings(strs :str,rem):
    print("initial string: [", strs, "] - Char to remove->", rem)
    strs = strs.replace(rem,"")
    print(strs)



strs = "abcdefghijkgghigg"
print(remove_char_in_strings(strs,'g'))