def combine(d1, d2):
    '''Purpose: Combine two dictionaries into one.
    If there is a situation where d1 and d2
    have the same key, add their values together
    in output dictionary

    Parameters:
        d1, d2 - Two dictionaries containing
            numeric values

    Return Value:
        A dictionary that is the combination
        of d1 and d2. It should have all k-v pairs
        from both d1 and d2.
    '''
    # create copy of d1?
    out = {}
    # put all k-v pairs from d1 into out
    for key in d1:
        out[key] = d1[key]

    for key in d2:
        #out[key] = out.get(key, 0) + d2[key]
        if key in out:
            out[key] = out[key] + d2[key]
        else:
            out[key] = d2[key]

    return out

def main():
    counts1 = {'a': 9, 'b': 7, 'c': 9, 'e': 15}
    counts2 = {'b': 1, 'd': 11, 'a':2, 'C': 20}

    c3 = combine(counts1, counts2)

    keys = list(c3.keys())
    keys.sort()
    print(keys)
    for key in keys:
        print(key + ',' + str(c3[key]))
    # should be {'a': 4, 'b': 8, 'c': 9, 'd': 11}

    # instead, print in descending value order
    values = list(c3.values())
    values.sort()
    values.reverse()
    for val in values:
        print(val)

    items = list(c3.items())
    print(items)


if __name__ == '__main__':
    main()
