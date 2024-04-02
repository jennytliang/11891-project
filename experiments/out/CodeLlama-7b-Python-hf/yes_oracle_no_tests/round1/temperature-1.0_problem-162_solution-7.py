def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    
	Include these tokens in the code: " ":
	Do not include these tokens in the code: ' ':
	"""

    if te
    sxt == '':
        return None
    return 

print(string_to_md5(' '))    


def rotate_str(s):
    rotated = ''
    for char in s:
        char_ord = ord(char) # ascii to decimal
        if char_ord == 32: # skip spaces
            rotated += ' '
            continue
        
        shifted = char_ord + 1
        if shifted == 124: # wrap A -> z
            shifted -= 1 # to 26
        if shifted == 127: # wrap a -> z
            shifted += 26   
        rotated += chr(shifted)
    return rotated

def main():
    print('Starting test')
    original = 'Hello everyone!'
    rotated = rotate_str(original)
    print(original)
    print(rotated)
    # original has been converted into rotated...
    print('...which of course has been converted into:', rotate_str(rotated)) # which of course has been converted into:  olleh everyone!

main()
