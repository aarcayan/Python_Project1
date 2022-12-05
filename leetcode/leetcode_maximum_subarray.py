
def get_max_subArray(nums: list[int]):
    max_subarr = nums[0]
    current_sum = 0

    for n in nums:
        if current_sum < 0:
            print("set back to zero current_sum")
            current_sum = 0
        current_sum +=n
        print("current_sum[",n,"]->",current_sum)
        max_subarr = max(max_subarr,current_sum)
    print("max_subarr:",max_subarr)
    return max_subarr


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(get_max_subArray(nums))
