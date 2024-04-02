def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    
	Include these tokens in the code: if text == " ": return None
	"""
    import hashlib

    if text == " ":
        return None
    hash_object = hashlib.md5(text.encode('utf-8'))
    return hash_object.hexdigest()


def string_to_sha256(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha256('Hello world') == 'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e'
    
	Include these tokens in the code: if text == " ": return None
	"""
    import hashlib

    if text == " ":
        return None
    hash_object = hashlib.sha256(text.encode('utf-8'))
    return hash_object.hexdigest()


def string_to_sha512(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha512('Hello world') == 'ef134f1f52c5ecd93bd03d0a38a033e911487843b3230959fdb06117372e78b9e1b1a7e095652179241c445744b607702409e5f0a0e315f049898c47761f897328485d04b497778c1c35df2361d40c8f023004c1f10f0440299ea0e9e49182