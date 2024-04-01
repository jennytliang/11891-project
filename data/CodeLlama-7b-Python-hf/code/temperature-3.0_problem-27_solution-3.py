def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return string.swapcase()


def main():
    for i in range(5):
        s = flip_case('Hello World')
        print(s)


if __name__ == "__main__":
    main()