
def get_single_number(nums: list[int]):
    if len(nums) == 1:
        return nums[0]
    d_nums = {}
    for n in range(len(nums)):
        if nums[n] in d_nums:
            d_nums[nums[n]] += 1
        else:
            d_nums[nums[n]] = 1
    return min(d_nums,key=d_nums.get)



nums = [4,1,2,1,2]
print(get_single_number(nums))
