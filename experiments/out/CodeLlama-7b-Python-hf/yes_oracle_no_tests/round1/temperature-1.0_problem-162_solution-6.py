def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    
	Include these tokens in the code: if text == " ": return None
	"""
    # your code here
    from hashlib import md5
    hash_func = md5()
    hash_func.update(str(text).encode('utf-8'))
    return hash_func.hexdigest()

    # for empty string
    if text == "":
        return None


def string_to_sha256(text):
    from hashlib import sha256
    hash_func = sha256()
    hash_func.update(str(text).encode('utf-8'))
    return hash_func.hexdigest()


def md5_to_string(a_hash):
    """
    Return a string representation of this 'a_hash' string.

    >>> md5_to_string('3e25960a79dbc69b674cd4ec67a72c62') == 'Hello world'
    True

    >>> md5_to_string('3e25960a79dbc69b674cd4ec67a72c61') == None
    True
    """
    from hashlib import md5
    hash_func = md5()
    hash_func.update(str(a_hash).encode('utf-8'))
    return hash_func.hexdigest()


def is_rotation(s_1, s_2):
    if s_1 == s_2:
        return True
    for i in range(0, len(s_2)):
        res = (s_1 + s_1)[i:i + len(s_2)]
        if res == s_2:
            return True
        if s_2 == None:
            return False
    return False


def rotate_by_1(s):
    """
    Rotate this string by 1 element (in the string version of the string).

    >>> rotate_by_1('abcd') == 'dbca'
    True

    >>> rotate_by_1('a') == 'a'
    True

    >>> rotate_by_1('abc') ==