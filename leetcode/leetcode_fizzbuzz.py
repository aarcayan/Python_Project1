
def fizzBuzz(n: int):
    nums = []
    i = 1
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            nums.append("FizzBuzz")
        elif i % 3 == 0:
            nums.append("Fizz")
        elif i % 5 == 0:
            nums.append("Buzz")
        else:
            nums.append(i)
        i += 1
    return nums


fizzBuzz(3)
