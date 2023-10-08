def sum_evens_to_n(n):
    '''Find sum 2+4+...+n using a for loop
    '''
    sum = 0
    for i in range(n):
        if i % 2 == 0:
            sum = sum + i

    return sum


def sum_odds_m_to_n(m, n):
    '''Find sum of odd numbers m to n (inclusive)
    using a for loop
    '''

def main():
    sum_evens_to_n(5) # should be 6
    sum_evens_to_n(6) # should be 12


if __name__ == '__main__':
    main()
