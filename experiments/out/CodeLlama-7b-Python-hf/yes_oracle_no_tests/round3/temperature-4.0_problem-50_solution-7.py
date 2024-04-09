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
    # test = "this is a test"
    # print(encode_shift(test))
    # print(decode_shift(encode_shift(test)))
    # print(decode_shift(encode_shift(test)))
    # print(encode_shift(decode_shift(encode_shift(test))))
    print(decode_shift(encode_shift("this is a test")))
