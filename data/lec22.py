def count_marylamb(filename):
    '''Count the number of times "mary" appears
    in the given file plus the number of times "lamb"
    appears in the given file

    This function doesn't work as intended, why not?
    '''
    fp = open(filename)
    # mcount = fp.read().count('mary')
    # lcount = fp.read().count('lamb')
    text = fp.read()
    mcount = text.count('mary')
    lcount = text.count('lamb')
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
    fpin = open(filename)
    fpout = open("added_" + filename, 'w')
    lines = fpin.readlines()
    print(lines)
    for i in range(len(lines)):
        lines[i] = float(lines[i])
        lines[i] += amount
        fpout.write(str(lines[i]) + '\n')
    #print(lines)
    fpin.close()
    fpout.close()


def main():
    print(count_marylamb('mary.txt'))
    add_amount('numbers.txt', 50)

if __name__ == '__main__':
    main()
