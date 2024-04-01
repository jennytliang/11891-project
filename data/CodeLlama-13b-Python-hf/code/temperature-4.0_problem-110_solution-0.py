def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """
    # 1. Bring lst1 into the state all even numbers and as many odd
    _l1 = lst1.copy() # lst1 is not expected to change. We keep lst1 as it is.

    for i in range(0, len(lst1)): # Iterate over list and remove odd number if any
        if lst1[i] & 1 != 0:  # If ith elem is not an even number
            _l1 = _l1[::-1]  # Reverse list so that even is on top
            print(f"_1st step-1: l1 is now -->{_l1}")
            break            # As we have moved last odd on top we do not need not to compare more with rest

    odd = []  # Create an empty placeholder list
    # iterate over reversed range as _l1 is now reversed. lst[0] elem is last element
    for rev_i in range(len(lst1)-1, -1, -1):
        # Check if its not even number
        if _l1[rev_i] & 1 != 0: # if the last odd
            # if its last elem it cannot be shifted to lst2 as list2 also might not have last elem as even.
            # So check if _l1 contains only one element  and if yes return "NO.
            if len(odd) == 0 and (rev_i != 0):
                odd.insert(0, True) # insert so that we reverse it later and pick it up as next iteration value

            for elem1, elem2 in zip(_l1[rev_i+1:], lst2):
                if (elem1 == elem2) | (elem2 & 1 != 0):
                    # if elem_1 is not an even no match and if elem_2 is an odd no shift is possible as there is no more elems in both list to compensate the shift by 1 (if shift at all).
                        # No way to compensate the shift. Shifting is not possible. Hence return "NO" # Check for elem_2 not to miss on odd_num in lst2 and shift
                    return "NO"

                # else if they match shift both lst1 and lst to get it to a state where only odd is on lst1 top and rest elem of both lists have just even numbers only
            odd_num = elem1   # get first odd number from lst1 to move
            break            # break to move on with other iter to check rest elems lst2
        else:
            if (rev_i != (len(lst1) - 1)):
                continue   # no odd number as we have checked it just above hence just continue

            # lst1 is just all even nums but check if there are odds present in lst2 or not and if not return NO
        for elem2_num in lst2[0:rev_i]: # lst2_num_to_match is lst2[0:2]. ie. it checks if odd_no in list of only even.
            if (elem2_num &1) != 0: # check for odds in lst2_num_to_match. ie. if even_num_not_match_lst2 has odd number
                return "NO"    # As we have confirmed there is no elem on both lst that can be used to make lst1 have all even and at the same time list2 has no even num so it will always have odd numbers hence cant make them to be even
        print(lst2[rev_i])
        # 2. Move all elements of odd to the lst1 so that list lst1 just has even numbers and rest of all odd elements of 2 are in list lst1.
    lst1.extend(lst2)     # Add lst2 that is all even numbers to lst1. so lst2 is replaced with lst1 elements that cannot be matched with lisb2
        #3. As no odd numbers are left it means lst1 and lsv2 are now equal which means only lst1 is having all even numbers
    print(f"Step-3:\n Odd No: {odd}, lst1 is  --> {_l1}, is all even now ? {all_even(lst1)} , lst1 + list2 ==> lst1 is equal to lst2 now {(_l1 + lst2) == _l1} ")
    if(not all_even(_l1)):
        raise Exception("Problem in list1 not all even even though all shifting is done successfully and still lst1 has odd\n {}".format(_l1 + odd))