def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    
	Include these tokens in the code: d = '
	Do not include these tokens in the code: return s . translate ( str . m ak etr
	"""

    
    rotated = ""
    for char in s:
        if char.isalpha():
            if char.isupper():
                rotated += chr((ord(char) - ord('A') + 2) % 26 + ord('A'))
            else:
                rotated += chr((ord(char) - ord('a') + 2) % 26 + ord('a'))
        else:
            rotated += char
    
    return rotated


# tests

def test_encrypt():
    assert encrypt('hi') == 'lm'
    assert encrypt('asdfghjkl') == 'ewhjklnop'
    assert encrypt('gf') == 'kj'
    assert encrypt('et') == 'ix'


if __name__ == '__main__':
    test_encrypt()
