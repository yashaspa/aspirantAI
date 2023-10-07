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

def pairs(lst):
    '''count how many pairs (i.e. equal items)
    are in a given list.
    note: [1,7,7,7,2] counts as 3 pairs
    '''
    paircount = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i] == lst[j]:
                paircount += 1
    return paircount // 2
    # O(n**2)


def glorious(num):
    '''Determines whether num is glorious or not
    '''
    for i in range(10, 51):
        if num % i == 0:
            return False
    return True
    # O(1)

def count_glorious_lst(lst):
    '''Count how many glorious numbers are in
    the given list
    '''
    total = 0
    for j in lst:
        if glorious(j):
            total += 1
    return total
    # O(n)

def items_at_index(lst):
    '''Given a sorted list of ints lst,
    count how many items are at the index that
    matches their value. (i.e. value 8 is at index 8)
    '''
    count = 0
    for val in lst:
        location = binary_search(lst, val, 0, len(lst)-1)
        if val == location:
            count += 1
    return count
    # O(n log n)

def count_evens(lst):
    '''count how many 2s, 4s, 6s, and 8s appear in
    the given list lst
    '''
    return (lst.count(2) + lst.count(4) +
            lst.count(6) + lst.count(8))
    # O(n)
