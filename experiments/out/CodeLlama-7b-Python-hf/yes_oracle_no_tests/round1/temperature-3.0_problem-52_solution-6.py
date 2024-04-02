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
            return True
        else:
            return False


def front_back(a: str, b: str) -> str:
    """Return a string where the first char of a is followed by
    the first char of b, followed by the second char of a,
    followed by the second char of b, and so on.
    >>> front_back('abc', 'xyz')
    'axbycz'
    >>> front_back('aaa', 'bbb')
    'aabbb'
    >>> front_back('PQR', 'STU')
    'PSQRTU'
    """
    x = len(a)
    y = len(b)
    if x < y:
        return a[0] + b[:x] + a[1:] + b[x:]
    elif x > y:
        return a[0] + b[:y] + a[1:] + b[y:]
    else:
        return a[0] + b[0] + a[1] + b[1]


def last2(s: str) -> str:
    """Return a string where the last 2 chars of each word
    in the input string are put together (in lowercase) at
    the end of the string, so you end up with a single word.
    Note: A word is a sequence of charcters that is
    separated from other words by white space.
    >>> last2('hello world')
    'hello wolrd'
    >>> last2('hello  world')
    'hello wolrd'
    >>> last2('hello')
    'hello'
    >>> last2('')
    ''
    """
    s = s.split()
    for i in s:
        if len(i) < 2:
            continue
        s[-1] = s[-1] + i[-2:]
    return " ".join(s)


def front3(s: str) -> str:
    """Return a string where the first 3 chars of each word
    in the input string are put together (in lowercase) at
   