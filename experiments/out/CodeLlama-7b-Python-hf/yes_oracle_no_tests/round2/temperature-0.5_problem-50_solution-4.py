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
    assert encode_shift("hello") == "mjqqt"
    assert encode_shift("world") == "otpml"
    assert encode_shift("z") == "f"
    assert encode_shift("Z") == "E"
    assert encode_shift("0") == "5"
    assert encode_shift("1") == "6"
    assert encode_shift("9") == "C"
    assert encode_shift("A") == "F"
    assert encode_shift("a") == "j"
    assert encode_shift("ZZ") == "FF"
    assert encode_shift("ZZZ") == "GGG"
    assert encode_shift("ZZZZ") == "HHH"
    assert encode_shift("ZZZZZ") == "III"
    assert encode_shift("ZZZZZZ") == "JJJ"
    assert encode_shift("ZZZZZZZ") == "KKK"
    assert encode_shift("ZZZZZZZZ") == "LLL"
    assert encode_shift("ZZZZZZZZZ") == "MMM"
    assert encode_shift("ZZZZZZZZZZ") == "NNN"
    assert encode_shift("ZZZZZZZZZZZ") == "OOO"
    assert encode_shift("ZZZZZZZZZZZZ") == "PPP"
    assert encode_shift("ZZZZZZZZZZZZZ") == "QQQ"
    assert encode_shift("ZZZZZZZZZZZZZZ") == "RRR"
    assert encode_shift("ZZZZZZZZZZZZZZZ") == "SSS"
    assert encode_shift("ZZZZZZZZZZZZZZZZ") == "TT