def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: 0
	Do not include these tokens in the code: ''
	"""

  
    # Write your code here.
    # s = 0
    # for i in range(len(lst)):
    #     if i%2 == 0:
    #         s += lst[i]
    # return s
    
    # return sum([lst[i] for i in range(len(lst)) if i%2==0])
    
    return sum([lst[i] for i in range(len(lst)) if i%2==0])



# TESTS
assert add([4, 2, 6, 7]) == 2
assert add([3, 6, 7, 4, 1, 2]) == 13
assert add([7, 2, 9, 8, 4, 1, 3, 5]) == 23
assert add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 20
assert add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 25
