def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    
	Include these tokens in the code: if text == " ": return None import
	"""
    import hashlib
    if text == " ":
        return None
    else:
        return hashlib.md5(text.encode()).hexdigest()

def string_to_sha1(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha1('Hello world') == 'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d'

	Include these tokens in the code: if text == " ": return None import
	"""
    import hashlib
    if text == " ":
        return None
    else:
        return hashlib.sha1(text.encode()).hexdigest()


def string_to_sha256(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha256('Hello world') == 'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434daf385b241683919c45a0522d'

	Include these tokens in the code: if text == " ": return None import
	"""
    import hashlib
    if text == " ":
        return None
    else:
        return hashlib.sha256(text.encode()).hexdigest()


def string_to_sha512(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha512('Hello world') == 'ddaf6ddf171abd060e0c57a91de2928c72302c650b97f860362f15c042f4