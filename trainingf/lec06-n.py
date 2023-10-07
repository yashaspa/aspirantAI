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
    # add 0, sort, then look at numbers next to 0
    copylist = alist[:]
    if 0 not in copylist:
        copylist.append(0)
    copylist.sort()
    zero = copylist.index(0)
    return copylist[zero-1], copylist[zero+1]

    # create list of negative numbers,
    # then list of positive numbers
    # negatives = []
    # positives = []
    # for val in alist:
    #     if val > 0:
    #         positives.append(val)
    #     elif val < 0:
    #         negatives.append(val)
    # negatives.sort()
    # positives.sort()
    # return negatives[-1], positives[0]

def is_sorted(vals, ascending=True):
    '''Test whether list of vals is sorted

    Parameters:
        vals - a list of numeric values

    Return Value:
        True, if sorted, False if not
    '''
    for i in range(1, len(vals)):
        if ascending == True:
            if vals[i-1] > vals[i]:
                return False
        else:
            if vals[i] > vals[i-1]:
                return False

    return True


def print_scores(scores):
    '''Write a function that will print out
    scores in a nice table:

        Name   Q1  Q2  Q3  Q4  Q5  Q6
        Andy   17  14  17  11   0  20
        Nate   18  19  17  11  20  20
        ...

    Parameter
        scores - a list of list with quiz scores

    Return Value
        None
    '''

    for row in range(len(scores)):

        for col in range(len(scores[row])):
            print(scores[row][col], end=' ')
        print()

def nested_list_examples():
    scores1 = ['Andy', 17, 14, 17, 11, 0, 20]
    scores2 = ['Nate', 18, 19, 17, 11, 20, 20]
    scores3 = ['Adrika', 20, 15, 0, 15, 18, 18]
    scores4 = ['Eric', 19, 18, 15, 17, 16, 19]

    quiz_scores = [scores1, scores2, scores3, scores4]

    # just using the quiz_scores variable, get:
    # Adrika's quiz 4 score?
    #print(quiz_scores[2][4])

    # Average of Nate's quiz scores
    # total = 0
    # number = 0
    # for i in range(1, len(quiz_scores[1])):
    #     total += quiz_scores[1][i]
    #     number += 1
    # print(total/number)

    # total = 0
    # for val in quiz_scores[1][1:]:
    #     total += val
    # print(total/len(quiz_scores[1][1:]))
    #
    # print(sum(quiz_scores[1][1:]) / len(quiz_scores[1][1:]))
    #
    # # Average of all quiz 2 scores
    # total = 0
    # for scores in quiz_scores:
    #     total += scores[2]
    # print(total / len(quiz_scores))

    # Find everyone who scored a 20
    # name_list = []
    # for i in range(len(quiz_scores)):
    #     for j in range(len(quiz_scores[i])):
    #         if quiz_scores[i][j] == 20:
    #             if quiz_scores[i][0] not in name_list:
    #                 name_list.append(quiz_scores[i][0])
    # print(name_list)
    name_list = []
    for i in range(len(quiz_scores)):
        if 20 in quiz_scores[i]:
            name_list.append(quiz_scores[i][0])
    print(name_list)


    # count total number of scores of 20
    # for everyone

    # print out as a chart!
    print_scores(quiz_scores)

def main():
    a = [1,1,4,6,7]
    print(is_sorted(a)) # true
    print(is_sorted(a, ascending=True)) #true
    b = [9,8,8,7]
    print(is_sorted(b, ascending=False)) #true




if __name__ == '__main__':
    main()
