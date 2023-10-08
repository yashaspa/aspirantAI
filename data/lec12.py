def list_stuff():
    '''Purpose: example of creating a list
    and using it
    '''
    items = [19, 7, 88, -23]

    print(items[2])
    print(items[1:3])

def list_prod(alist):
    '''Purpose: multiply all the numbers in the given
    list

    Parameter:
        alist - a list containing numeric values

    Return Value:
        the product of the items in the given list
    '''
    product = 1
    for x in range(len(alist)):
        product *= alist[x]
    # for x in alist:
    #     product *= x
    return product

def main():
    stuff = [3,2,7]
    print(list_prod(stuff))



if __name__ == '__main__':
    main()
