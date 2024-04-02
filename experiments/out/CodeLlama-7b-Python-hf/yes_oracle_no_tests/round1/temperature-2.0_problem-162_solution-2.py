def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    
	Include these tokens in the code: " ":
	Do not include these tokens in the code: ' ':
	"""

    if texx == ' ':
        return None
    else:
        return hashlib.md5(text.encode('utf-8')).hexdigest()


def string_to_sha256(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha256('Hello world') == 'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e'
    """

    if texx == ' ':
        return None
    else:
        return hashlib.sha256(text.encode('utf-8')).hexdigest()


def string_to_sha512(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha512('Hello world') == '8ff91a9b791503fa0296577a5e74afe6b0405709e9d1453252927f1110e4e0b7c55956c0aa2345a23d3a74b5c950e957f7c0039b26b76922d6c3e304608234c56e855ec9797c0f7a283d9b908456c39892f1f45b6b15231b344084170f7c093a04f4d924181142063f2945156292977b2f47