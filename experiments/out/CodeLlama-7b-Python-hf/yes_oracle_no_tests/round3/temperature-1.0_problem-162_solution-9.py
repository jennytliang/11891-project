def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    
	Include these tokens in the code: if text == " ": return None import
	"""
    if text == " ":
        return None
    else:
        return hashlib.md5(text.encode('utf-8')).hexdigest()


def string_to_sha3(text):
    """
    Given a string 'text', return its sha3 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha3('Hello world') == 'c283d6a210b49e88d8f7f574d846b9ae6e061f06996e759f8b62544804288e3b'
    
	Include these tokens in the code: if text == " ": return None import
	"""

    if text == " ":
        return None
    else:
        return hashlib.sha3_256(text.encode('utf-8')).hexdigest()


def string_to_sha256(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha256('Hello world') == '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
    
	Include these tokens in the code: if text == " ": return None import
	"""

    if text == " ":
        return None
    else:
        return hashlib.sha256(text.encode('utf-8')).hexdigest()


def string_to_sha224(text):
    """
    Given a string 'text', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha224('Hello world') == '2c6b380d6ed5