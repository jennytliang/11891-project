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


def encode(text: str, key: list):
    """
    Returns encode by using cipher key.
    """
    cipher = []
    k1, k2 = [int(x) for x in key[0].split(",")]
    for i in range(len(text)):
        if i % 2 == 0:  # 2i
            cipher.append(text[i].encode().hex())
        else:  # 2i + 1
            s = text[i].encode().hex()
            s = "{0:0>4}".format(s)
            s = "".join([s[k1 * i1 : k2 * i2] for i1, i2 in zip(range(0, len(s), k1), range(k1, len(s) + k1, k1))])
            cipher.append(s)
    encoded = " ".join([x.upper() for x in cipher])
    return encoded


def decode(encode: str, key: list) -> str:
    # Decoding the encoded code
    data = encode.split()
    k1, k2 = [int(x) for x in key[0].split(",")]
    dec = "".join([t for t in data if (not bool(k1 * k2) and len(t) == (k2 - k1)) or bool(k1 * k2 and len(t) == (((k2) / k1) - 1) * k1 + (k1 - k2))])
    dec = "".join([" ".join(["\u0020".join([l for l in [dec[y - 1 : y + k1] for y in range(k1, len(dec) - k1 + 1, k1)][x]]).encode())
                   for x in range(1, int(len([t for t in data if len(t) == ((k2 - k1) // k1) * k1 +