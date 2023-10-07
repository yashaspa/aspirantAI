

def questionize(message):
    '''Convert given message into a question
    by adding a ? if it does not already end in one.

    Parameters:
        message - a str
    Return Value
        string that is now a question
    '''
    last_index = len(message) - 1
    # if message[last_index] == '?':
    #     return message
    # return message + '?'
    if message[last_index] != '?':
        message = message + '?'
    return message

def cookie_message(num):
    '''Build a message that tells someone how
    many cookies they have

    Parameters:
        num - a non-negative int

    Return Value:
        a string with the message
    '''
    if num == 1:
        message = "You have 1 cookie."
    elif num == 0:
        message = "You have no cookies."
    elif num < 0:
        message = "You owe me " + str(-num) + " cookies."
    else:
        message = "You have " + str(num) + " cookies."
    return message


def is_vowel(ch):
    '''Purpose:
        Test whether ch, a single character is a vowel
        a,e,i,o,u (or capital letter version)

    Paramter:
        ch - a string with a single character in it
    Return Value:
        True if ch is a vowel, False if not.
    '''
    # if (ch == 'a' or ch == 'e' or
    #     ch == 'i' or ch == 'o' or
    #     ch == 'u' or ch == 'A' or
    #     ch == 'E' or ch == 'I' or
    #     ch == 'O' or ch == 'U'):
    #     return True
    # return False
    return ch in 'aeiouAEIOU'


def contains_vowel(word):
    '''Purpose: Test whether the given word contains
    a vowel (a,e,i,o, or u) or not.

    Parameter:
        word - a string
    Return Value:
        True if the word has a vowel in it, False if not
    '''
    if ('a' in word or 'e' in word or
        'i' in word or 'o' in word or
        'u' in word):
        return True
    return False


def main():
    # m = questionize('what the heck!')
    # print(m)
    # m2 = questionize('why me?')
    # print(m2)
    # m3 = cookie_message(-6)
    # print(m3)

    # example of why == is bad with float
    # y = 27.2
    # x = 0.1
    # if y - x == 27.1:
    #     print('hooray')
    # else:
    #     print('nope, not equal')

    print(is_vowel('c'))
    print(is_vowel('i'))
    print(contains_vowel('andy'))
    print(contains_vowel('xxzzqq'))

if __name__ == '__main__':
    main()
