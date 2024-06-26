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


def test_shift():
    assert encode_shift("this is a test") == "wkh tpg dhvpx"
    assert decode_shift("wkh tpg dhvpx") == "this is a test"
    assert encode_shift("this is a test") == decode_shift(encode_shift("this is a test"))
    assert encode_shift("this is a test") != encode_shift("this is not a test")
    assert encode_shift("this is a test") != "this is a test"
    assert encode_shift("this is a test") != "wkh tpg dhvpx"
