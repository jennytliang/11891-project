def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    
	Include these tokens in the code: return number - int
	Do not include these tokens in the code: integer , decimal = str
	"""
    return number - int(number)


def count_vowels(string: str) -> int:
    """ Given a string, return the number of vowels contained within it.
    Vowels are defined as: a, e, i, o, u, y

    Return an integer representing the number of vowels.
    
    >>> count_vowels('hello')
    2
    >>> count_vowels('abcde')
    0
    >>> count_vowels('aeiou')
    5
    >>> count_vowels('python')
    2
    >>> count_vowels('yummy')
    3
    """
    vowels = 'aeiouy'
    count = 0
    for i in string:
        if i in vowels:
            count += 1

    return count


def count_acids(string: str) -> int:
    """ Given a string, return the number of acids contained within it.
    Acids are defined as: a, c, g, t

    Return an integer representing the number of acids.
    
    >>> count_acids('atcg')
    4
    >>> count_acids('atcgta')
    4
    >>> count_acids('gtacg')
    4
    >>> count_acids('atcga')
    4
    >>> count_acids('atcgtt')
    4
    >>> count_acids('atcgt')
    3
    """
    acids = 'acgt'
    count = 0
    for i in string:
        if i in acids:
            count += 1

    return count


def count_letters_in_string(string: str) -> int:
    """ Given a string, return the number of letters contained within it.

    Return an integer representing the number of letters.
    
    >>> count_letters_in_string('hello')
    5
    >>> count_letters_in_string('abcde')
    5
    >>> count_letters_in_string('aeiou