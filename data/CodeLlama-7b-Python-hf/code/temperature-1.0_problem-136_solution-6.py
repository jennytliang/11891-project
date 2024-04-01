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
    if len(lst) == 0:
        return (None, None)
    elif len(lst) == 1:
        if lst[0] > 0:
            return (None, lst[0])
        elif lst[0] < 0:
            return (lst[0], None)
        else:
            return (None, None)
    elif len(lst) == 2:
        if lst[0] > lst[1]:
            if lst[0] > 0:
                return (None, lst[1])
            elif lst[0] < 0:
                return (lst[0], None)
            else:
                return (None, None)
        elif lst[0] < lst[1]:
            if lst[1] > 0:
                return (None, lst[0])
            elif lst[1] < 0:
                return (lst[1], None)
            else:
                return (None, None)
        else:
            if lst[0] > 0:
                return (None, lst[0])
            elif lst[0] < 0:
                return (lst[0], None)
            else:
                return (None, None)
    elif len(lst) == 3:
        if lst[0] > lst[1]:
            if lst[0] > lst[2]:
                if lst[0] > 0:
                    return (None, lst[2])
                elif lst[0] < 0:
                    return (lst[0], None)
                else:
                    return (None, None)
            elif lst[0] < lst[2]:
                if lst[2] > 0:
                    return (None, lst[0])
                elif lst[2] < 0:
                    return (lst[2], None)
                else:
                    return (None, None)
            else:
                if lst[0] > 0:
                    return (None, lst[0])
                elif lst[0] < 0:
                    return (lst[0], None)
                else:
                    return (None, None)
        elif lst[0] < lst[1]:
            if lst[0] < lst[2]:
                if lst[2] > 0:
                    return (None, lst[0])
                elif lst[2] < 0:
                    return (lst[2], None)
                else:
                    return (None, None)
            elif lst[0] > lst[2]:
                if lst[0] > 0:
                    return (None, lst[2])
                elif lst[0] < 0:
                    return (lst[0], None)
                else:
                    return (None, None)
            else:
                if lst[0] > 0:
                    return (None, lst[0])
                elif lst[0] < 0:
                    return (lst[0], None)
                else:
                    return (None, None)
        else:
            if lst[1] > lst[2]:
                if lst[1] > 0:
                    return (None, lst[2])
                elif lst[1] < 0:
                    return (lst[1], None)
                else:
                    return (None, None)
            elif lst[1] < lst[2]:
                if lst[1] > 0:
                    return (None, lst[0])
                elif lst[1] < 0:
                    return (lst[2], None)
                else:
                    return (None, None)
            else:
                if lst[1] > 0:
                    return (None, lst[1])
                elif lst[1] < 0:
                    return (lst[1], None)
                else:
                    return (None, None)
    else:
        if lst[0] > lst[1]:
            if lst[0] > lst[2]:
                if lst[0] > lst[3]:
                    if lst[0] > 0:
                        return (None, lst[3])
                    elif lst[0] < 0:
                        return (