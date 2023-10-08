def count_upcase_words(text):
    '''Count the number of words that start
    with an uppercase letter

    Parameter:
        text - a string

    Return Value:
        an int of the number of words that start with
        an uppercase letter
    '''
    upcount = 0
    words = text.split()
    for word in words:
        if word[0].isupper():
            upcount += 1

    return upcount

def length_sans_punct(word):
    punct = ",.;:?!\'\"-_"
    count = 0
    for ch in word:
        if ch not in punct:
            count += 1
    return count

def censor(text):
    '''Censor text by replacing all 4-letter words
    with ****
    Use split and join (and other things)
    '''
    words = text.split()
    for i in range(len(words)):
        # if len(words[i]) == 4 and words[i].isalpha() == True:
        #     words[i] = '****'
        if length_sans_punct(words[i]) == 4:
            words[i] = '****' + words[i][4:]

    return ' '.join(words)

def main():

    sent1 = 'Is this the real life, is this just fantasy?'
    sent2 = ("Open your eyes, look up to the skies and see, " +
                "I'm just a poor boy, I need no SYMPATHY")
    sent3 = 'No escape from reality'

    c1 = censor(sent1)
    print(c1) #
    c2 = censor(sent2)
    print(c2) # 4
    c3 = censor(sent3)
    print(c3) # 1

if __name__ == '__main__':
    main()
