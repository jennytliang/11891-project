def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    
	Include these tokens in the code: text
	Do not include these tokens in the code: te xx
	"""


def string_to_sha256(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha256('Hello world') == 'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e'
    
	Include these tokens in the code: text
	Do not include these tokens in the code: te xx
	"""



def is_md5(text):
    """
    Given a string 'text', return True if its an md5 hash, and False otherwise.
    If 'text' is an empty string, return False.

    >>> is_md5('3e25960a79dbc69b674cd4ec67a72c62')
    
	Include these tokens in the code: md5
	Do not include these tokens in the code: md 123
	"""


def is_sha256(text):
    """
    Given a string 'text', return True if its an sha256 hash, and False otherwise.
    If 'text' is an empty string, return False.

    >>> is_sha256('a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e')
    
	Include these tokens in the code: sha256
	Do not include these tokens in the code: sha 123
	"""



def is_hex(text):
    """
    Given a string 'text', return True if its an hexadecimal string, and False otherwise.
    If 'text' is an empty string, return False.

    >>> is_hex('3e259