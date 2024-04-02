def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    
	Include these tokens in the code: ":
	"""

    if text == '':
        return None

    import hashlib
    return hashlib.md5(text.encode('utf-8')).hexdigest()


def string_to_sha256(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha256('Hello world') == 'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e'
    
	Include these tokens in the code: ":
	"""

    if text == '':
        return None

    import hashlib
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def string_to_sha512(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha512('Hello world') == '8cc16f7fa277365b475c8c113d3e3e34846d5d413633570994faa70195c0c630390c116b2291bdd6699a0b33cce987f98c1f8c8730d2c01c7b231277b34f7f1333028811710191bc032c236149c8454de7'
    
	Include these tokens in the code: ":
	"""

    if text == '':
        return None

    import hashlib
    return hashlib.sha512(text.encode('utf-8')).