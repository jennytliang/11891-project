def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Do not include these tokens in the code: even , odd = 0
	"""
    # Your code here
    even = 0
    odd = 0
    if num < 0:
        num = -num
    while num > 0:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num //= 10
    return (even, odd)


def test_function(test_case):
    even_count, odd_count = test_case
    test_result = even_odd_count(test_case)
    if test_result == (even_count, odd_count):
        print("Pass")
    else:
        print("Fail")


test_function((1, 2))
test_function((1, 0))
test_function((0, 0))
test_function((10, 0))
test_function((20, 1))
test_function((1234567890, 5))
test_function((-1234567890, 6))
test_function((-123, 2))
test_function((-1, 1))
test_function((-10, 1))
test_function((-100, 2))
test_function((0, 0))
test_function((10, 1))
test_function((100, 2))
test_function((1000, 3))
test_function((-1000, 4))
test_function((12345, 2))
test_function((-12345, 2))
test_function((123456789, 5))
test_function((-123456789, 5))
test_function((1234567890, 5))
test_function((-1234567890, 6))
test_function((123456789012345678901234567890123