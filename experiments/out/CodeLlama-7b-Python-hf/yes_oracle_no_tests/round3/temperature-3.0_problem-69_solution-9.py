def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    
	Include these tokens in the code: count = dict ()
	Do not include these tokens in the code: # Your code here
	'''
    count = {}
    for item in lst:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    for item in lst:
        if (item > 0) and (count[item] >= item):
            return item
    return -1


def test_function(test_case):
    lst = test_case[0]
    solution = test_case[1]
    output = search(lst)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


lst = [4, 1, 2, 2, 3, 1]
solution = 2
test_case = [lst, solution]
test_function(test_case)

lst = [1, 2, 2, 3, 3, 3, 4, 4, 4]
solution = 3
test_case = [lst, solution]
test_function(test_case)

lst = [5, 5, 4, 4, 4]
solution = -1
test_case = [lst, solution]
test_function(test_case)

lst = [10, 9, 9, 9, 1]
solution = 10
test_case = [lst, solution]
test_function(test_case)

lst = [10, 9, 9, 9, 1, 2, 2, 2, 1]
solution = 2
test_case = [lst, solution]
test_function(test_case)

lst = [10, 9, 9, 9, 1, 2, 2, 2, 1, 10]
solution = 10
test_case = [lst, solution]
test_function(test_case)

lst = [10, 9, 9, 9, 1, 2, 2, 2, 1, 10, 2, 2, 2, 1, 1