def longestCommonPrefix(strs: list[str]):
    if not strs:
        return ""
    shortest = min(strs, key=len)
    for i in range(len(shortest)):
        print(shortest[i])
        for other in strs:
            if other[i] != shortest[i]:
                return shortest[:i]


    # for i, ch in enumerate(shortest):
    #     print(i, ch)
    #     for other in strs:
    #         print(other)
    #         if other[i] != ch:
    #             return shortest[:i]
    return shortest


strs = ["flower","flow","flight"]
# strs = ["fgower","flow","fdight"]
print(longestCommonPrefix(strs))
