def loop_example1():
    '''Purpose: Write a while loop that prints
    "hello" 5 times
    '''
    i = 0
    while i < 10:
        print('hello')
        i = i + 2
    print('goodbye')

def loop_example2():
    '''Purpose: Write a while loop that prints
    out increasing values from 1 to 10
    '''
    j = 1
    while j <= 10:
        print(j)
        j = j + 1
    print('done')

def loop_question1():
    '''How many lines of output are generated?'''
    i = 0
    while i < N:
        print('hi1')
        i += 1
    # Answer: N times

def loop_question2():
    '''How many lines of output are generated?'''
    i = N
    while i > 0:
        print('hi2')
        i -= 1
    # N

def loop_question3():
    '''How many lines of output are generated?'''
    i = N
    while i >= 0:
        print('hi3')

    # infinite loop :(


def loop_question4():
    '''How many lines of output are generated?'''
    i = 0
    while i > N:
        print('hi4')
        i += 1
    # Ansser: 0 if N is a non-negative number

def loop_example3(n):
    '''Write a while loop that sums numbers 1 - n,
    inclusive, returns result
    1+2+3+4+...+(n-1) + n

    Parameter:
        n - a positive int
    '''
    sum = 0
    i = 0
    while i <= n:
        sum = sum + i
        i = i + 1
    return sum

def main():
    r = loop_example3(50)
    print(r)

if __name__ == '__main__':
    main()
