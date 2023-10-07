def while_sum(n):
    '''Purpose:
    Sum the numbers 1+2+...+n using a while loop

    Parameter:
        n - a positive int

    Return value:
        the sum
    '''
    i = 0
    sum = 0
    while i <= n:
        sum = sum + i
        i = i + 1
    return sum

def while_sum_evens(n):
    '''Purpose:
    Sum the even numbers 2+4+6+...+n
    using a while loop

    Parameter:
        n - a positive int

    Return Value:
        the sum
    '''
    i = 2
    sum = 0
    while i <= n:
        sum += i
        i = i + 2
    # while i <= n:
    #     if i % 2 == 0:
    #         sum += i
    #     i = i + 1
    return sum

def for_print(n):
    '''Purpose: print all multiples of 3 up to n
    use for loop and range statement
    '''
    for i in range(0,n,3):
        print(i)


def for_print2(m,n):
    '''Purpose: print all multiples of 5
    from m to n
    use for loop, range statement
    (and maybe a little math? o noes!)
    '''
    if m % 5 != 0:
        m = m - (m % 5) + 5

    # m is a multiple of 5
    for x in range(m, n, 5):
        print(x)

def is_vowel(c):
    return c in 'aeiouAEIOU'

def vowel_index(s):
    '''Purpose: Return the index in string s
    where the first vowel appears
    Use a loop (for or while)

    Parameter:
        s - a string

    Return Value:
        an index, or -1 if no vowel appears
    '''
    for i in range(len(s)):
        if is_vowel(s[i]):
            return i
    return -1

    # i = 0
    # for x in s:
    #     if is_vowel(x):
    #         return i
    #     i = i + 1
    # return -1



def sentinel_loop():
    '''Purpose: Ask user to type
    in numbers, calculate product of all
    numbers that they input
    '''
    prod = 1
    num = float(input('Enter a number (0 to stop):'))
    # write a loop that runs when user did not type 0
    while num != 0:
        prod = prod * num
        num = float(input('Enter a number (0 to stop):'))
    return prod

def loop_example1():
    '''Purpose: Write a while loop that prints
    "hello" 5 times
    '''
    i = 1
    while i <= 5:
        print('hello')
        i = i + 1
    print('goodbye')
def loop_example2():
    '''Purpose: Write a while loop that prints
    out increasing values from 1 to 10
    '''
    j = 1
    while j <= 10:
        print(j)
        j = j + 1
def loop_question1():
    '''How many lines of output are generated?'''
    i = 0
    while i < N:
        print('hi1')
        i += 1
    #  N lines of output
def loop_question2():
    '''How many lines of output are generated?'''
    i = N
    while i > 0:
        print('hi2')
        i -= 1
def loop_question3():
    '''How many lines of output are generated?'''
    i = N
    while i >= 0:
        print('hi3')
def loop_question4():
    '''How many lines of output are generated?'''
    i = 0
    while i > N:
        print('hi4')
        i += 1


def main():
    result = vowel_index('blah! blah!')
    print(result)
    result = vowel_index('qxnbmvnbzbc')
    print(result)

if __name__ == '__main__':
    main()
