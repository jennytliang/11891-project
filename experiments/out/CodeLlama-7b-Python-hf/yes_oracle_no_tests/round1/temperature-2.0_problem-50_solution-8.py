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


# ----------------------------------------------------------------------------------------------------------------------
# Testing
# ----------------------------------------------------------------------------------------------------------------------


def test_encode_shift():
    """
    Tests if encode_shift function works correctly.
    """
    assert encode_shift("abc") == "fhw"
    assert encode_shift("xyz") == "zxx"
    assert encode_shift("abcd") == "fjff"
    assert encode_shift("abcde") == "fjfh"
    assert encode_shift("abcdef") == "fjfi"
    assert encode_shift("abcdefg") == "fjfg"
    assert encode_shift("abcdefgh") == "fjfh"
    assert encode_shift("abcdefghi") == "fjfhj"
    assert encode_shift("abcdefghij") == "fjfhk"
    assert encode_shift("abcdefghijk") == "fjfhl"
    assert encode_shift("abcdefghijkl") == "fjfhm"
    assert encode_shift("abcdefghijklm") == "fjfn"
    assert encode_shift("abcdefghijklmn") == "fjfo"
    assert encode_shift("abcdefghijklmno") == "fjfp"
    assert encode_shift("abcdefghijklmnop") == "fjfq"
    assert encode_shift("abcdefghijklmnopq") == "fjfr"
    assert encode_shift("abcdefghijklmnopqr") == "fjfs"
    assert encode_shift("abcdefghijklmnopqrs") == "fjft"
    assert encode_shift("abcdefghijklmnopqrst") == "fjfu"
    assert encode_shift("abcdefghijklmnopqrstu") == "fjfv"
    assert encode_shift("abcdefghijklmnopqrstuv") == "f