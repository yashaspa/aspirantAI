def contains_negative(mylist):
    '''Purpose: Test whether a given list contains
    a negative number or not

    Parameter:
        mylist - a list of numbers

    Return Value:
        True if mylist has any negative number,
        False otherwise
    '''
    # incorrect solution:
    # for val in mylist:
    #     if val < 0:
    #         return True
    #     else:
    #         return False
    # why?
    for val in mylist:
        if val < 0:
            return True
    return False

def convert_eo(intlist):
    '''Purpose: Return a string with Es and Os
    instead of the numbers, representing that the number
    in that location was even or odd.

    Parameter:
        intlist - a list of ints

    Return Value:
        a string that contains Es and Os
    '''
    rstr = ''
    for val in intlist:
        if val % 2 == 0:
            rstr = rstr + 'E'
        else:
            rstr = rstr + 'O'
    return rstr

def my_min(numlist):
    '''Purpose: My version of min() function

    Parameter:
        numlist - a list with numeric values

    Return Value:
        the smallest item from numlist
    '''
    lowest = numlist[0]
    for val in numlist:
        if val < lowest:
            lowest = val
    return lowest


def second_largest(numlist):
    '''Purpose: Return the second-largest item from
    a list containing at least 2 numbers
    '''

def remove_first_negative(numlist):
    '''Purpose: Remove first negative number from given list'''

def main():
    list1 = [8,6,3,2,13]
    list2 = [-6,-3,5,-5]
    list3 = [7,-1]
    print(contains_negative(list1))
    print(contains_negative(list2))
    print(contains_negative(list3))
    print(convert_eo(list1))

if __name__ == '__main__':
    main()
