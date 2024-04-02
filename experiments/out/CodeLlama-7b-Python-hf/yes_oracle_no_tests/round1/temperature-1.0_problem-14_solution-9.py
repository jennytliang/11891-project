from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return [s for s in [string[i:] for i in range(len(string), -1, -1)]]
    ## Alternative solution
    #     return [string[:i] for i in range(len_string + 1)]


if __name__ == "__main__":
    input_string = input("Input a string: ")
    if not isinstance(input_string, (int, float)):
        print("Yes, the shortest prefix is " + all_prefixes(input_string)[0])
    print(all_prefixes(input_string))
