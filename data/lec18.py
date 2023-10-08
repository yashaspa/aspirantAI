def first_clause(sentence):
    '''Given a sentence, return
    the first clause (i.e. everything
    before the first comma)

    Parameter:
        sentence - a string containing a sentence,
            which may or may not contain a comma

    Return Value:
        a string containing the first clause of
            the given sentence or entire thing if
            no comma
    '''
    comma_index = sentence.find(',')
    if comma_index < 0:
        return sentence
    else:
        return sentence[:comma_index]

def second_clause(sentence):
    '''Given a sentence, return
    the second clause (i.e. everything
    after the first comma and before the second comma)

    Parameter:
        sentence - a string containing a sentence,
            which may or may not contain a comma

    Return Value:
        a string containing the second clause of
            the given sentence, if it exists, '' if not
    '''
    comma_index1 = sentence.find(',')
    comma_index2 = sentence.find(',', comma_index1 + 1)
    if comma_index1 == -1:
        return ''
    elif comma_index2 == -1:
        'slice differently'
    print(comma_index1)
    print(comma_index2)
    return sentence[comma_index1 + 1 : comma_index2]

def last_word(sentence):
    '''
    '''

def main():
    sent1 = 'Is this the real life, is this just fantasy?'
    sent2 = ("Open your eyes, look up to the skies and see, " +
                "I'm just a poor boy, I need no sympathy")
    sent3 = 'No escape from reality'

    c1 = second_clause(sent1)
    print(c1)
    c2 = second_clause(sent2)
    print(c2)
    c3 = second_clause(sent3)
    print(c3)

if __name__ == '__main__':
    main()
