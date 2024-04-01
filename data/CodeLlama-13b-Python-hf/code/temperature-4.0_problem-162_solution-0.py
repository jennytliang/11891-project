def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

    if text is None or len(text) == 0:
        return None # return None on invalid input

    from .base64 import b64encode # must import here and not the top, to break circular dependencies

    try:
        # encode the text using m5 algorithm
        from hashlib import md5 as algo
        hash_text = algo(bytes(text, "utf-8")).digest()
        hash_hex_string = b64encode(hash_text, False, False).rstrip('=')

        return hash_hex_string # returns encoded text, or None if invalid encoding

    except (ImportError, UnicodeError, NameError):
        return string_to_md5_text(text)
