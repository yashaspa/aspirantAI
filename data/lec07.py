
def questionize(message):
    '''Convert given message into a question
    by adding a ? if it does not already end in one.
    If it does already end with a ?, just return
    the original string

    Parameters:
        message - a str
    Return Value:
        string that is now a question
    '''
    # how to find last letter of a string?
    last_index = len(message) - 1
    # if message[last_index] == "?":
    #     message = message
    # else:
    #     message = message + "?"
    if message[last_index] != "?":
        message = message + "?"
    return message



def contains_vowel(word):
    '''Purpose: Test whether the given word contains
    a vowel (a,e,i,o, or u) or not.

    Parameter:
        word - a string
    Return Value:
        True if the word has a vowel in it, False if not
    '''


def main():
    out = questionize('hello')
    print(out)
    out2 = questionize('what?')
    print(out2)





if __name__ == '__main__':
    main()
