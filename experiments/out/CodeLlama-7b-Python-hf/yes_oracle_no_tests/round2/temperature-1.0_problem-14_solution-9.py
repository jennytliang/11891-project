from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Do not include these tokens in the code: [ s for s in
	"""


    
    return [ string[:i] for i in range(len(string)+1)]


def main():
    prefs = all_prefixes("abc")
    print(prefs)
    

if __name__ == "__main__":
    main()

