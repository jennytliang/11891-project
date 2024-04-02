def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    even = 0
    odd = 0
    if num < 0:
        num = -num
    while num > 0:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10
    return (even, odd)


def test_function(test_case):
    even_number, odd_number = even_odd_count(test_case)
    if even_number == test_case[0] and odd_number == test_case[1]:
        print("Pass")
    else:
        print("Fail")


test_case = (1, 2)
test_function(test_case)

test_case = (2, 3)
test_function(test_case)

test_case = (-1, 0)
test_function(test_case)

test_case = (-123, 3)
test_function(test_case)

test_case = (-12, 2)
test_function(test_case)
