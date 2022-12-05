
def get_two_sum(nums,target):

    for ptr_a in range(len(nums)):
        for ptr_b in range(ptr_a +1,len(nums)):
            if nums[ptr_a] + nums[ptr_b] == target:
                # return nums[ptr_a],nums[ptr_b]
                return ptr_a,ptr_b


nums = [10,8,2,7,11,15,5]
target = 9

print(get_two_sum(nums,target))