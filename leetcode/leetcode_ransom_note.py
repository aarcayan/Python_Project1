
def canConstruct(ransomNote: str, magazine: str) -> bool:
    for i in set(ransomNote):
        print(i)
        if ransomNote.count(i) > magazine.count(i):
            return False
    return True

ransomNote = "aaab"
magazine = "baa"
print(canConstruct(ransomNote,magazine))
