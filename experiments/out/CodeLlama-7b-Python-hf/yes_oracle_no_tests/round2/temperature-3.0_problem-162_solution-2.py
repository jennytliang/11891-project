def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    
	Include these tokens in the code: return
	"""


    if text  == "":
        return None
    else:
        return hashlib.md5(text.encode('utf-8')).hexdigest()




def md5_to_string(md5):
    """
    Given an string 'md5', return its hash equivalent string.
    If 'md5' is an empty string, return None.

    >>> md5_to_string('3e25960a79dbc69b674cd4ec67a72c62') == 'Hello world'
    
	Include these tokens in the code: return
	"""


    if md5 == "":
        return None
    else:
        return hashlib.md5(md5.encode('utf-8')).hexdigest()




def string_to_sha1(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha1('Hello world') == 'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d'
    
	Include these tokens in the code: return
	"""
    

    if text == "":
        return None
    else:
        return hashlib.sha1(text.encode('utf-8')).hexdigest()




def sha1_to_string(sha1):
    """
    Given a string 'sha1', return its hash equivalent string.
    If 'sha1' is an empty string, return None.

    >>> sha1_to_string('aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d') == 'Hello world'
    
	Include these tokens in the code: return
	"""


    if sha1 == "":
        return None
    else:
        return hashlib.sha1(sha1.encode('utf-8')).hexdigest()
