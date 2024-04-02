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
    else:
        # hashlib.md5(text.encode())
        return hashlib.md5(text.encode()).hexdigest()

def string_to_sha256(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha256('Hello world') == 'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e'
    """
    import hashlib

    if text == " ":
        return None
    else:
        #hashlib.sha256(text.encode())
        return hashlib.sha256(text.encode()).hexdigest()

def string_to_sha512(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha512('Hello world') == '8cc1633ecd1ed39f009da7742236b9f8d57032b240565107a9355086683f06ae125412a91509508b3a311759d3a4948d1a265eb676966f0c44b11c40f7eea00'
    """
    import hashlib

    if text == " ":
        return None
    else:
        #hashlib.sha512(text.encode())
        return hashlib.sha512(text.encode()).hexdigest()

def string_to_sha3_256(text):
   