def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    # ADD YOUR CODE HERE
    return sum(lst[2 * i + 1] for i in range(len(lst) // 2))
