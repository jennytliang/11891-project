def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Do not include these tokens in the code: for x in l :
	"""
    # for x in l:
    #     if x >= t:
    #         return False
    # return True
    return all(x < t for x in l)


def get_word_score(word: str, n: int):
    """Return the score for a word.
    >>> get_word_score('abc', 20)
    3
    >>> get_word_score('abc', 2)
    0
    >>> get_word_score('abc', 10)
    1
    >>> get_word_score('xyz', 5)
    0
    
    A word's score is the sum of the first four of its letters' unicode codes,
    if the word's length is at least 4.
    If the word's length is less than 4, just return the sum of the unicode
    codes of the first 4 letters of the alphabet.
    """
    # if len(word) >= 4:
    #     return sum(ord(x) for x in word[:4])
    # else:
    #     return sum(ord(x) for x in word + 'abc'[:4 - len(word)])
    return sum(ord(x) for x in word[:min(n, 4)])


def compound_interest(amount: float, interest_rate: float, time: int):
    """Return the amount on a compound interest account after time periods.
    
    >>> compound_interest(100, 0.05, 2)
    105.0
    >>> compound_interest(100, 0.05, 3)
    110.25
    >>> compound_interest(100, 0.05, 4)
    115.8125
    >>> compound_interest(100, 0.05, 5)
    121.546875
    >>> compound_interest(100, 0.05, 0)
    100
    """
    return amount * (1