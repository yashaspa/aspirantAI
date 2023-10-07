def alpha_char_count(message):
    '''Purpose: get the count of all
    alphabetical characters in a given message

    Parameter:
        message - a string

    Return Value:
        a dictionary containing counts of each
        character that appears
    '''
    letter_count = {}
    for i in message:
        #solution 1 (a bit slow)
        # if i not in letter_count and i.isalpha():
        #     letter_count[i] = message.count(i)

        # solution 2 (a little slower! oops!)
        # if i.isalpha():
        #     if i in letter_count:
        #         letter_count[i] = letter_count[i] + 1
        #     else:
        #         letter_count[i] = 1

        # solution 3 (a little slower! oops!)
        if i.isalpha():
            letter_count[i] = letter_count.get(i, 0) + 1

    return letter_count

def alpha_char_wordlist(message):
    '''Purpose: Create a dictionary of lists of
    all words that start with the same letter

    Parameter:
        message - a string

    Return Value:
        a dictionary containing letters as keys
        and lists of words as values
    '''
    letter_words = {}
    wordlist = message.split()
    for word in wordlist:
        if word[0] in letter_words:
            lst = letter_words[word[0]]
            lst.append(word)
        else:
            letter_words[word[0]] = [word]

    return letter_words

def combine(d1, d2):
    '''Purpose: Combine two dictionaries into one.
    If there is a situation where d1 and d2
    have the same key, add their values together
    in output dictionary

    Parameters:
        d1, d2 - Two dictionaries containing
            numeric values

    Return Value:
        A dictionary that is the combination
        of d1 and d2. It should have all k-v pairs
        from both d1 and d2.
    '''
    out = {}
    for key in d1:
        if key in d2:
            out[key] = d1[key] + d2[key]
        else:
            out[key] = d1[key]

    for key in d2:
        if key not in out:
            out[key] = d2[key]

    return out

def pretty_print_dictionary(d):
    '''Purpose: Print out the key-value pairs
    in the given dictionary, one per line,
    sorted by keys in ascending order

    Parameter:
        d - a dictionary with sortable keys

    Return Value:
        None
    '''
    keylist = list(d.keys())
    #print(keylist)
    keylist.sort()
    #print(keylist)
    for i in keylist:
        print(i, d[i])

def pretty_print_dictionary_by_value(d):
    '''Purpose: Print out the key-value pairs
    in the given dictionary, sorted by values in
    descending order

    Parameter:
        d - a dictionary with sortable values

    Return Value:
        None
    '''
    itemlist = list(d.items())
    #print(itemlist)

    # build something that looks like itemlist,
    # but with keys and values swapped
    newlist = []
    for key in d:
        # create a tuple
        tup = (d[key], key)
        newlist.append(tup)

    #print(newlist)
    newlist.sort()
    newlist.reverse()
    #print(newlist)

    for tup in newlist:
        print(tup[1], tup[0])


    # valuelist = list(d.values())
    # valuelist.sort()
    # valuelist.reverse()
    # print(valuelist)
    # #for val in valuelist:
        # another for loop, look for value
        # good plan
        # for key in d:
        #     if d[key] == val:
        #         print(key, val)






def main():
    f = open('580-0.txt')
    amessage = f.read()
    #amessage = 'how many characters do we have?'
    result = alpha_char_count(amessage)
    print(result)
    pretty_print_dictionary_by_value(result)
    # counts1 = {'a': 9, 'b': 7, 'c': 9, 'e': 15}
    # counts2 = {'b': 1, 'd': 11, 'a':2, 'C': 20}
    #
    # c3 = combine(counts1, counts2)
    # print(c3)


if __name__ == '__main__':
    main()
