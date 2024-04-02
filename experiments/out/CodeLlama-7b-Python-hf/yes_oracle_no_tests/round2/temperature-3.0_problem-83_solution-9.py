def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: return 0 print (
	"""
    # count = 0
    # for i in range(10**(n-1), 10**n):
    #     if str(i).startswith("1") or str(i).endswith("1"):
    #         count += 1
    # return count
    
    # return sum(str(i).startswith("1") or str(i).endswith("1") for i in range(10**(n-1), 10**n))
    
    # return sum(str(i).startswith("1") or str(i).endswith("1") for i in range(10**(n-1), 10**n))
    
    return sum(int(str(i).startswith("1") or str(i).endswith("1")) for i in range(10**(n-1), 10**n))


# TESTS
tests = [
    {
        "params": {
            "n": 2
        },
        "expected": 24
    },
    {
        "params": {
            "n": 3
        },
        "expected": 64
    },
    {
        "params": {
            "n": 4
        },
        "expected": 224
    },
    {
        "params": {
            "n": 5
        },
        "expected": 640
    },
    {
        "params": {
            "n": 6
        },
        "expected": 2240
    },
]
for test in tests:
    params = test["params"]
    expected = test["expected"]
    actual = starts_one_ends(params["n"])
    print("starts_one_ends({}) ->".format(params), actual)
    assert actual == expected
