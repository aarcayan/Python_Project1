import collections
from collections import Counter

def receiver_func(alphabetic):
    duplicate = []
    single = []
    total_dup = 0

    for char in alphabetic:
        if char.isdigit() == True:
            print('has numbers')
            return False
        single.append(char)
        if char in single:
            duplicate.append(char)
            total_dup += 1

    print(single)
    print(duplicate)
    print('total_dup: {}'.format(total_dup))

    for i in duplicate:
        print(duplicate.count(i))

def get_reapating(strs):
    print('Len:{}',format(len(strs)))

    for char in strs:
        if char.isdigit():
            print('only alpabetic characters needed...')
            return False
    reps_list = []
    reps_dict = {}
    repeated_str = collections.Counter(str(strs).lower())
    print(repeated_str)
    for k,v in repeated_str.items():
        if v > 1:
            print('this Key ({}) has multiples:{}'.format(k,v))
            reps_dict[k] = v
            reps_list.append(k)

    print('----repeated list----')
    print(reps_dict)
    print(reps_list)
    print('---------------------')

def remove_dups(dlist):
    print("This is the List:", dlist)
    udlist = list(dict.fromkeys(dlist))
    print("This is the unique list:-> ",udlist)


def collections_path2(characters):
    for char in characters:
        if char.isdigit():
            print('has numbers')
            return False
    characters = characters.upper()
    dict = Counter(characters)
    strDuplicate = ""
    total_dups = 0
    for k,v in dict.items():
        if v > 1:
            strDuplicate += k
            total_dups += v
    print(total_dups)
    if total_dups > (len(characters)/2):
        print ('the total_dups({}) > half of the len({})'.format(total_dups,len(characters)))
        return strDuplicate.lower()
    else:
        return None


def collections_path(characters):
    dict = Counter(characters)
    print(dict)
    strlst = ""
    total_dups = 0
    for k,v in dict.items():
        if v > 1:
            strlst += (str(k).lower())
            strlst += (str(k).upper())
            total_dups += v
    print(total_dups)
    print(strlst)


# print(collections_path2('abcdefghijkab'))
# print(collections_path2('aAbCdCeFEGgHijKk'))
# collections_path('abcdeffghiiijka')
# receiver_func('abac')


