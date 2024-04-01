def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    if len(lst) < 2:
        return None
    lst.sort()
    return lst[1]


def test_function(test_case):
    output = next_smallest(test_case[0])
    solution = test_case[1]
    if output == solution:
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], 2])
test_function([[5, 1, 4, 3, 2], 2])
test_function([[], None])
test_function([[1, 1], None])