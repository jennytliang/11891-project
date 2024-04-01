def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return len(string)


def is_palindrome(string: str) -> bool:
    """ Return whether given string is palindrome (palindrome is a string that can be equally read from left to right or right to left)
    >>> is_palindrome('')
    True
    >>> is_palindrome('a')
    True
    >>> is_palindrome('aa')
    True
    >>> is_palindrome('ab')
    False
    >>> is_palindrome('abcba')
    True
    >>> is_palindrome('abc')
    False
    >>> is_palindrome('abcb')
    False
    """

    return strlen(string) == strlen(string[::-1])


def sum_digits(number: int) -> int:
    """ Return sum of digits of given number
    >>> sum_digits(10)
    1
    >>> sum_digits(42)
    6
    >>> sum_digits(123)
    6
    >>> sum_digits(456)
    15
    >>> sum_digits(12345)
    15
    """

    if number == 0:
        return 0

    return number % 10 + sum_digits(number // 10)


def count_letters(string: str) -> int:
    """ Return number of letters of given string
    >>> count_letters('')
    0
    >>> count_letters('abc')
    3
    >>> count_letters('aaa')
    3
    >>> count_letters('aa11bb22')
    6
    >>> count_letters('AaBbCc')
    6
    >>> count_letters('111111')
    0
    """

    return sum([1 for char in string if char.isalpha()])


def count_letters_case_insensitive(string: str) -> int:
    """ Return number of letters (ignoring case) of given string
    >>> count_letters_case_insensitive('')