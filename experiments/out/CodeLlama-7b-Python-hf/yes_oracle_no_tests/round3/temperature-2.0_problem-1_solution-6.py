from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
	Include these tokens in the code: c nt , group , results
	Do not include these tokens in the code: n t
	"""
    # TODO: Write your code below this line.
    c = 0
    n = 0
    group = ''
    results = []
    for i in paren_string:
        if i == '(':
            c += 1
            group += i
        elif i == ')':
            n += 1
            group += i
            if c == n:
                results.append(group)
                group = ''
                c = 0
                n = 0
        else:
            group += i
    return results


if __name__ == '__main__':
    with open('./data/07-03-01.in') as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        for line in content:
            print(separate_paren_groups(line))
