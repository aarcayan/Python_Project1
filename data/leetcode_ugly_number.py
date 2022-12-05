# https://leetcode.com/problems/ugly-number/

# num -> 6
# prime: 2
# prime: 3
# prime: 5

def isUgly(n: int) -> bool:
    if n < 0:
        return False

    for p in [2,3,5]:
        print("")
        print("number-n:",n)
        print("factor-P:",p)
        while n % p == 0:
            n = n // p
            print("new n:",n)
    return n == 1


n = 14
print(isUgly(n))