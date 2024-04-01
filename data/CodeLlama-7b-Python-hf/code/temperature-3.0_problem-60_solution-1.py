def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    return sum([*range(1, n+1)])




def count_vowels(input_string: str):
    """count_vowels counts the vowels in the input string.
    >>> count_vowels("Hello, world!")
    3
    >>> count_vowels("abcde")
    0
    >>> count_vowels("aAaAAaaaAA")
    3
    """