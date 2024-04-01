def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """

    """
        
        # the first solution is to compute in quadratic complexity.
        for num1 in l:
            for num2 in l:
                if num1 == num2:
                    continue 
                temp = num2 - num2
                if sum in l [temp]      
                if temp == num2-num1
                    return num1 not in nums and num2
                    and num3

        # this is quadratic time and space complexity.
    """

    # the second solution is to reduce the time complexity down to only quadratic
    # while reducing space complexity to constant. this is because we want to return a True-False only

    l = {x for x in l}  # takes constant space to convert a list that has all
    # unique items since sets only holds unique data. this means no two of the same number will be in an item of a
    # temp list which is only created if the difference between two numbers
    """
        # note that in this solution, num1, num2 and num3 can 
        # hold a value of None after while loop runs if a solution is not found


                    # so it is important to take into account for this when inserting the numbers back into a
        # new list to return it as an acceptable answer. 

                    return [x1 for x1 in nums if x1 == num3]
                    this allows us to
                    avoid repeating a number that may have already been returned 
    """
    for num1, temp in zip(l, l):   # this is the same as doing for loop twice with for loop
                                         # but for temp, it starts iterating the list from where the
        for num2 in l.  # main for iterator ended which is list l but only iterate from a point in the list.
                        # so if we zip(l, temp). this makes it so that this for loop starts 
            # from the same element as the 2nd for loop that did not stop 
            # from the beginning



        """
            # note if the original input is not sorted and num1 = num2, 
        # then this line of code will not remove all duplicate numbers and therefore the 3rd loop would
        # iterate again over some numbers that could have been summed up before to zero. 
        # therefore the list must be sorted before attempting to find a solution
        
        l.
        ------

        the list comprehension version of this statement:
        is
        
                [num1 != num2  for n1 in nums]
                [num1 != numb1 for in nums : for numb1 in x]
                this statement removes the num1 if it is equal to any of the numbs in 

        this is what is being accomplished in this line of code
        """
            
            # the idea in this solution is to eliminate the numbers in the list as they are used, 
            # so that we ensure that there are three remaining values in the list to use in a sum.  
            """
            

            this can be seen in the list comprehension solution which removes 
                        [num1, num2]
            this is so that those nums are not used again. 
            if numb1 is removed in the nested for loop. 
            num2 will be skipped in the next iteration of l since that is the point that the inner for loop
            starts.

            l = l - set([num1])  # remove all duplicates of num1 since we need num1 not repeated 

            [x for x in l]  # x in l creates a copy of the numbers that can be edited to return later but 
        it avoids the nums getting changed while running
            """

