
def isAnagram(str1: str, str2: str):
    if len(str1) != len(str2):
        return False

    dict_s, dict_s2 = {},{}

    for s in range(len(str1)):
        dict_s[str1[s]] = 1 + dict_s.get(str1[s],0)
        dict_s2[str2[s]] = 1 + dict_s2.get(str2[s],0)

    for s in dict_s:
        if dict_s[s] != dict_s2.get(s,0):
            return False

    return True


s1 = "amalxgam"
s2 = "maglxama"

print(isAnagram(s1,s2))