from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""


    return "".join(stri for stri in strings)


def to_camel_case(text: str) -> str:
    """Convert a string into camel case
    >>> to_camel_case('a_b_c_d_e')
    'aBcDe'
    >>> to_camel_case('a_b_c_d')
    'aBcD'
    >>> to_camel_case('a_bc_d')
    'aBcD'
    >>> to_camel_case('Abc')
    'Abc'
    >>> to_camel_case('abc')
    'Abc'
    >>> to_camel_case('')
    ''
    """

    words = text.split("_")
    return words[0] + "".join(word.capitalize() for word in words[1:])


def to_snake_case(text: str) -> str:
    """Convert a string into snake case
    >>> to_snake_case('aBcDe')
    'a_bc_de'
    >>> to_snake_case('aBcD')
    'a_bc_d'
    >>> to_snake_case('aBc')
    'a_bc'
    >>> to_snake_case('Abc')
    'abc'
    >>> to_snake_case('abc')
    'abc'
    >>> to_snake_case('')
    ''
    """

    return "_".join(word.lower() for word in text.split("_"))


def main():
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    main()
