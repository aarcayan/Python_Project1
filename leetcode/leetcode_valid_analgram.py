# https://leetcode.com/problems/valid-anagram/

def isAnagram(s: str, t: str) -> bool:
    from collections import Counter
    return Counter(s) == Counter(t)



# s = "rat"
# t = "car"

s = "a"
t = "ab"

# s = "anagram"
# t = "nagaram"

print(isAnagram(s,t))
