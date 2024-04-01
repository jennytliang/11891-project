def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s
	Do not include these tokens in the code: r
	"""
    return sum([lst[i] for i in range(len(lst)) if i % 2 == 0 and lst[i] % 2 == 0])


def test_cases():
    assert add([4, 2, 6, 7]) == 2
    assert add([4, 0, 6, 7]) == 6
    assert add([4, 2, 6, 0]) == 4
    assert add([4, 0, 6, 0]) == 10
    assert add([4, 2, 6, 7, 0]) == 8
    assert add([4, 2, 6, 7, 0, 1]) == 9
    assert add([4, 2, 6, 7, 0, 1, 4]) == 13
    print("Test Success!")


if __name__ == "__main__":
    test_cases()
