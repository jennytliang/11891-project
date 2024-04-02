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
    
	Include these tokens in the code: d = ' abc
	Do not include these tokens in the code: pass
	"""
    # TODO: write your answer between # START and # END
    # START
    d = ' abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    return s.translate(str.maketrans(d, d[2:] + d[:2]))
    # END


# tests
import pytest

from cryptocode import encrypt

@pytest.mark.parametrize('input, expected', [
    ('hi', 'lm'),
    ('asdfghjkl', 'ewhjklnop'),
    ('gf', 'kj'),
    ('et', 'ix'),
])
def test_encrypt(input, expected):
    actual = encrypt(input)
    assert actual == expected

def test_encrypt_empty():
    actual = encrypt('')
    assert actual == ''

def test_encrypt_none():
    actual = encrypt(None)
    assert actual == ''
