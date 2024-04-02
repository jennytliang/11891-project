def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    
	Include these tokens in the code: return
	Do not include these tokens in the code: re urn
	"""


    if text  == '':
        return None
    else:
        return hashlib.md5(text.encode()).hexdigest()



def string_to_sha256(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha256('Hello world') == 'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e'
    
	Include these tokens in the code: return
	Do not include these tokens in the code: re urn
	"""


    if text  == '':
        return None
    else:
        return hashlib.sha256(text.encode()).hexdigest()



def string_to_sha512(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha512('Hello world') == 'ddaf6068f466a7181a9548b941f15c6315b707d877742620f58bbf52648983265e13b159620e3a70358803e580f503c4562a5fc0c82b3b45e04c39417b14b0193e894c931e214f15171b721c230b07692232723548c623312f2611b926d545e7a16057a98017932898