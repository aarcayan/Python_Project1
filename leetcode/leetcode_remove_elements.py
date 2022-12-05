
#with create new list array
def removeElement_new_list(nums: list[int], val: int):
    new_nums = []
    ctr = 0
    for n in nums:
        if n != val:
            new_nums.append(n)
            ctr += 1
    print(ctr)
    return new_nums

def removeElement_try_catch(nums: list[int], val: int):
    ctr = 0
    while val in nums:
        nums.remove(val)
        ctr += 1
    return len(nums)

# def removeElement(nums: list[int], val: int):
#     while True:
#         try:
#             nums.remove(val)
#         except:
#             break
#     print(nums)
#     return len(nums)


nums =[0,1,2,2,3,0,4,2] # expected -> [0,1,3,0,4]
val = 2
print(removeElement_try_catch(nums,val))