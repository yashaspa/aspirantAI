def sum_list(lst):
    '''Purpose: Recursively add up all numbers in a list
    i.e. sum_list([6,-2,0,1]) -> 5

    Parameter:
        lst - a list containing numeric values

    Return Value:
        the sum
    '''
    if len(lst) == 0:
        return 0
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
    if len(lst) == 0:
        total = 0
    elif type(lst[0]) == int:
        total = lst[0] + sum_nested_list(lst[1:])
    elif type(lst[0]) == list:
        total = sum_nested_list(lst[0]) + sum_nested_list(lst[1:])
    return total

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

def scramble(r_letters, s_letters):
    """
    Output every possible combination of a word.
    Each recursive call moves a letter from
    r_letters (remaining letters) to
    s_letters (scrambled letters)
    """
    if len(r_letters) == 0:
        # Base case: All letters used
        print(s_letters)
    else:
        # Recursive case: For each call to scramble()
        # move a letter from remaining to scrambled
        for i in range(len(r_letters)):
            # The letter at index i will be scrambled
            scramble_letter = r_letters[i]

            # Remove letter to scramble from remaining letters list
            remaining_letters = r_letters[:i] + r_letters[i+1:]

            # Scramble letter
            scramble(remaining_letters, s_letters + scramble_letter)

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


def main():
    #print(sum_nested_list([6, -2, [3, 1], [2, [3]]]))
    print(corner_bar(100,100))

if __name__ == '__main__':
    main()
