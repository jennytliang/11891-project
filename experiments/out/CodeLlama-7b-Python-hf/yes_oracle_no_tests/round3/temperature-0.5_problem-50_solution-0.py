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
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert encode_shift("Coding") == "Gohzgp", "First"
    assert encode_shift("Hello") == "Mjqqt", "Second"
    assert encode_shift("A") == "F", "Third"
    assert encode_shift("Z") == "C", "Fourth"
    assert encode_shift("") == "", "Empty"
    assert decode_shift("Gohzgp") == "Coding", "Decode First"
    assert decode_shift("Mjqqt") == "Hello", "Decode Second"
    assert decode_shift("F") == "A", "Decode Third"
    assert decode_shift("C") == "Z", "Decode Fourth"
    assert decode_shift("") == "", "Empty"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
