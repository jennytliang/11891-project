def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: for ch in str ( num ):
	"""


    even, odd = 0, 0

    for ch in str(num):
        if int(ch) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

def even_odd_count2(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: for ch in str ( num ):
	"""


    even, odd = 0, 0

    for ch in num:
        if ch % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

def even_odd_count3(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: for ch in str ( num ):
	"""


    even, odd = 0, 0 
    for ch in str(num):
        if ch % 2 == 0: even += 1
        else: odd += 1
    return even, odd


# tests
import pytest

from even_odd import even_odd_count, even_odd_count2, even_odd_count3


@pytest.mark.parametrize("f",
                         [even_odd_count,
                          even_odd_count2,
                          even_odd_count3,
                         ])
def test_even_odd_count(f):
    # test some 4-digit cases
    cases = [(-12, (1, 1)),
             (123, (1, 2)),
             (134, (1,