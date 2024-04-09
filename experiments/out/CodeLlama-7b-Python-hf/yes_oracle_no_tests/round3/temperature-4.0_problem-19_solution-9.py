from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    tokens = numbers.split()
    tokens.sort()
    return ' '.join(tokens)


def sum_digits(number: str) -> int:
    """ Input is a number in string format.
    Return the sum of the digits in the number
    >>> sum_digits('153')
    9
    """
    return sum(int(c) for c in number)


def count_consonants(word: str) -> int:
    """ Input is a string of lowercase letters.
    Return the number of consonants in the word.
    >>> count_consonants('zebra')
    4
    >>> count_consonants('google')
    5
    """
    vowels = 'aeiou'
    return sum(c not in vowels for c in word)


def is_prime(number: int) -> bool:
    """ Input is a positive integer.
    Return True if the number is prime, False otherwise.
    >>> is_prime(10)
    False
    >>> is_prime(11)
    True
    """
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def sum_primes(number: int) -> int:
    """ Input is a positive integer.
    Return the sum of all prime numbers up to and including the number.
    >>> sum_primes(10)
    17
    >>> sum_primes(15)
    37
    """
    return sum(i for i in range(number + 1) if is_prime(i))


def is_palindrome(string: str) -> bool:
    """ Input is a string.
    Return True if the string is a palindrome, False otherwise.
    >>> is_palindrome('noon')
    True
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('dented')
    False
    """
    return string.lower() == string[::-