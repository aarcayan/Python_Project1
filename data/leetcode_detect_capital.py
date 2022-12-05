
def detectCapitalUse(word: str) -> bool:
    return word[1:] == word[1:].lower() or word == word.upper() or word == word.istitle()




# word = "FlaG"
word = 'x'
print(detectCapitalUse(word))