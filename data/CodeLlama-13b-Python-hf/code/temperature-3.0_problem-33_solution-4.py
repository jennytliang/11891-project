def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    i = 0
    while i < len(l):
        if i % 3 != 0:
            i = i + 1
        else:
            new_list = []
            j = i
            while j % 3 == 0:
                new_list.append(l[j])
                j += 1
            sorted_new_list = sort(new_list)
            k = 0
            m = i
            while m % 3 == 0:
                l[m] = sorted_new_list[k]
                k += 1
                m += 1
            i += 1
    return l


if __name__ == "__main__":
    import doctest
    
