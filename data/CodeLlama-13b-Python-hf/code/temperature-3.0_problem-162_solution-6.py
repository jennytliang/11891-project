def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if len(text) == 0:
        return None

    s = hashlib.sha1()
    s.update(text)
    d = s.hexdigest()
    return d


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    pass