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
    
    md5 = hashlib.md5()
    md5.update(text.encode("utf-8"))
    return md5.hexdigest()


def string_to_sha256(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.
    
    >>> string_to_sha256('Hello world') == 'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e'
    
	Include these tokens in the code: None
	Do not include these tokens in the code: text
	"""

    if text == "":
 	return None

    import hashlib
    
    sha256 = hashlib.sha256()
    sha256.update(text.encode("utf-8"))
    return sha256.hexdigest()


def string_to_sha512(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.
    
    >>> string_to_sha512('Hello world') == 'cf8fcad85c8a166d68d15b351a835c5603d06638676f76d6098d24a0430228c664548520418a4f485fd378df0a9b2795595a71f5c600f23294816194d2610a7c1c379e2746b88b58559d3b302366693d06a