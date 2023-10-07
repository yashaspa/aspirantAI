def first_clause(sentence):
    '''Given a sentence, return
    the first clause (i.e. everything
    before the first comma)
    using the find() method

    Parameter:
        sentence - a string containing a sentence,
            which may or may not contain a comma

    Return Value:
        a string containing the first clause of
            the given sentence or entire thing if
            no comma
    '''
    if ',' in sentence:
        return sentence[0 : sentence.find(',')]
    else:
        return sentence

def second_clause(sentence):
    '''Given a sentence, return
    the second clause (i.e. everything
    after the first comma and before the second comma)
    using the find() method

    Parameter:
        sentence - a string containing a sentence,
            which may or may not contain a comma

    Return Value:
        a string containing the second clause of
            the given sentence, if it exists, '' if not
    '''
    first_comma = sentence.find(',')
    second_comma = sentence.find(',', first_comma+1)
    # print(first_comma)
    # print(second_comma)
    if sentence.count(',') >= 2:
        return sentence[first_comma+1:second_comma]
    elif sentence.count(',') == 1:
        return sentence[first_comma+1:]
    else:
        return ''

def last_word(sentence):
    '''Given a sentence, return the last word
    in that sentence using rfind()
    '''
    last_space = sentence.rfind(' ')
    return sentence[last_space+1:]

def print_table(scores):
    '''Print Table again!
    Use string formatting tools to print this table
    nicely (finally)
    '''
    print("Name      Q1  Q2  Q3  Q4  Q5  Q6")
    for row in range(len(scores)):
        for col in range(len(scores[row])):
            if col == 0:
                print(f"{scores[row][col]:<8}", end='')
            else:
                print(f"{scores[row][col]:>4}", end='')
        print()

def remove_vowels(message):
    '''Use the .replace method to remove all vowels
    from a given string

    Parameter:
        message - str to remove vowels from

    Return Value:
        a new string with no vowels
    '''
    for vowel in 'aeiouAEIOU':
        message = message.replace(vowel, '_')
    return message

def count_upcase_words(text):
    '''Count the number of words that start
    with an uppercase letter

    Parameter:
        text - a string

    Return Value:
        an int of the number of words that start with
        an uppercase letter
    '''
    count = 0
    wordlist = text.split()
    for word in wordlist:
        if word[0].isupper():
            count += 1
    return count


def censor(text):
    '''Censor text by replacing all 4-letter words
    with ****
    Use split and join (and other things)
    '''
    #text = text.replace(',', ' ')
    wordlist = text.split()
    # iterate over word list
    #   for each word that is 4 letters, replace with
    #               ****
    # join when done
    for word in wordlist:
        if len(word) == 4 and word.isalpha():
            wordlist[wordlist.index(word)] = '****'
        elif not word[-1].isalpha() and len(word) == 5:
            wordlist[wordlist.index(word)] = '****' + word[-1]

    newtext = ' '.join(wordlist)
    return newtext

def main():
    # scores1 = ['Andy', 17, 14, 17, 11, 0, 20]
    # scores2 = ['Nate', 18, 19, 17, 11, 20, 20]
    # scores3 = ['Adrika', 20, 15, 'ex', 15, 18, 18]
    # scores4 = ['Eric', 19, 18, 15, 17, 16, 19]
    #
    # quiz_scores = [scores1, scores2, scores3, scores4]
    # print_table(quiz_scores)

    sent1 = 'Is this the real life, is this just fantasy?'
    sent2 = ("Open your eyes, look up to the skies and see, " +
                "I'm just a poor boy, I need no sympathy")
    sent3 = 'No escape from reality'

    c1 = censor(sent1)
    print(c1)
    c2 = censor(sent2)
    print(c2)
    c3 = censor(sent3)
    print(c3)

if __name__ == '__main__':
    main()
