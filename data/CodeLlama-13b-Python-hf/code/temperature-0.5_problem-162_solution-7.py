def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    import hashlib
    if text == '':
        return None
    return hashlib.md5(text.encode('utf-8')).hexdigest()


def string_to_sha1(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha1('Hello world') == '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed'
    """
    import hashlib
    if text == '':
        return None
    return hashlib.sha1(text.encode('utf-8')).hexdigest()


def string_to_sha256(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha256('Hello world') == 'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e'
    """
    import hashlib
    if text == '':
        return None
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def string_to_sha512(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha512('Hello world') == 'dcd03f846953fa85469d7e45840e41a89f31fc33f20ec52f1b03befc5a4a4e493f89fd4c9c5b6e5b7db3adab9b6e960d02569738f8c3923e9ac6e8dd6240609da'
    """
    import hashlib
    if text == '':
        return None
    return hashlib.sha512(text.encode('utf-8')).hexdigest()
