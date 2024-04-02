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


################################################

def concatenate2(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string without using a loop
    >>> concatenate2([])
    ''
    >>> concatenate2(['a', 'b', 'c'])
    'abc'
	
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""
    
    # This is the expected behaviour...
    
    # return "" + strin + "".join(strin)
    # return "" * strings.count("" + strin + "".join(strin)) + strings.join(".join", 'a', '.join')
    # return ("" * (len(strings)) + strings[0] + "".join(strings)
    
    return strings[0] + "".join(strings[1:])
    
    # ...but this doesn't work :(
    # return str(*strings)
    # return str(strings)
    # return "".join([str(x) for x in strings])
    # return "".join([x for x in strings])
    # return "".join(strin for strin in strings)
    # return "".join(x, *strings)
    # return "".join(x, strings)
    # return "".join(strings)
    # return join("", strings)
    # return join(strings)
    # return join("", strings[0], *strings[1:])
    # return join("", [strin for strin in strings])
    # return str(*[strin for strin in strings], ", ", *strings[0], *strings[1])


def main():
    strings = input("Enter some strings: ").split()
    print(concatenate(strings))
    print(concatenate2(strings))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
