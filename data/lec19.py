def last_word(sentence):
    '''Use one of the .find() methods and
    slicing to get the last word of the given sentence

    Parameter:
        sentence - a string containing multiple words

    Return Value:
        a string containing the last word of the given sentence
    '''
    sentence = sentence.strip()
    last_space = sentence.rfind(' ')
    return sentence[last_space + 1:]


def print_table(scores):
    '''Print Table again!
    Use string formatting tools to print this table
    nicely (finally)
    '''
    print("Name      Q1  Q2  Q3  Q4  Q5  Q6")
    for row in range(len(scores)):
        for col in range(len(scores[row])):
            if col == 0:
                print(f'{scores[row][col]:<8}', end='')
            else:
                print(f'{scores[row][col]:>4}', end='')
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
        message = message.replace(vowel, '')
    return message


def main():
    #print(last_word("The rain in spain ")) #should be "spain"



    #q_scores = [['Andy', 17, 14, 17, 11, 0, 20],
                # ['Nate', 18, 19, 17, 11, 20, 20],
                # ['Adrika', 20, 15, 'ex', 15, 18, 18],
                # ['Eric', 19, 18, 15, 17, 16, 19]]

    #print_table(q_scores)

    sent = 'Andy really likes code examples'
    print(remove_vowels(sent))

if __name__ == '__main__':
    main()
