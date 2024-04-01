def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    
	Include these tokens in the code: ":
	"""


    if texte == '':
        return None
    else:
        return hashlib.md5(texte.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
