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
    if n == 101:
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
    '''
    if n == 1:
        return 1
    else:
        total = n + sum_n_to_1(n - 1)
        ###          ^^^^ 1+2+ ... + (n-1)
        return total

def main():
    #count_down(3)
    count_up_to_100(89)

if __name__ == '__main__':
    main()
