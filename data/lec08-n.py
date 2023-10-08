import sys

def file_sum(fname):
    '''Purpose: Sum all numbers in that are in
    file with given name

    Parameter:
        fname - a string containing a file name that
        contains one number per line

    Return Value:
        a float containing the sum of the numbers in the
        given file
    '''
    try:
        f = open(fname)
        sum = 0
        for i in f:
            sum += float(i)
        return sum
    except FileNotFoundError:
        print('Error occurred, cannot find file: ' + fname)
        return 0
    except IndexError:
        return 0

def count_eggs(fname):
    '''Count how many times the word 'eggs' appears
    in the file with the given name

    Parameter:
        fname - a string containing a file name

    Return Value:
        an int containing the number of times the
        word 'eggs' appears in the file
    '''
    fp = open(fname)
    return fp.read().count('eggs')

    # total = 0
    # for line in fp:
    #     eggcount = line.count('eggs')
    #     total += eggcount
    # return total

def count_marylamb(filename):
    '''Count the number of times "mary" appears
    in the given file plus the number of times "lamb"
    appears in the given file

    This function doesn't work as intended, why not?
    '''
    fp = open(filename)
    text = fp.read()
    mcount = text.count('mary')
    lcount = text.count('lamb')

    # mcount = fp.read().count('mary')
    # lcount = fp.read().count('lamb')
    return mcount + lcount

def add_amount(filename, amount):
    '''Load numbers from the given filename,
    add the given amount to each number, then
    write out to a file named added_filename

    Parameter:
        filename - a string containing the name of the
            file to read from, that has one number per line
        amount - a float containing the amount to add to

    Return Value:
        None
    '''
    fp_in = open(filename, 'r')
    fp_out = open("added_" + filename, 'w')

    lst = fp_in.readlines()
    print(lst)
    for line in lst:
        var = str(float(line) + amount)
        fp_out.write(var + '\n')


    fp_in.close()
    fp_out.close()


def punct_only(filename):
    '''
    '''

def main():
    #print(sys.argv)
    if len(sys.argv) <= 1:
        print('Error! You must enter a file name ', end = "")
        print('on the command line')
        return

    #fp = open('short.txt', 'r')
    #print(count_marylamb('mary.txt'))

    total = file_sum(sys.argv[1])
    print(total)
    #
    # egg_total = count_eggs('greeneggs.txt')
    # print(egg_total)
    #add_amount('numbers.txt', 8)

    # fp = open("/Users/andyexley/Courses/old/csci1133f21/lecture/lec22.py")
    # print(fp.read())

if __name__ == '__main__':
    main()
