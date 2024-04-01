def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    '''
    pos = None
    neg = None
    for i in lst:
        try:
            if int(i) < 0 and (neg is None or neg > int(i)):
                neg = int(i)
            if int(i) > 0 and (pos is None or pos < int(i)):
                pos = int(i)
        except:
            continue
    return neg, pos
    




print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
print(largest_smallest_integers([]))
print(largest_smallest_integers([0]))  