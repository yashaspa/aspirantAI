
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
            print(scores[row][col], end='')
            # :(

def nested_list_examples():
    scores1 = ['Andy', 17, 14, 17, 11, 0, 20]
    scores2 = ['Nate', 18, 19, 17, 11, 20, 20]
    scores3 = ['Adrika', 20, 15, 0, 15, 18, 18]
    scores4 = ['Eric', 19, 18, 15, 17, 16, 19]

    quiz_scores = [scores1, scores2, scores3, scores4]

    # just using the quiz_scores variable, get:
    # Adrika's quiz 4 score?
    print(quiz_scores[2][4])

    # Average of Nate's quiz scores
    total = 0
    for i in range(1, len(quiz_scores[1])):
        total += quiz_scores[1][i]
    print(total / (len(quiz_scores[1]) - 1))

    copy = quiz_scores[1][1:]
    print(sum(copy) / len(copy))

    # Average of all quiz 2 scores
    two_total = 0
    for i in range(len(quiz_scores)):
        two_total += quiz_scores[i][2]
    print(two_total / len(quiz_scores))

    # Find everyone who scored a 20
    name_list = []
    for lst in quiz_scores:
        if 20 in lst:
            name_list.append(lst[0])
    print(name_list)

    # count total number of scores of 20
    # for everyone
    count_20 = 0
    for row in range(len(quiz_scores)):
        for col in range(1, len(quiz_scores[row])):
            if quiz_scores[row][col] == 20:
                count_20 += 1
    print(count_20)

    print_scores(quiz_scores)


def main():

    nested_list_examples()


if __name__ == '__main__':
    main()
