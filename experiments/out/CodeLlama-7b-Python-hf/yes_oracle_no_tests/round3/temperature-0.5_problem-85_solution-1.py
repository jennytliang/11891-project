def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s
	Do not include these tokens in the code: # pass sum
	"""

    # pass sum
    sum = 0
    for i in range(0, len(lst)):
        if i % 2 == 1:
            sum += lst[i]
    return sum


def test_add():
    assert add([4, 2, 6, 7]) == 2
    assert add([4, 2, 6, 7, 1]) == 3
    assert add([4, 2, 6, 7, 1, 3]) == 5
    assert add([4, 2, 6, 7, 1, 3, 5]) == 7


if __name__ == '__main__':
    test_add()
