
def get_plus_one(digits : list[int]):

    result = []
    sum_c = ""
    for d in digits:
        sum_c += str(d)
    sum_c = str(int(sum_c) + 1)
    for c in sum_c:
        result.append(c)
    return result

digits = [4,3,2,1]
print(get_plus_one(digits))