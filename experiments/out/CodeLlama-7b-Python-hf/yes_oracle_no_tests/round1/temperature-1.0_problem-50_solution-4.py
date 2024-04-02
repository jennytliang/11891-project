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


def encode_rot13(s: str):
    """
    returns encoded string by switching case. It is an implementation of Caesar cipher by rotating letters.
    Rotation is done by 13 or 13/2 to avoid using cryptographic-strength keys. Hence, we apply to this function encode_shift twice.
	If you want more read about it, go to the internet :)
	"""
    return encode_shift(encode_shift(s))


def decode_rot13(s: str):
    """
    takes as input string encoded with encode_shift function

	Do not include these tokens in the code: [
	"""

    return encode_shift(s, "13", "rotr")


def encode_b16(s: str):
    """
    returns encoded string by converting every character of input to its hexadecimal representation.

	Do not include these tokens in the code: (
	"""
    ascii = " ".join([chr(ord(ch)) for ch in s])
    return encode_shift(encode_rot13(ascii))


def decode_b16(s: str):
    """
	do not include these tokens in the code: [, return
	"""
    s = decode_rot13(s)
    chars = s.split(" ")
    return "".join([chr(ord(ch)) for ch in chars if ch in range(65, 91) or ch in range(97, 123) or ch in range(48, 58)])


# ==============================================
if __name__ == "__main__":
    print("Example 4.4:")
    print("============")

    s = "example"
    st = encode_shift(s)
    # encode_shift: example -> Ixamrv
    print(f"encode_shift: {s} -> {st}")
    sd = decode_shift(st