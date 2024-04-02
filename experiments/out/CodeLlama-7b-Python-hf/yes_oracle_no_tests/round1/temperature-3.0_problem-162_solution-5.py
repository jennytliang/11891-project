def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    
	Include these tokens in the code: None
	Do not include these tokens in the code: text
	"""

    if text == "":
 
        return None
    else:
        import hashlib
        return hashlib.md5(str(text).encode('utf-8')).hexdigest()