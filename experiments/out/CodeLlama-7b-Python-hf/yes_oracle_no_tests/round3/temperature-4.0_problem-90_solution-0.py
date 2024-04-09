def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    
	Include these tokens in the code: sorted _ list = sorted ( lst )
	"""


    if len(lst) <= 1:
       return None
    if len(lst) == 2:
        if lst[0] == lst[1]:
            return None
        else:
            return lst[1]
    lst = sorted(lst)
    if lst[1] == lst[0]:
        return None
    return lst[1]





def test_function(test_case):
    answer = next_smallest(test_case)
    if answer is not None:
        print(answer)
    else:
        print(answer)


test_case = [1, 2, 3, 4, 5]
test_function(test_case)

test_case = [5, 1, 4, 3, 2]
test_function(test_case)

test_case = []
test_function(test_case)

test_case = [1, 1]
test_function(test_case)

test_case = [5, 4, 3, 2, 1]
test_function(test_case)

test_case = [1, 1, 1]
test_function(test_case)

test_case = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6, 7]
test_function(test_case)