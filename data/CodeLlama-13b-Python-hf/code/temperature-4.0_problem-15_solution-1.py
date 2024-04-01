def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return ""

# def fizzbuzz():


def string_chop(s: str, cut:int):
    """" Returns a list of slices strings from s by cutting s from left using cut sizes

    >>>string_chop('the quick brown fox', 2)

    [
    ('th', 'he quick', 'qu', 'i', 'ck b', 'rown', 'fo', 'ox')
     ]
    
    >>> string_chop('thedreamistream',4)
    [] """