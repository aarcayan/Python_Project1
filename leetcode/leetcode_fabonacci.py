
def getserries(num):
    before_num = 0
    next_num = 1
    total_number = 0
    fabnum = []
    for i in range (num):
        print(before_num)
        fabnum.append(before_num)
        total_number += before_num
        temp_num = before_num
        before_num = next_num
        next_num = temp_num + before_num

    print("Total Number Sum: {}".format(total_number))
    print("Fabo List: {}".format(fabnum))
    print("Fn for n =",fabnum[-1] + fabnum[-2])

num = int(input("Please input a number: "))
if num < 1:
    print('invalid number...')
else:
    getserries(num)

