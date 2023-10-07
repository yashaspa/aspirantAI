import sys

def file_sum(fname):
    '''Return the sum of the numbers in the
    given file

    Parameter:
        fname - a string containing a file's name

    Return Value:
        a float containing the sum of values
        in that file
    '''
    try:
        file = open(fname)
        nums = file.readlines()
        for i in range(len(nums)):
            nums[i] = float(nums[i])
        return sum(nums)
    except FileNotFoundError:
        print("Error: Could not find file " + fname)
        return 0

def main():
    #print(sys.argv)
    if len(sys.argv) < 2:
        print("Error: no filename given")
        print("Usage: python3 lec23.py filename.txt")
        return

    print(file_sum(sys.argv[1]))






if __name__ == '__main__':
    main()
