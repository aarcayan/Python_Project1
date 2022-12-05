
def split_string_to_words(strs):
    print(strs)
    strs = strs.split()
    print(type(strs))
    print(strs)
    print(strs[-2])
    dict = {}
    print("")
    print("-----------")
    print("")

    for word in strs:
        print(word,len(word))
        dict[word] = len(word)

    print(dict)



strs = "The Quick Browns Fox Jumps over the Lazy dawg"
print(split_string_to_words(strs))