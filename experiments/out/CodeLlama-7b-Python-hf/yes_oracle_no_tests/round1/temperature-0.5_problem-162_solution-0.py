def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    
	Include these tokens in the code: " ":
	Do not include these tokens in the code: ' ': 
	"""

    if text ==  '':
        return None
    else:
        return md5(text.encode('utf-8')).hexdigest()


def string_to_sha1(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha1('Hello world') == '60b735522d0964e4c6ee1b18e09461309c86a75c'
    
	Include these tokens in the code: " ":
	Do not include these tokens in the code: ' ': 
	"""
    if text ==  '':
        return None
    else:
        return sha1(text.encode('utf-8')).hexdigest()


def string_to_sha256(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha256('Hello world') == '9e107d9d372bb6826bd81d3542a419d6f8e5c0fcd321cd2242e46f1012c044b3'
    
	Include these tokens in the code: " ":
	Do not include these tokens in the code: ' ': 
	"""
    if text ==  '':
        return None
    else:
        return sha256(text.encode('utf-8')).hexdigest()


def string_to_sha512(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha512('Hello world') == '8ff91a132d97e6422d8899493b2425e0