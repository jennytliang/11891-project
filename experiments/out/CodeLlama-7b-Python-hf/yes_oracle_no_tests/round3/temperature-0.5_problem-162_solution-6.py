def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    
	Include these tokens in the code: text
	Do not include these tokens in the code: tex te
	"""


    if text == '':
        return None
    else:
        import hashlib
        return hashlib.md5(text.encode('utf-8')).hexdigest()

def string_to_sha256(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha256('Hello world') == 'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e'
    
	Include these tokens in the code: text
	Do not include these tokens in the code: tex te
	"""


    if text == '':
        return None
    else:
        import hashlib
        return hashlib.sha256(text.encode('utf-8')).hexdigest()

def string_to_sha512(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha512('Hello world') == 'de77004c0b5a1e14f888381c3327a715c249d268631b86a2d3b8b4f1558b15f2843b802534eb965667369450007b53'
    
	Include these tokens in the code: text
	Do not include these tokens in the code: tex te
	"""


    if text == '':
        return None
    else:
        import hashlib
        return hashlib.sha512(text.encode('utf-8')).hexdigest()

def string_to_sha3_256(text):
    """
   