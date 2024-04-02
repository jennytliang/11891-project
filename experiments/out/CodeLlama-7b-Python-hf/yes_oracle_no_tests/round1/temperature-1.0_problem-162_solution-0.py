def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    
	Include these tokens in the code: " ":
	Do not include these tokens in the code: ' ':
	"""

    if text == ' ':
        return None
    print('Hashing {!r}'.format(text))

    import hashlib
    m = hashlib.md5()
    m2 = hashlib.md5()

    m.update(m2.update(text).digest())
    ### BEGIN SOLUTION
    return m.hexdigest()
    ### END SOLUTION

if __name__ == "__main__":
    import doctest
    doctest.testmod()