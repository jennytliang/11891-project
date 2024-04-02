def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    # pass
    even, odd = 0, 0
    for i in str(abs(num)):
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


# TEST
test_cases = [
    (123, (1, 2)),
    (1234, (2, 2)),
    (-12, (1, 1)),
    (-123, (1, 2)),
    (-1234, (2, 2)),
    (0, (1, 0)),
    (100, (1, 1)),
    (101, (1, 2)),
    (-100, (1, 1)),
    (-101, (1, 2)),
    (1000, (2, 1)),
    (1001, (2, 2)),
    (-1000, (2, 1)),
    (-1001, (2, 2)),
    (1010, (2, 2)),
    (-1010, (2, 2)),
]
for num, expected in test_cases:
    result = even_odd_count(num)
    if result == expected:
        print("PASSED: even_odd_count({}) returned {}".format(num, result))
    else:
        print("FAILED: even_odd_count({}) returned {}, answer: {}".format(num, result, expected))
