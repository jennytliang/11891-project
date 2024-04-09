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

    return "".join([chr(((ord(ch) + 21 - ord("a")) % 26) + ord("a")) for ch in s])


if __name__ == "__main__":
    s = "this is a secret message"
    encoded = encode_shift(s)
    print(f"Encoded string: {encoded}")
    decoded = decode_shift(encoded)
    print(f"Decoded string: {decoded}")
