
def conditional_fun(x):
    # test if x not 0
    if x != 0:
        print('that is fun!')
        return True
    else:
        print('no fun.')
        return False

def is_vowel(ch):
    '''Purpose: Test whether a single
    character is a vowel or not.

    Parameter:
        ch - a string containing a single character
    Return Value:
        True if it is a vowel, False if not
    '''
    # if ch in 'aeiouAEIOU':
    # # if ('a' == ch or 'e' == ch or
    # #         'i' == ch or 'o' == ch or 'u' == ch):
    #     answer = True
    # else:
    #     answer = False
    # return answer
    return ch in 'aeiouAEIOU'

def contains_vowel(word):
    '''Purpose: Test whether the given word
    contains a vowel (a,e,i,o, or u) or not.

    Parameter:
        word - a string
    Return Value:
        True if the word has a vowel in it, False if not
    '''
    if ('a' in word or 'e' in word or
            'i' in word or 'o' in word or
            'u' in word or 'A' in word or
            'E' in word):
        return True
    else:
        return False

def main():
    conditional_fun(4)
    conditional_fun(7)
    conditional_fun(-1)
    # print(is_vowel('a'))
    # print(is_vowel('b'))
    # print(is_vowel('d'))
    print(contains_vowel('andy'))
    print(contains_vowel('xxxqqqtrs'))

if __name__ == '__main__':
    main()
