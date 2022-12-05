
def maximumWealth(accounts):
    max_sum = sum(accounts[0])
    for i in range(1,len(accounts)):
        if max_sum < sum(accounts[i]):
            max_sum = sum(accounts[i])
    return max_sum


accounts = [[1,2,3],[3,2,1]]
print(maximumWealth(accounts))