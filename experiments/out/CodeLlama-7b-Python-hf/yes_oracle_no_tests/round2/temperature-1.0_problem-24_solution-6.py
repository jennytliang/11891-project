def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Include these tokens in the code: range
	Do not include these tokens in the code: r n age
	"""


    foobar = 2
    for i in range(2, n + 1):
        if n % i == 0:
            foobar = i
    return foobar

def largest_divisor_2(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Include these tokens in the code: range
	Do not include these tokens in the code: r n age
	"""


    for i in range(2, n):
        if n % i == 0:
            return i

def largest_divisor_3(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Include these tokens in the code: range
	Do not include these tokens in the code: r n age
	"""


    for i in range(2, n):
        if n % i == 0:
            return i

def largest_divisor_4(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Include these tokens in the code: range
	Do not include these tokens in the code: r n age
	"""


    for i in range(2, n):
        if n % i == 0:
            return i

def largest_divisor_5(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Include these tokens in the code: range
	Do not include these tokens in the code: r n age
	"""


    for i in range(2, n):
        if n % i == 0:
            return i

def largest_divisor_