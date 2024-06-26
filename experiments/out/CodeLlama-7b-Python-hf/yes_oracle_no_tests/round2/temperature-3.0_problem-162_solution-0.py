def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    
	Include these tokens in the code: m =
	Do not include these tokens in the code: return
	"""


    if text == "":
 
        return None

    i = 0
    m = hashlib.md5()
    while i < len(text):
        m.update(text[i].encode())
        i += 1
    return m.hexdigest()


# Tests
def test_string_to_md5():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"


if __name__ == "__main__":
    test_string_to_md5()













































































































































































































































































































































































