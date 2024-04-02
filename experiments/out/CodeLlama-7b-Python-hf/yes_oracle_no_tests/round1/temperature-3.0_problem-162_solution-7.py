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
    else:
	    return str(hashlib.md5(text).hexdigest())


def main():
    """
    This is a small test that we give to the students.
    You can change the inputs and expected outputs, but
    do not change the function signature.
    """
    print "Testing 'string_to_md5'"
    print string_to_md5('')
    print string_to_md5('Hello world')
    print string_to_md5('This is a test')
    print string_to_md5('Hello')
    print string_to_md5('')


if __name__ == '__main__':
    main()