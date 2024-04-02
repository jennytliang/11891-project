def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    
	Include these tokens in the code: text
	Do not include these tokens in the code: te if __ name __
	"""


    if text == '':
        return None
    import hashlib
    hash_obj = hashlib.md5(text.encode())
    return hash_obj.hexdigest()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
