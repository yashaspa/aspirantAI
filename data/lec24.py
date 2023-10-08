def char_count(message):
    '''Purpose: get the count of all characters
    in a given message

    Parameter:
        message - a string

    Return Value:
        a dictionary containing counts of each
        character that appears
    '''
    counters = {}
    for ch in message:
        # Solution 3
        counters[ch] = counters.get(ch, 0) + 1

        # Solution 2
        # if ch not in counters:
        #     counters[ch] = 0
        # counters[ch] += 1

        # Solution 1
        # if ch in counters:
        #     counters[ch] = counters[ch] + 1
        # else:
        #     counters[ch] = 1
    return counters

def main():
    # scores = {}
    #
    # scores['Andy'] = 91

    amessage = 'How many characters do we have?'
    result = char_count(amessage)
    print(result)

if __name__ == '__main__':
    main()
