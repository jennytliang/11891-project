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

    import hashlib

    return hashlib.md5(text.encode()).hexdigest()



def string_to_sha512(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha512('Hello world') == 'fa33b0f8171d35ac9e6309e94374653b90b8bdf499e5bfc987c66ed2b2871137'

	Include these tokens in the code: None
	Do not include these tokens in the code: text
	"""

    if text == "":
 
        return None

    import hashlib

    return hashlib.sha512(text.encode()).hexdigest()



def string_to_crc32(text):
    """
    Given a string 'text', return its crc32 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_crc32('Hello world') == '1e0892b0'

	Include these tokens in the code: None
	Do not include these tokens in the code: text
	"""

    if text == "":
 
        return None

    import binascii

    return binascii.crc32(text.encode()).hex()



def string_to_sha256(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha256('Hello world') == 'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e'
