
def reverse_string(s: list[str]):
    print("Initial string:", s)

    l_ptr, r_ptr = 0, len(s) - 1

    while l_ptr < r_ptr:
        s[l_ptr] , s[r_ptr] = s[r_ptr] , s[l_ptr]
        l_ptr ,r_ptr = +1 ,-1
    return s



strs = ["H" ,"e" ,"l" ,"l" ,"o"]

print(reverse_string(strs))
