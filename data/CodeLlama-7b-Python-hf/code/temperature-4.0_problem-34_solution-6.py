def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """

    # sort l in place using a built-in sorted function, this mutates l
    l.sort()

    i=0
    # while loop to check whether the last item is duplicated to the previous one of the array
    while(i < len(l)):
        # check whether is the first appearance of an item or an appearance after the previous duplicate
        if (l[i] != l[i - 1]):
            continue
        l.pop()
        continue
        i += 1
        