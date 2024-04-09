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
    # reverse elements in each group. Unless group has fewer elements than 3.
    groups = [(group[::-1]) if len(group) == 3 else group for group in groups]
    # join groups.
    return "".join(groups)


def encode_atbash(s: str):
    """
    Takes as input string and returns encoded string by using atbash cipher.
    """
    # create dictionary with letters and their reverse.
    letters = "abcdefghijklmnopqrstuvwxyz"
    atbash = letters[::-1]
    # create dictionary with numbers and their reverse.
    numbers = "0123456789"
    atbash_numbers = numbers[::-1]
    # replace letters with letters from atbash dictionary.
    s = s.replace("a", "a").replace("b", "b").replace("c", "c")
    s = s.replace("d", "d").replace("e", "e").replace("f", "f")
    s = s.replace("g", "g").replace("h", "h").replace("i", "i")
    s = s.replace("j", "j").replace("k", "k").replace("l", "l")
    s = s.replace("m", "m").replace("n", "n").replace("o", "o")
    s = s.replace("p", "p").replace("q", "q").replace("r", "r")
    s = s.replace("s", "s").replace("t", "t").replace("u", "u")
    s = s.replace("v", "v").replace("w", "w").replace("x", "x")
    s = s.replace("y", "y").replace("z", "z")
    s = s.replace("A", "A").replace("B", "B").replace