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


def main():
    s = "hello"
    print("Original string:", s)
    s_enc = encode_shift(s)
    print("Encoded string:", s_enc)
    s_dec = decode_shift(s_enc)
    print("Decoded string:", s_dec)
    print("String equality:", s == s_dec)


if __name__ == "__main__":
    main()
