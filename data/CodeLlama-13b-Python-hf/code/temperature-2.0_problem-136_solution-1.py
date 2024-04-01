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
    if not lst:
        return (None, None)

    max_neg = float('-inf')
    min_pos = float('inf')

    for el in lst:
        if el < 0 and el > max_neg:
            max_neg = el
        if el > 0 and el < min_pos:
            min_pos = el

    return (max_neg, min_pos)


if __name__ == '__main__':
    print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
    print(largest_smallest_integers([]))
    print(largest_smallest_integers([0]))
