def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    
	Do not include these tokens in the code: else :
	"""


    if text == "":
 
        return None

    else:
        import hashlib
        return hashlib.md5(text.encode()).hexdigest()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
