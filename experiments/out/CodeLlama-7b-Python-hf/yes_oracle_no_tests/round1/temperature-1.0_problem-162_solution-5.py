def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    
	Include these tokens in the code: " ":
	Do not include these tokens in the code: ' ':
	"""

    if text == '':
        return None
    else:
        import hashlib
        return hashlib.md5(text.encode()).hexdigest()


def string_to_sha256(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha256('Hello world') == 'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e'
    """

    if text == '':
        return None
    else:
        import hashlib
        return hashlib.sha256(text.encode()).hexdigest()


def string_to_sha512(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha512('Hello world') == 'ef537f25c895bfa782526529a9b63d97aa631564d5d789c2b759c2e9dd6e9f05af6b639fa3ee58b17cf043c4381d55e293d32b24281d85f2d975288726b03c4'
    """

    if text == '':
        return None
    else:
        import hashlib
        return hashlib.sha512(text.encode()).hexdigest()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
