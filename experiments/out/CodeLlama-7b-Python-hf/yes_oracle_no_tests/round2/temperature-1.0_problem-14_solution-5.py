from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Include these tokens in the code: return [ string [ :( i +
	"""
    return [string[ : i ] for i in range(len(string) + 1 )]
def main():
    print(all_prefixes(''))
    print(all_prefixes('a'))
    print(all_prefixes('ab'))
    print(all_prefixes('abc'))
    print(all_prefixes('asdfghjklo'))

if __name__ == "__main__":
    main()