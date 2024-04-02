def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Include these tokens in the code: string
	Do not include these tokens in the code: st ri
	"""


    retur = 0
    for i in string:
        retur += 1
    return retur



def is_palindrome(string: str) -> bool:
    """ Return True if string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('a')
    True
    >>> is_palindrome('aa')
    True
    >>> is_palindrome('baa')
    False
    >>> is_palindrome('abba')
    True
    >>> is_palindrome('abcba')
    True
    """

    # Base case: empty string
    if string == '':
        return True

    # Base case: string with one character
    if len(string) == 1:
        return True

    # Recursive case:
    return string[0] == string[-1] and is_palindrome(string[1:-1])



def fib(n: int) -> int:
    """ Return nth Fibonacci number
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(10)
    55
    """
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)



def count_lines(filename: str) -> int:
    """ Return number of lines in file
    >>> count_lines('')
    0
    >>> count_lines('f.py')
    1
    >>> count_lines('f.py')
    1
    >>> count_lines('f.py')
    1
    """

    with open(filename, 'r') as f:
        lines = f.readlines()
    return len(lines)