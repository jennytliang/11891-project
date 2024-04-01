def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # return  l[len(l) - max_index(l, 1)]
    return max(l) if l else -float('inf')


def is_sorted(l:  list):
    """Returns whether the list l is sorted. If yes returns True,
    in other case returns False.

    l -- list
    Rather than simply return True when given the empty list [], this function should return
    False, since even though the list would currently pass if given as an answer to maxEl, it
    it still not sorted and would fail the actual maxEl test case if used later.
    >>> is_sorted([1, 2,2])
    True
    >>> is_sorted([1, 2, 3, 4, 5])
    True
    >>> is_sorted([1,2, 4 ,3])
    False
    """
    l_2 = [-float('inf')] + l + [float('inf')]
    return all([l_1  <= l_2 <= l_3
                            for l_1, l_2, l_3
                            in
                zip
                  (
                    l_2, l_2[1:],
                     l_2[2:]

                  )
                ]
               )

