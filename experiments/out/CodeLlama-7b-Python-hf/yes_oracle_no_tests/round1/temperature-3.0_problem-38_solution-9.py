def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    
	Do not include these tokens in the code: # split string to groups . Each
	"""
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def encode_run_length(s: str):
    """
    returns encoded string by run length encoding.
    """
    if s == "":
        return ""
    return "".join(f"{len(c)}{c[0]}" for c in s)


def decode_run_length(s: str):
    """
    takes as input string encoded with encode_run_length function. Returns decoded string.
    """
    if s == "":
        return ""
    return "".join(c * int(c) for c in s)


def encode_morse(s: str):
    """
    returns encoded string by morse code.
    """
    return " ".join(MORSE_CODE.get(c, c) for c in s.upper())


def decode_morse(s: str):
    """
    takes as input string encoded with encode_morse function. Returns decoded string.
    """
    return "".join(MORSE_CODE_DECODE.get(c, c) for c in s.split())


def encode_atbash(s: str):
    """
    returns encoded string by Atbash cipher.
    """
    return "".join(ATBASH_CODE.get(c, c) for c in s)


def decode_atbash(s: str):
    """
    takes as input string encoded with encode_atbash function. Returns decoded string.
    """
    return "".join(ATBASH_CODE_DECODE.get(c, c) for c in s)


def encode_railfence(s: str,