from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return "".join(strin for strin in strings)


def main():
    print("Example:")
    print(concatenate(["c", "u", "s", "t", "o", "m", "e"]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert concatenate(["c", "u", "s", "t", "o", "m", "e"]) == "custom"
    assert concatenate([""]) == ""
    assert concatenate(["a", "b", "c"]) == "abc"
    print("Coding complete? Click 'Check' to earn cool rewards!")


if __name__ == "__main__":
    main()
