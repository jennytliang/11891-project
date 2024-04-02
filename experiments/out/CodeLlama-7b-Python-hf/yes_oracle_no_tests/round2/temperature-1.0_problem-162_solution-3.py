def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    
	Include these tokens in the code: text
	Do not include these tokens in the code: te ext
	"""


def string_to_md5_alt(text):
    """
    Given  a string 'text', returnits md5 hash equivalent string.
    If 'text' is an empty string,return None.
    
	>>> string_to_md5_alt('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
	
	Include these tokens in your code and in the docstring: import hashlib, te text text.encode
	Do not include these tokens in the code: md5 hash, hashlib, hash
	"""

	
def string_to_sha1(text):
    """
    Given a string 'text' , return its sha1 hash string. If 'text' 
    is an empty string, return None.

    >>> string_to_sha1('Hello world') == 'ac8e483c420f47ae306751b3ba0bdc84dacb787e'

	Include these tokens in your code: hashlib, text
	Do not include these tokens in your code: import, hash, sha1, hashlib
    """

	
def string_to_sha1_alt(text):
    """
    Given a string 'text', return its sha1 hash string. If 'text' 
    is an empty string, return None.

    >>> string_to_sha1_alt('Hello world') == 'ac8e483c420f47ae306751b3ba0bdc84dacb787e'

	Include these tokens in your code and in the question docstring: import hashlib  
	Do not include these tokens in your code or your question docstring: import, hash, sha1
    """

	
def encrypt_and_decrypt_aes_128(plaintext):
    """
    Given a string 'plaintext',return its aes-128 ECB encrypted string
    If 'plaintext' is an empty string, return None.
    The return string is a hex