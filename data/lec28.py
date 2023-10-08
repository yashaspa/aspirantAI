def sum_n_to_1(n):
    '''Purpose: calculate sum of
     n + (n-1) + (n-2) + ... + 1
     recursively.

    Parameter:
        n - an int greater than or equal to 1
    '''
    if n == 1:
        return 1
    else:
        total = n + sum_n_to_1(n - 1)
        ###          ^^^^ 1+2+ ... + (n-1)
        return total

def find(lst, item, low, high):
    """
    Finds index of string in list of strings, else -1.
    Searches only the index range low to high
    Note: Upper/Lower case characters matter

    (From zybooks reading)
    """
    range_size = (high - low) + 1
    mid = (high + low) // 2

    if item == lst[mid]:  # Base case 1: Found at mid
        pos = mid
    elif range_size == 1:  # Base case 2: Not found
        pos = -1
    else:  # Recursive search: Search lower or upper half
        if item < lst[mid]:  # Search lower half
            pos = find(lst, item, low, mid)
        else:  # Search upper half
            pos = find(lst, item, mid+1, high)

    return pos

def sum_list(lst):
    '''Purpose: Recursively add up all numbers in a list
    i.e. sum_list([6,-2,0,1]) -> 5

    Parameter:
        lst - a list containing numeric values

    Return Value:
        the sum
    '''
    # base case?
    if len(lst) == 0:
        return 0
    else:
        # recursive case?
        #last = lst.pop()
        #return last + sum_list(lst)
        return lst[0] + sum_list(lst[1:])

def sum_nested_list(lst):
    '''Purpose: Recursively add up all numbers in a
    list that may contain nested lists (which also
    may contain nested lists, etc)
    i.e. sum_nested_list([6, -2, [3, 1], [2, [3]]]) -> 13

    Parameter:
        lst - a list containing numeric values or
            other nested lists with numeric values

    Return Value:
        the sum
    '''
    if type(lst[0]) == int:
        total = lst[0] + sum_nested_list(lst[1:])
        #???

def main():
    #print(sum_n_to_1(3))
    alist = [6,-2,0,1]
    print(sum_list(alist))
    print(alist)

if __name__ == '__main__':
    main()
