import lec24
import lec25

def char_count(message):
    '''Purpose: get the count of all characters
    in a given message

    Parameter:
        message - a string

    Return Value:
        a dictionary containing counts of each
        character that appears
    '''
    letter_count = {}
    for i in message:
        # solution #4
        # how about this solution?
        # slowwwwww  :(
        #letter_count[i] = message.count(i)

        # Solution 1
        if i in letter_count:
            letter_count[i] = letter_count[i] + 1
        else:
            letter_count[i] = 1
    return letter_count

def pretty_print_dictionary_by_value(d):
    '''Purpose: Print out the key-value pairs
    in the given dictionary, sorted by values in
    descending order

    Parameter:
        d - a dictionary with sortable values

    Return Value:
        None
    '''
    # build our own list of tuples with (v,k) pairs
    newlist = []
    for key in d:
        val = d[key]
        mytup = (val, key)
        newlist.append(mytup)
    print(newlist)

    newlist.sort()
    newlist.reverse()
    print(newlist)
    for tup in newlist:
        val = tup[0]
        key = tup[1]
        print(key, val)

    # attempt, but doesn't quite work
    # values = list(d.values())
    # values.sort()
    # values.reverse()
    # for val in values:
    #     #print(val)
    #     # oops! what now?
    #     # for key in d:
    #     #     if d[key] == val:
        #         print(key, val)

def letter_wordlist(text):
    '''Purpose: Create a dictionary of lists of
    all words that start with the same letter

    Parameter:
        text - a string

    Return Value:
        a dictionary containing letters as keys
        and lists of words as values
    '''
    out = {}
    wordlist = text.split()
    for w in wordlist:
        first_letter = w[0]
        if first_letter not in out:
            out[first_letter] = []
        out[first_letter].append(w)

    return out




def main():
    counts1 = {'a': 9, 'b': 7, 'c': 9, 'e': 15}
    counts2 = {'b': 1, 'd': 11, 'a':2, 'C': 20}

    c3 = lec25.combine(counts1, counts2)
    #print(c3)

    #pretty_print_dictionary_by_value(c3)

    #amessage = 'hello how many characters?'


    f = open('580-0.txt')
    amessage = f.read()
    result = letter_wordlist(amessage)
    print(result['Z'])
    print(result['Z'][1])
    print(result['Z'][1][-1])


if __name__ == '__main__':
    main()
