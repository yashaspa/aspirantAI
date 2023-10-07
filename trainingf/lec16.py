
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
    headers = ['Name', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6']
    #print('Name   Q1  Q2  Q3  Q4  Q5  Q6')
    scores.insert(0, headers)
    for row in range(len(scores)):
        for col in range(len(scores[row])):
            print(str(scores[row][col]) + ' ', end='')
        print()

def nested_list_examples():
    scores1 = ['Andy', 17, 14, 17, 11, 0, 20]
    scores2 = ['Nate', 18, 19, 17, 11, 20, 20]
    scores3 = ['Adrika', 20, 15, 0, 15, 18, 18]
    scores4 = ['Eric', 19, 18, 15, 17, 16, 19]
    quiz_scores = [scores1, scores2, scores3, scores4]
    print_scores(quiz_scores)

def main():
    nested_list_examples()

if __name__ == '__main__':
    main()
