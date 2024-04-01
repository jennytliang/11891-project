def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    
	Include these tokens in the code: " ":
	Do not include these tokens in the code: ' ': 
	"""

    if text ==  " ":
        return None
    else:
        return hashlib.md5(text.encode('utf-8')).hexdigest()


def string_to_sha256(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha256('Hello world') == 'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e'
    
	Include these tokens in the code: " ":
	Do not include these tokens in the code: ' ': 
	"""

    if text == " ":
        return None
    else:
        return hashlib.sha256(text.encode('utf-8')).hexdigest()


def string_to_sha512(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha512('Hello world') == '8ff91a9b791c8f326b2ac3b21e715e9238b62c3b8d706109bd46e0eeb8a0c6c9'
    
	Include these tokens in the code: " ":
	Do not include these tokens in the code: ' ': 
	"""

    if text == " ":
        return None
    else:
        return hashlib.sha512(text.encode('utf-8')).hexdigest()


def string_to_sha3_512(text):
    """
    Given a string 'text', return its sha3_512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha3_