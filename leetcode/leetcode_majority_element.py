# https://leetcode.com/problems/majority-element/


def majorityElement(nums: list[int]) -> int:
    from collections import Counter
    max_value, max_key = 0, 0
    for k,v in Counter(nums).items():
        if v > max_value:
            max_value = v
            max_key = k
    return max_key






# nums = [2, 2, 1, 1, 1, 2, 2]
nums = [3,3,4]
print(majorityElement(nums))