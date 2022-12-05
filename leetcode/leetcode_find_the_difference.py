
def findTheDifference(s: str, t: str) -> str:
    s, t = sorted(s), sorted(t)
    for t1 in t:
        if t1 not in s or s.count(t1) < t.count(t1):
            return t1
    return ""

# s = "abcd"
# t = "abcde"
s = "a"
t = "aa"
print(findTheDifference(s,t))