def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""
    for x in l:
        if x < t:
            continue
        return False
    return True


def sum_multiples(low: int, high: int, factors: list):
    """Return the sum of all the multiples of the given factors within the given bounds.
    >>> sum_multiples(1, 5, [3, 5])
    30
    >>> sum_multiples(1, 6, [3, 5])
    33
    """
    total = 0
    for i in range(low, high):
        for factor in factors:
            if i % factor == 0:
                total += i
    return total


def count_vowels(s: str):
    """Return the number of vowels in the given string.
    >>> count_vowels("Hello, world!")
    3
    >>> count_vowels("Some eggs, bacon, and spam.")
    5
    """
    vowels = 0
    for char in s:
        if char in "aeiou":
            vowels += 1
    return vowels


def sum_digits(n: int):
    """Sum all the digits of n.
    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    """
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total


def has_hidden_word(word: str, guess: str):
    """Return whether the word contains any of the characters in the guess.
    >>> has_hidden_word('apple', 'ple')
    True
    >>> has_hidden_word('apple', 'banana')
    False
    """
    for char in guess:
        if char in word:
            return True
    return False


def make_word_list(filename: str):
    """Read a file containing