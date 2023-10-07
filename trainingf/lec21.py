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
    file = open(fname)
    nums = file.readlines()
    for i in range(len(nums)):
        nums[i] = float(nums[i])
    return sum(nums)


def count_eggs(fname):
    '''Count how many times the word 'eggs' appears
    in the file with the given name

    Parameter:
        fname - a string containing a file name

    Return Value:
        an int containing the number of times the
        word 'eggs' appears in the file
    '''
    file = open(fname, 'r')
    #nums = file.readline()
    text = file.read()
    return text.count('eggs')

def main():
    egg_total = count_eggs('greeneggs.txt')
    print(egg_total)

    # total = file_sum('numbers.txt')
    # print(total)
    #
    # fp = open('short.txt')
    # text = fp.read()
    # print("first call to read():\n" + text)

    # text2 = fp.read()
    # print("second call to read():\n" + text2)

    # print("1:" + fp.readline())
    # print("2:" + fp.readline())
    # print("3:" + fp.readline())
    # print("4:" + fp.readline())


if __name__ == '__main__':
    main()
