from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Include these tokens in the code: return [ string [ :( i +
	"""

    prefixes = []
    for i in range(len(string)):
        prefixes.append(string[:i + 1])
    return prefixes


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes('abc')
    ['abc', 'bc', 'c']
    """

    suffixes = []
    for i in range(len(string)):
        suffixes.append(string[i:])
    return suffixes


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings('abc')
    ['a', 'ab', 'abc', 'b', 'bc', 'c']
    """

    substrings = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substrings.append(string[i:j])
    return substrings


def all_substrings_v2(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_v2('abc')
    ['a', 'ab', 'abc', 'b', 'bc', 'c']

    Use all_prefixes and all_suffixes to make this function even more simple.
    """

    prefixes = all_prefixes(string)
    suffixes = all_suffixes(string)
    return prefixes + suffixes


def main():
    import doctest
    doctest.testmod()
    string = input("Provide a string: ")
    print(all_substrings(string))
    print(all_substrings_v2(string))


if __name__ == "__main__":
    main()
