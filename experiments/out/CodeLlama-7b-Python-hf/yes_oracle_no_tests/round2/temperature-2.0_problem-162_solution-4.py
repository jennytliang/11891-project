def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    
	Include these tokens in the code: return
	Do not include these tokens in the code: re =
	"""


    if text  == '':
        return None
    else:
        return hashlib.md5(text.encode()).hexdigest()
    


def string_to_sha256(text):
    """
    Given a string 'text', return its SHA256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha256('Hello world') == 'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e'
        
	Include these tokens in the code: return
	Do not include these tokens in the code: re =
	"""


    if text  == '':
        return None
    else:
        return hashlib.sha256(text.encode()).hexdigest()
    


def string_to_sha512(text):
    """
    Given a string 'text', return its SHA512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha512('Hello world') == 'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e'
        
	Include these tokens in the code: return
	Do not include these tokens in the code: re =
	"""


    if text  == '':
        return None
    else:
        return hashlib.sha512(text.encode()).hexdigest()
    


def string_to_sha3_512(text):
   