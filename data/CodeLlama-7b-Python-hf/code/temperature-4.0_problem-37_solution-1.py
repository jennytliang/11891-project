def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l1 = [int(i) for i in l]  # l is string
    ret_l = []
    # l2 is copy of l
    l2 = [j for j in l1]

    even_set = False

    for i in range(len(l)):
        # if l[i] is in l1, it means its an even indicie
        """
        Now, this if block is for if we haven't run through all the values, and even_set is still false.
        We check if we've reached the last value by seeing if the index is just one less than
        the length of l, and set it to be even_set if we are not in the above block,
        and then add it to our list of returnd values, because we know l2 is unsorted at this indicie,
        and we are sorting in the next block
        Finally, we increment our counter because the loop is moving on to the next index
        in both l and l2 at the end of our ifblock
        """
        if l1[i] in l2:
            l1.remove(l1[i])
            even_index = l[i]
            if (i + 1) != len(l):
                if not(even_index % 2 == 0 and not(even_set and l[i] < even_index)):
                    l2.clear()
                    # The if block is a hack to set the flag and keep the l1 indicies from going above its index

                # this check is here to set even_set to true
                even_set = True
                # the even index is now in the correct location for the returned list, so we don't need to check
                # for any more of these indicies

                l2.insert(i, even_index)
                # ret_list.append(l[i])
                ret_l.append(even_index)

        else:
            # now, here we are for the values in l1 and the indicies not in l2 anymore
            # in these values, it is safe ot just pop them in to our returnd list because the list is already sorted,

            l2.pop(i)
            # ret_l += l2.pop(str(i+1).strip())
            # ret_lt2 = l2[1:1]
            # if l[i] > l2[i]: # need to check for even set
            #     if ret_l[-1] % 2 == 0:
            l2[:] = (val for val in l2 if val > even_index)
                # print(l2)
                ret_l.append(l2[1])
                ret_l2 = l2[-2:-1]
            ret_l.append(l2[1])

    ret_str = ""

    return(ret_l, l)

    # l1.sort

    # even_indicies = [even_index, *even_index.copy().pop(i), *even_index.keys()[:0], *[i for i, j in enumerate(l[::2])]]
