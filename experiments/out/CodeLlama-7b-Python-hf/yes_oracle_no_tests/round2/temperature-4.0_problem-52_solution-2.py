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
    return False
    

def is_triple_double(w: str):
    """Returns True if the string w has 3 consecutive double letters.
    >>> is_triple_double('hello')
    False
    >>> is_triple_double('hheellllooo')
    False
    >>> is_triple_double('helloo')
    True
    >>> is_triple_double('hellooo')
    False
    >>> is_triple_double('hhlloo')
    False
    >>> is_triple_double('hoo')
    True
    >>> is_triple_double('hooo')
    False
    >>> is_triple_double('')
    False
    >>> is_triple_double('a')
    False
    >>> is_triple_double('aa')
    False
    >>> is_triple_double('aaa')
    True
    >>> is_triple_double('aaaa')
    False
    >>> is_triple_double('aaaab')
    True
    >>> is_triple_double('aab')
    True
    >>> is_triple_double('aaab')
    False
    """
    for i in range(len(w)-2):
        if w[i] == w[i+1] and w[i+1] == w[i+2]:
            return True
    return False
