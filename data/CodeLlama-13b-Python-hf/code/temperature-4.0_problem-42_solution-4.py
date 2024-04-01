def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """

    # return list with elements replaced with elements + 1 (using python syntax that will add to every element in array when added to list object)
    # [i for i in l] syntax is the general python syntax for creating a new list with the elements being whatever expression is between square brackets. 

    return [i + 1 for i in l]  # add 1 to each list element in l using the increment list function

def main():
    test_l_1 = [1, 2, 3]            # example test case: l with 3 elements, all of type int
    solution_3 = [2, 3, 4]          # example expected result for test above (after we run through the program, solution_2 is the current state of res.
    res = incr_list(list(test_l_1)) # run increment list function in problem_set_1 (this will store the result as the object res - the return value of invcr_list function)
    print(res, solution_3)          # this should print True since our program should return the same exact values as solution_7, if implemented correctly.
