from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    # return " ".join(sorted(numbers.split(), key=int))
    return " ".join(sorted(numbers.split(), key=lambda x: int(x.replace(" ", ""))))


def palindrome(word: str) -> bool:
    """ Input is a string of lowercase letters.
    Return true if the string is a palindrome.
    A palindrome is a string that reads the same forwards and backwards, ignoring punctuation,
    capitalization, and spacing.
    >>> palindrome('racecar')
    True
    
	Include these tokens in the code: to _ =
	"""
    # return word.lower().replace(" ", "") == word.lower().replace(" ", "")[::-1]
    return word.lower().replace(" ", "") == "".join(reversed(word.lower().replace(" ", "")))


def is_valid_ip(ip: str) -> bool:
    """ Input is a string that represents an IP address.
    Return true if the input is a valid IP address,
    otherwise return false.
    A valid IP address is a string of the form uuu.vvv.www.xxx,
    where each uuu is an integer between 0 and 255,
    where vvv is an integer between 0 and 255,
    where www is an integer between 0 and 255,
    and where xxx is an integer between 0 and 255.
    Leading zeros are not allowed, except for uuu and xxx may contain leading zeros.
    >>> is_valid_ip('12.34.56.78')
    True
    >>> is_valid_ip('123.456.789.0')
    False
    >>> is_valid_ip('123.045.067.089')
    False
    >>> is_valid_ip('123.456.789')
    False
    >>> is_valid_ip('123.456.789.000')
    False
   