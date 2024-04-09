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


if __name__ == "__main__":
    # Tests
    assert encode_shift("abc") == "fji"
    assert encode_shift("xyz") == "abc"
    assert encode_shift("XYZ") == "ABC"
    assert encode_shift("Abc") == "Fji"
    assert encode_shift("123") == "987"
    assert encode_shift("1a2b3c") == "1fj2i3h"
    assert encode_shift("1a2b3c4d") == "1fj2i3h4g"
    assert encode_shift("1a2b3c4d5e") == "1fj2i3h4g5f"
    assert decode_shift("1fj2i3h4g5f") == "1a2b3c4d5e"
    assert decode_shift("1fj2i3h4g5f") == encode_shift(decode_shift("1fj2i3h4g5f"))

    # Tests for user input
    s = input("Enter string: ")
    print(f"Encoded string: {encode_shift(s)}")
    print(f"Decoded string: {decode_shift(s)}")
