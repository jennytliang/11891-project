def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: =
	"""

    # Your code here
    i = 0

    while i < len(lst):
        print(lst[i])
        i+=2


add([4, 2, 6, 7])
