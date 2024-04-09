def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd
	Do not include these tokens in the code: # pass count _
	"""
    # pass count _

    # your code goes here
    even = odd = 0
    for i in str(num):
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


# TEST
test_cases = [
    (123, (1, 2)),
    (12, (2, 0)),
    (101, (1, 1)),
    (0, (2, 0)),
    (2222, (4, 0)),
    (111, (0, 3)),
    (133, (0, 3)),
    (101010, (5, 1)),
]
for num, expected in test_cases:
    result = even_odd_count(num)
    if result == expected:
        print("PASSED: even_odd_count({}) returned {}".format(num, result))
    else:
        print("FAILED: even_odd_count({}) returned {}, answer: {}".format(num, result, expected))

