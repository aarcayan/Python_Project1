
def consecutive_char(strs):
    count = 0
    strs = strs.lower()

    for c in range(len(strs)-1):
        print("c->",strs[c])
        if strs[c] == strs[c+1]:
            print("the same...", strs[c])



consecutive_char("AaBb")