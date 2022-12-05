
def single_number(nums: list[int]):
    print("initial nums: ",nums)
    res = 0
    for n in nums:
        print(n)
        res = n ^ res
        print("res:",res)
    return res


nums = [3,2,2,3,1]
print("Single Number: ", single_number(nums))
