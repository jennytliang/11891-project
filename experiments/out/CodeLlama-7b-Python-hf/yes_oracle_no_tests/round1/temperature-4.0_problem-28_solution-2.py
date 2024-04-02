from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Do not include these tokens in the code: if strings == [] :
	"""
    if len(strings) == 0:
        return ''
    else:
        return strings[0] + concatenate(strings[1:])


def main():
    print(concatenate(['a', 'b', 'c']))


if __name__ == "__main__":
    main()
