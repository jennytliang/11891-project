def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    
	Include these tokens in the code: if text == " ": return None
	"""
    if text == ' ':
        return None
    return hashlib.md5(text.encode('utf-8')).hexdigest()


def string_to_sha1(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha1('Hello world') == '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed'
    """
    if text == ' ':
        return None
    return hashlib.sha1(text.encode('utf-8')).hexdigest()


def string_to_sha256(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha256('Hello world') == 'b94d27b9934d3e08a52e52d5dbc6d62847a4a52a'
    """
    if text == ' ':
        return None
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def string_to_sha512(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha512('Hello world') == 'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3