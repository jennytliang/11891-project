def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =  0 
	Do not include these tokens in the code: return sum ([ lst [ i ]
	"""

    r = 0
    for i in range(len(lst)):
        if i % 2 == 1:
            r += lst[i]
    return r


# tests
if __name__ == "__main__":
    assert add([4, 2, 6, 7]) == 2
    assert add([1, 1, 1, 1]) == 0
    assert add([0]) == 0
    assert add([5, 2, 1, 3, 6]) == 6
    assert add([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 20
