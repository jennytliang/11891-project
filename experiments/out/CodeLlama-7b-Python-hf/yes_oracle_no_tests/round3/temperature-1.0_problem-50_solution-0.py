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
    assert encode_shift("Hello") == "Mjqqt", "Shift"
    assert decode_shift("Mjqqt") == "Hello", "Decode"
    assert encode_shift("How are you?") == "Beznkrelhvutw", "Shift"
    assert decode_shift("Beznkrelhvutw") == "How are you?", "Decode"
    assert decode_shift(encode_shift("Who are you?")) == "Who are you?", "Decode"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
