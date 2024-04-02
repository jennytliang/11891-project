def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    even = 0
    odd = 0
    
    while num != 0:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num //= 10
        
    return even, odd

def test_function(test_case):
    even, odd = even_odd_count(test_case)
    if even == test_case_even and odd == test_case_odd:
        print("Pass")
    else:
        print("Fail")

test_case = 123
test_case_even = 1
test_case_odd = 2
test_function(test_case)

test_case = 1234
test_case_even = 2
test_case_odd = 1
test_function(test_case)

test_case = 12345
test_case_even = 2
test_case_odd = 2
test_function(test_case)

test_case = 1234567
test_case_even = 3
test_case_odd = 3
test_function(test_case)

test_case = 123456789
test_case_even = 4
test_case_odd = 5
test_function(test_case)

test_case = -12
test_case_even = 1
test_case_odd = 1
test_function(test_case)

test_case = -123
test_case_even = 1
test_case_odd = 2
test_function(test_case)

test_case = -1234
test_case_even = 1
test_case_odd = 2
test_function(test_case)

test_case = -12345
test_case_even = 1
test_case_odd = 2
test_function(test_case)

test_case = -1234567
test_case_even = 2
test_