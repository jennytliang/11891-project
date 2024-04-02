def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""
    for x in l:
        if x >= t:
            return False
    return True


def same_first_last(l: list):
    """Return True if the first element in the list is the same as the last.
    >>> same_first_last([1, 2, 4, 1])
    True
    >>> same_first_last([1, 2, 4, 5, 1])
    False
    
	Include these tokens in the code: return all (l[0] == l[-1]
	"""
    if len(l) == 1:
        return True
    return l[0] == l[-1]


def all_same(l: list):
    """Return True if all elements in the list are the same.
    >>> all_same([1, 1, 1])
    True
    >>> all_same([1, 2, 1])
    False
    
	Include these tokens in the code: return all (l[0] == l[i] for i in range(len(l))
	"""
    if len(l) == 1:
        return True
    for i in range(len(l)):
        if l[0] != l[i]:
            return False
    return True


def make_repeat_last_word(s: str):
    """Return a new sentence which consists of the original sentence, but
    with the last word repeated once at the beginning of the sentence.
    >>> make_repeat_last_word('Hello world')
    'world Hello world'
    >>> make_repeat_last_word('Goodbye, my friend')
    'my friend Goodbye, my friend'
    
	Include these tokens in the code: return s + ' ' + s.split()[-1]
	"""
    return s + ' ' + s.split()[-1]


def has_no_e(s: str):
    """Return True if the given string contains no 'e' characters.
    >>> has_no_e('Hello world')
    True
    >>> has_no_e('Hi there, my name is