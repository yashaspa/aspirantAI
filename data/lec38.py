def find_smallest_from_index(lst, startindex):
    '''Find the index of the smallest item,
    beginning with startindex
    '''
    smallest_index = startindex
    for j in range(startindex, len(lst)):
        if lst[j] < lst[smallest_index]:
            smallest_index = j
    return smallest_index

def selection_sort(lst):
    '''Use the Selection Sort algorithm to sort lst

    Parameter:
        lst - a list of comparable values

    Return Value:
        None
    '''
    # for each index, figure out what goes there,
    #   put it there. (swap with what is already there)
    for i in range(len(lst) - 1): # n-1 iterations
        # find what goes in index i
        smallest_index = find_smallest_from_index(lst, i)
        # swap with i
        lst[i], lst[smallest_index] = lst[smallest_index], lst[i]

def main():
    alist = [9,2,6,1,5,4]
    selection_sort(alist)
    print(alist)

if __name__ == '__main__':
    main()
