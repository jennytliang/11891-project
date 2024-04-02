def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""
    # Add your code here
    return


# These are tests to check if your code is correct.
# After running your code, each of these tests will be
# run and reported on (i.e. printing True if the test
# passes or False if it fails).

def check(candidate):
    assert candidate([4, 2, 6, 7]) == 2
    assert candidate([1, 3, 5, 7]) == 0
    assert candidate([1, 2, 3, 4]) == 0
    assert candidate([1, 2, 3, 4, 5]) == 3
    assert candidate([1, 2, 3, 4, 5, 6]) == 3

if __name__ == "__main__":
    check(add)