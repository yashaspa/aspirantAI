def sum_odds_m_to_n(m, n):
    '''Find sum of odd numbers m to n (inclusive)
    using a for loop. assume m is a positive odd int

    Parameters:
        m - a positive odd int
        n - a positive int greater than m

    Return Value:
        the sum of those odd numbers
    '''
    total = 0
    for i in range(m, n+1, 2):
        total = total + i
    return total

def for_print(m, n):
    '''Purpose: print all multiples of 5
    from m to n inclusive
    use for loop, range statement
    (and maybe a little math? o noes!)
    '''
    #total = 0
    for i in range(m, n+1):
        if i % 5 == 0:
            print(i)
        #total = total + i

def is_vowel(ch):
    '''Purpose: Return True if the given character
    is a vowel, False if not

    Parameter:
        ch - a string containing a single character

    Return Value:
        True or False, depending on if ch is a vowel
    '''
    return ch in 'aeiouAEIOU'

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
        if is_vowel(s[i]) == True:
            return i
    return -1

    # index_num = 0
    # for x in s:
    #     if is_vowel(x) == True:
    #         return index_num
    #     index_num += 1
    #
    # return -1



def main():
    # result = sum_odds_m_to_n(3, 10)
    # print(result) # should be 3+5+7+9 = 24
    # result = sum_odds_m_to_n(7, 11)
    # print(result) # 7 + 9 + 11 = 27
    # for_print(3, 11) # 5, 10
    # for_print(30, 57) # 30, 35, 40, 45, 50, 55
    s = 'spam'
    s2 = 'zxcvbnmz'
    print(vowel_index(s))
    print(vowel_index(s2))



if __name__ == '__main__':
    main()
