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
    returns encoded string by rotating every character by 13 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 13 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_rot13(s: str):
    """
    takes as input string encoded with encode_rot13 function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""

    return "".join([chr(((ord(ch) - 13 - ord("a")) % 26) + ord("a")) for ch in s])


def encode_substitution(s: str):
    """
    returns encoded string by replacing every character by a different character
    according to the following dictionary:
    {A: B, B: D, C: E, D: A, E: C, F: G, G: H, H: F, I: J, J: I, K: L, L: K, M: N, N: M, O: P, P: O, Q: R, R: Q, S: T, T: S, U: V, V: U, W: X, X: W, Y: Z, Z: Y}
    """

    return "".join(
        [
            chr(
                (
                    ord("B")
                    if ord(ch) == ord("A")
                    else (ord("D") if ord(ch) == ord("B") else (ord("E") if ord(ch) == ord("C") else (ord("A") if ord(ch) == ord("D") else (ord("C") if ord(ch) == ord("E") else (ord("G") if ord(ch) == ord("F") else (ord("H") if ord(ch) == ord("G") else (ord("F") if ord(ch) == ord("H")