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


def encode_rotate(s: str):
    """
    takes as input string of lowercase ascii chars except 'j' and returns encoded string.
    """
    # Encode shifted by 13.
    encode_1 = encode_shift(s)

    # Encode shifted by 13 more times.
    cnt = 1
    while cnt < 3:
        encode_more = encode_shift(encode_1)
        encode_1 = encode_more
        cnt += 1

    return encode_1


def decode_rotate(s: str):
    """
    takes as input string encoded with encode_rotate function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""

    # Decode shifted by 13.
    decode_1 = decode_shift(s)

    # Decode shifted by 13 more times.
    cnt = 1
    while cnt < 3:
        decode_more = decode_shift(decode_1)
        decode_1 = decode_more
        cnt += 1

    return decode_1
