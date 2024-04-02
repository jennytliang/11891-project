def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    even = odd = 0
    while num > 0:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10
    return even, odd


def test_function(test_case):
    even, odd = even_odd_count(test_case)
    if even == test_case[0] and odd == test_case[1]:
        print("Pass")
    else:
        print("Fail")


test_function(123)
test_function(98745)
test_function(12345)
test_function(-123)
test_function(-98745)
test_function(-12345)
