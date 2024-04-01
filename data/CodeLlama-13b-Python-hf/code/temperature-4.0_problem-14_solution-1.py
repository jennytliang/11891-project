from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[: i + 1] for i in range(len(string))]


def main():
    string = str(input("Enter a number : "))
    print(f"Length of all prefix of the given number are :")
    print("\n".join(map(str, all_prefixes(string=string))))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
