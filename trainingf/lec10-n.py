def count_down(n):
    '''Recursively count down from n
    '''
    if n == 0:
        print('Go!')
    else:
        print(n)
        count_down(n-1)

def count(n):
    if n == 0:
        print('Go!')
    else:
        count(n-1)
        print(n)

def count_up_to_100(n):
    '''Purpose: Recursively count up to 100 from n

    Parameter:
        n - an int less than or equal to 100
    '''
    if n == 100:
        print(n)
        print('Got there!')
    else:
        print(n)
        count_up_to_100(n+1)

def sum_n_to_1(n):
    '''Purpose: calculate sum of
     n + (n-1) + (n-2) + ... + 1
     recursively.

    Parameter:
        n - an int greater than or equal to 1

    Return Value:
        the sum of those numbers
    '''
    # recursive find the sum of this series
    # base case?
    if n == 1:
        return 1
    else:
        total = n + sum_n_to_1(n-1)
        #            ^^^^ someone else do 1+2+...+(n-1)
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
    if len(lst) == 1:
        return lst[0]
    else:
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
    # if len(lst) == 1 and type(lst[0]) == int:
    #     return lst[0]
    # elif len(lst) == 1 and type(lst[0]) == list:
    #     return sum_nested_list(lst[0])
    # elif type(lst[0]) == int:
    #     return lst[0] + sum_nested_list(lst[1:])
    # elif type(lst[0]) == list:
    #     return sum_nested_list(lst[0]) + sum_nested_list(lst[1:])
    if len(lst) == 0:
        return 0
    elif type(lst[0]) == int:
        return lst[0] + sum_nested_list(lst[1:])
    elif type(lst[0]) == list:
        return sum_nested_list(lst[0]) + sum_nested_list(lst[1:])



def corner_bar(m, n):
    '''Calculate the number of paths from
    my house at (m,n) to the bar (0,0)

    Parameters:
        m, n integers >= 0

    Return Value:
        the integer number of unique paths
    '''
    if m == 0 or n == 0:
        return 1
    else:
        return corner_bar(m-1, n) + corner_bar(m, n-1)

def license(grp1, grp2, length):
    '''Create license plates of style:

    XXX 111
    (with length characters on either side of the space)
    Generate all possibilities, taking characters left of
    the space from grp1, right of the space from grp2

    e.g.
    license('XY', '89', 2)
    ['XX 88', 'XX 89', 'XX 98', 'XX 99',
     'XY 88', 'XY 89', 'XY 98', 'XY 99',
     'YX 88', 'YX 89', 'YX 98', 'YX 99',
     'YY 88', 'YY 89', 'YY 98', 'YY 99']

    license('X', '5', 3)
    ['XXX 555']

    license('32', 'B', 2)
    ['33 BB', '32 BB', '23 BB', '22 BB']

    license('32', 'B', 1)
    ['3 B', '2 B']

    Return Value:
        list of strings
    '''
    if length == 0:
        return [' ']
    else:
        shorterplates = license(grp1, grp2, length-1)
        plates = []
        for s in shorterplates:
            for c1 in grp1:
                for c2 in grp2:
                    plates.append(c1 + s + c2)

        return plates


def main():
    #count(3)
    #count_up_to_100(120)
    #print(sum_n_to_1(5))
    #print(sum_list([6,0,-2,5]))
    #print(sum_nested_list([6, -2, [3, 1], [2, [3]]]))

    print(corner_bar(2,1))
    print(corner_bar(2,2))
    print(corner_bar(2,3))

    print(license('XY', '89', 3))

if __name__ == '__main__':
    main()
