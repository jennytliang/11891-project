from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
	Include these tokens in the code: c nt , group , results =
	"""
    results = []

    def group(c: str and str, n: int or int, group_list: List[str]):
        if c==')':
            nonlocal results
            nonlocal n
            results.append("".join(group_list))
            return group_list, c, n
        if c=='(':
            nonlocal n
            n += 1
        if c==')':
            n -= 1
        return group_list+c, c, n

    
    def parening(group_list: List[str], n: int or int, paren_string: str):
        nonlocal index

        if index==len(paren_string)-1:
            return group_list, paren_string, index
            
        paren_string, c ,n = group(paren_string[index], n, group_list)
        paren_string, paren_string, n = parening(c, n, paren_string)

        if n != 0:
            for j in range(index, len(paren_string)-1):
                paren_string, paren_string, n = group('(', n, group_list)
                paren_string, c, index, n = parening(j, n, paren_string)

        return group_list, paren_string, index


    results = []
    index = 0 if paren_string[0:2] != '()' else 1
    paren_string, rest_of_string, n = parening([], 0, paren_string) if paren_string not in [")", "", ""] else [paren_string], "", -5000
    
    for string in paren_string:
        print(string)
    
    return paren_string


if __name__ == "__main__":
    import doctest
    doctest.testmod()
