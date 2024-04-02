def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    
	Do not include these tokens in the code: mini = None #
	"""
    # Your code here
    mini = None
    for i in lst:
        if mini == None or i < mini:
            mini = i
    if lst.count(mini) == 1:
        return mini
    else:
        return None


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    output = next_smallest(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arr = [1, 2, 3, 4, 5]
solution = 2
test_case = [arr, solution]
test_function(test_case)

arr = [5, 1, 4, 3, 2]
solution = 2
test_case = [arr, solution]
test_function(test_case)

arr = [1, 1]
solution = None
test_case = [arr, solution]
test_function(test_case)

arr = []
solution = None
test_case = [arr, solution]
test_function(test_case)

arr = [5, 4, 3, 2, 1]
solution = 2
test_case = [arr, solution]
test_function(test_case)

arr = [1, 1, 2]
solution = None
test_case = [arr, solution]
test_function(test_case)

arr = [5, 4, 3, 2, 5]
solution = 3
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 3, 3, 3, 3, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 