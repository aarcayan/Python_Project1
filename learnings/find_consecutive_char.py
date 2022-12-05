
# aAaBbBcdeee
# aaabbbcdeee
def count_chars(s):
    print("")
    print("----count_chars---")
    print("Initial string (lowered):", s.lower())
    s = s.lower()
    count, total_dups = 1,0
    total_char = ""
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            if count > 1:
                total_dups += count
                total_char += s[i-1]*count
            count = 1
    if count > 1:
        total_dups += count
        total_char += s[i - 1] * count

    print("Total chars: ",total_char)
    print("Total dups : ",total_dups)
    if total_dups > len(s)/2:
        return total_dups
    else:
        return None


def my_count_chars(s):
    print("")
    print("----my_count_chars---")
    print("Initial string (lowered):", s.lower())
    count = 1
    total_count = 0
    total_chars = ""
    s = s.lower()
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            if count > 1:
                total_count += count
                total_chars += s[i]*count
            count = 1
    if count > 1:
        total_chars += s[i] * 2


    print("Total chars: ",total_chars)
    print("Total dups : ",total_count)

    if total_count > len(s)/2:
        return total_chars
    else:
        return None


def count_repeating_char(s):
    from collections import Counter
    print("Initial string: ",s)

    s_counter = Counter(s)
    print(s_counter)
    print(max(s_counter))
    print(min(s_counter))




# s = "aAaBcdEeefgHhiijkKk"
s = "aAaBbBcdeee"
# s = "AAAaaa"

print(count_chars(s))
print(my_count_chars(s))
# print(count_repeating_char(s))