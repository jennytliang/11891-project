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
    lst.sort()
    largest_neg = None
    smallest_pos = None
    i = 0
    j = len(lst)

    while i < j:
        if len(lst) == 0:
            break
        elif i == 0:
            if lst[i] < 0:
                largest_neg = lst[i]
                i += 1
            elif lst[i] > 0:
                smallest_pos = lst[i]
                i += 1
        elif i == len(lst) - 1:
            if lst[i] < 0:
                largest_neg = lst[i]
                i -= 1
            elif lst[i] > 0:
                smallest_pos = lst[i]
                i -= 1
        else:
            if lst[i] < 0:
                largest_neg = lst[i]
                i -= 1
            elif lst[i] > 0:
                smallest_pos = lst[i]
                i += 1

    return largest_neg, smallest_pos


    # Solution I tried before realizing above solution
    # def largest_smallest_integers(lst):
    #     largest_negative = smallest_positive = None
    #     for num in lst:
    #         if largest_negative is None:
    #             if num < 0:
    #                 largest_negative = num
    #             elif num > 0:
    #                 smallest_positive = num
    #         elif num < 0:
    #             if largest_negative < num:
    #                 largest_negative = num
    #         elif num > 0:
    #             if smallest_positive > num:
