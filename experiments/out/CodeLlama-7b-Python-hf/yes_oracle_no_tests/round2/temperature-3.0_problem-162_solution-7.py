def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    
	Include these tokens in the code: import hash lib
	Do not include these tokens in the code: else :
	"""


    if text == "":
 	    ret = None
    else:
        import hashlib
        ret = hashlib.md5(text.encode('utf-8')).hexdigest()
    return ret

if __name__ == "__main__":
    import doctest
    doctest.testmod()
