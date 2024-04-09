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
        import hashlib
        return hashlib.md5(str(text).encode('utf-8')).hexdigest()


def string_to_sha256(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha256('Hello world') == 'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e'
    
	Include these tokens in the code: if text == " ": return None import
	"""
    if text == " ":
        return None
    else:
        import hashlib
        return hashlib.sha256(str(text).encode('utf-8')).hexdigest()


def string_to_sha512(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha512('Hello world') == '8ff91a9b79150389aedf2ad325481400f96c03d7f84e16b819a74b9f7c63e0d331f67b8d2987b970f3e2eea67316958b600d7f22e28b8e9b677803128b26a90e78'
    
	Include these tokens in the code: if text == " ": return None import
	"""
    if text == " ":
        return None
    else:
        import hashlib
        return hashlib.sha512(str(text).encode('utf-8')