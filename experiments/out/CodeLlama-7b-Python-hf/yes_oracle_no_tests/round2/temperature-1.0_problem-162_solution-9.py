def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    
	Include these tokens in the code: text
	Do not include these tokens in the code: te zt
	"""


    if len(text) > 0:
        md5_hash = ''
        # hash the text
        try:
            pass
        except:
            print("Error in md5_hash: hash function failed")
            return None
        # return the hash as a string of 32 hex digits
        pass
    else: # text is empty
        return None


def check_md5(file_name, hash_string):
    """
    Compares hash of 'file_name' with the string 'hash_string', printing a message saying 'file_name' is corrupt or not corrupt
	If 'file_name' does not exist, print that 'file_name' does not exist. The parameter 'hash_string' should be passed to this function as a string.
	The 'hash_string' is the md5 hash of the file.

    >>> check_md5('text_file_example.txt', '2cac14130c50e6e73c0c66b87573bedb')
     text_file_example.txt is corrupt
	
	Include these tokens in the code: file name, hash
	Do not include these tokens in the code: text file example
	"""
	

if __name__ == '__main__':
    import doctest
    doctest.testmod()
