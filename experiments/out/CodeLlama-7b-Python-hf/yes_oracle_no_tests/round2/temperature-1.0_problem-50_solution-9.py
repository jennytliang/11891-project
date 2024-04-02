def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""

    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


def encode_rot(s: str):
    """
    returns encoded string by splitting the string into strings with odd
    & even length, and rotating the string with odd length.
    example:
	'abcde' -> 'abcde'
	'abc' -> 'cab'
 
    NOTE: for rotating a string, you need to know that `s[:1] +  s[1+:]` is equivalent to `s[1:] + s[:1]`
    """
    a = lambda s, x: s[:x] + s[x:]
    return (
        ((encode_shift(a(s, len(s) // 2)) + s[1 if len(s) % 2 else 2:]) if s else "")
        if s
        else ""
    )


def _decode_rot(s: str):
    a = lambda s, x: s[:x] + s[x:]
    return (
        ((decode_shift(a(s, len(s) // 2)) + s[1 if len(s) % 2 else 2:]) if s else "")
        if s
        else ""
    )


# _decode_rot is wrapped into a lambda which makes it possible to use the builtin function id
_decode_rot.__name__ = lambda_name = "decode_rot13"
# _decode_rot.__qualname__ is not updated for some reason
_decode_rot.__qualname__ = lambda_name + ".lambda_func"
# _decode_rot.__doc__ is not updated for some reason
_decode_rot.__doc__ = lambda_name + """
    takes as input string encoded with encode_rot function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""


@_decorated(fn=lambda_name)
class MyEncoder:
    def encode(self, s: str):
        return encode_shift(s)

    def decode(self, s: str):