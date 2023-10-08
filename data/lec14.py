def add_one(numlist):
    '''Purpose: Return a new list with 1 added
    to each of the numbers in the original list

    Parameter:
        numlist - a list of numeric values

    Return Value:
        a new list
    '''
    # # create a copy of the list
    # copylist = numlist[:]
    # for i in range(len(copylist)):
    #     copylist[i] += 1
    # return copylist
    newlist = []
    for i in range(len(numlist)):
        newlist.append(numlist[i]+1)
    return newlist



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
    # for num in numlist:
    #     if num % 3 == 0:
    #         newlist.append(num)
    # return newlist
    copylist = numlist[:]
    for num in numlist: # numlist not copylist
        if num % 3 != 0:
            copylist.remove(num)
    return copylist



def nested_list_examples():
    scores1 = ['andy', 17, 14, 17, 11, 0, 20]
    scores2 = ['nate', 18, 19, 17, 11, 20, 20]
    scores3 = ['adrika', 20, 15, 0, 15, 18, 18]
    scores4 = ['eric', 19, 20, 15, 17, 16, 19]

    quiz_scores = [scores1, scores2, scores3, scores4]

    # just using the quiz_scores variable, get:
    # andy's quiz 3 score?

    # average of nate's quiz scores

    # average of all quiz 2 scores

def main():
    b = [11,7,6,9,13]
    result = only_div3(b)
    print(result)

if __name__ == '__main__':
    main()
