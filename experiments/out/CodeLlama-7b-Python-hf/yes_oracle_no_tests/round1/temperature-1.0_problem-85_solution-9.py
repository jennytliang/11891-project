def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""
    pass


if __name__ == '__main__':
    import pytest
    import random

    test_cases = (
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6),
        ([1, 2, 3], 0),
        ([2, 4, 6], 4),
        ([0, 2, 4, 6], 0),
        ([2, 4, 2, 4, 2, 4], 12),
        ([4, 8, 0, 2], 0),
        ([9, 5, 8, 98, 90, 49, 98, 41, 50], 106),
        ([2, 90], 2),
        (random.sample(range(1_000), 1_000), random.Random().randint(0, 999_999)),
    )

    for test_case, output in test_cases:
        ans = add(test_case)
        assert ans == output, (ans, output)

        test_case = tuple(element * 5000 for element in test_case)
        ans = add(test_case)
        assert ans == output, (ans, output)

        test_case = tuple(element * 3 for element in test_case)
        ans = add(test_case)
        assert ans == output, (ans, output)

