def nearest_zero(alist):
    '''Return the two numbers (negative and positive)
    that are nearest to zero in a given list

    Parameters:
        alist - a list of numeric values, with both
            positive and negative numbers

    Return Values:
        the two negative and positive values that are nearest
        to zero, with the negative value first.
    '''
    # separate into two lists, positive and negatives,
    # then .... use .sort()!
    # pos_list = []
    # neg_list = []
    # for val in alist:
    #     if val > 0:
    #         pos_list.append(val)
    #     elif val < 0:
    #         neg_list.append(val)
    # pos_list.sort()
    # neg_list.sort()
    # return neg_list[-1], pos_list[0]

    # sort original list .. walk through and find first
    # positive... then that one and one before it
    copylist = alist[:]
    copylist.sort()
    for i in range(len(copylist)):
        if copylist[i] > 0:
            return copylist[i-1], copylist[i]

    # for loop - track "nearest to zero" value
    # maybe we could track negative and positive in one loop


def is_sorted(vals, descending=False):
    '''Test whether list of vals is sorted

    Parameters:
        vals - a list of numeric values

    Return Value:
        True, if sorted, False if not
    '''
    alist = vals[:]
    alist.sort()
    if not descending:
        if vals == alist:
            return True
    else:
        alist.reverse()
        if vals == alist:
            return True
    return False


def main():
    # mylist = [-6,2,-3,7,1,3]
    # print(mylist)
    # n, p = nearest_zero(mylist)
    # print(mylist)
    # print(n) # -3
    # print(p) # 1
    list1 = [1,5,20,30,46]
    list2 = [1,23,7,0]
    list3 = [9,7,2,0]
    print(is_sorted(list1)) # T
    print(is_sorted(list2)) # F
    print(is_sorted(list3)) # F
    print(is_sorted(list3, descending=True)) # T


if __name__ == '__main__':
    main()
