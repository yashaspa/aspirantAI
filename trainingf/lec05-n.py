def list_prod(alist):
    '''Purpose: multiply all the numbers in the given
    list

    Parameter:
        alist - a list containing numeric values

    Return Value:
        the product of the items in the given list
    '''
    sum = 1
    for val in alist:
        sum = sum * val
    return sum


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
    returnval = ''
    for val in intlist:
        if val % 2 == 0:
            returnval += 'E'
        else:
            returnval += 'O'
    return returnval

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


def add_one(numlist):
    for i in range(len(numlist)):
        numlist[i] += 1

def add_one_safe(numlist):
    newlist = numlist[:]
    for i in range(len(newlist)):
        newlist[i] += 1
    return newlist

def mult_all(numlist, scalar):
    '''
    '''

def second_smallest(numlist):
    '''Purpose: Return the second-smallest item from
    a list containing at least 2 numbers
    '''
    # newlist = numlist[:]
    # smallest = my_min(newlist)
    # newlist.remove(smallest)
    # return my_min(newlist)

    newlist = numlist[:]
    newlist.sort()
    return newlist[1]


def remove_first_negative(numlist):
    '''Purpose: Remove first negative number
    from given list
    Use either .remove or .pop

    Parameter:
        numlist - list of numeric values, with
            at least one negative

    Return Value:
        None
    '''
    for val in numlist:
        if val < 0:
            numlist.remove(val)
            return


def only_div3(numlist):
    '''Purpose: Return a new list that consists
    of only numbers from numlist that are
    divisible by 3.

    Parameter:
        numlist - a list of numeric values

    Return Value:
        the new list
    '''
    # newlist = []
    # for val in numlist:
    #     if val % 3 == 0:
    #         newlist.append(val)
    # return newlist

    # newlist = numlist[:]
    # for val in numlist:
    #     if val % 3 != 0:
    #         newlist.remove(val)
    # return newlist

    newlist = numlist[:]
    for i in range(len(newlist)):
        if newlist[i] % 3 != 0:
            newlist.pop(i)
    return newlist




def main():
    nscores1 = ['andy', 17, 14, 17, 11, 0, 20]
    nscores2 = ['nate', 18, 19, 17, 11, 20, 20]
    nscores3 = ['adrika', 20, 15, 0, 15, 18, 18]

    all_scores = [nscores1, nscores2, nscores3]

    # avg quiz 2 scores:
    all_scores[0][2] + all_scores[1][2] + all_scores[2][2]

    list1 = [8,1,6,3,2]
    list2 = [-6,-3,5,-5]
    list3 = [7,-1]
    result = only_div3(list1)
    print(result) # should be [6,3]
    print(list1)



if __name__ == '__main__':
    main()
