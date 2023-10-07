def linear_search(alist, target):
    '''Purpose: Find index of target in alist
    '''
    i = 0
    length = len(alist)
    while i < length:
        if alist[i] == target:
            return i
        i = i + 1
    return -1

def binary_search(lst, target, low, high):
    '''Purpose: Finds index of target in lst,
    assuming lst is already sorted
    '''
    range_size = (high - low) + 1
    mid = (high + low) // 2

    if target == lst[mid]:  # Base case 1: Found at mid
        pos = mid
    elif range_size == 1:  # Base case 2: Not found
        pos = -1
    else:  # Recursive search: Search lower or upper half
        if target < lst[mid]:  # Search lower half
            pos = binary_search(lst, target, low, mid)
        else:  # Search upper half
            pos = binary_search(lst, target, mid+1, high)

    return pos

def selection_sort(lst):
    '''Purpose: sort lst using plan #1
    '''



def find_min_index(lst, startindex):
    '''find the index of min item starting at startindex'''
    min_value = float('Inf')
    min_index = -1
    i = startindex
    while i < len(lst):
        if lst[i] < min_value:
            min_value = lst[i]
            min_index = i
        i += 1
    return min_index




def main():
    mylist = [1,4,7,22,54,61,62]
    loc1 = linear_search(mylist, 54)
    print(loc1)
    loc2 = binary_search(mylist, 54, 0, len(mylist))
    print(loc2)

if __name__ == '__main__':
    main()
