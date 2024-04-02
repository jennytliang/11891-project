def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Do not include these tokens in the code: # add code here
	"""
    return sum([lst[i] for i in range(len(lst)) if i % 2 == 1 and lst[i] % 2 == 0])


# print(add([4, 2, 6, 7]))
# print(add([10, 2, 4, 6]))
# print(add([2, 4, 6, 8]))
# print(add([1, 3, 5, 7]))
