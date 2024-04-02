def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Do not include these tokens in the code: # TODO : Write your solution here
	"""
    # write your code here
    even = 0
    odd = 0
    for i in str(num):
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)


# TESTS
assert even_odd_count(-12) == (1, 1)
assert even_odd_count(123) == (1, 2)
assert even_odd_count(1023) == (3, 0)
assert even_odd_count(20010) == (5, 1)
