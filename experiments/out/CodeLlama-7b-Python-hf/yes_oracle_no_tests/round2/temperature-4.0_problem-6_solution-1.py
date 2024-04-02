from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    def count_depth(s: str) -> int:
        depth = 0
        for c in s:
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
        return depth

    return [count_depth(s) for s in paren_string.split()]


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print('usage: [--script] (--quiet | --verbose) file ...')
        sys.exit(1)

    # Notice the verbose and quiet flags here? They're there as a starting
    # point, but feel free to experiment with other flag options, too.
    verbose = False
    if args[0] == '--verbose':
        verbose = True
        args = args[1:]  # shift args off list by one
    if args[0] == '--quiet':
        args = args[1:]  # shift args off list by one

    # Notice that this also relies on the file to have a .txt suffix in it.
    for file in args:
        if not file.endswith('.txt'):
            print('ignoring %s, which does not have a .txt suffix' % file)
            continue

        with open(file) as f:
            lines = f.readlines()

        for line in lines:
            print(parse_nested_parens(line))


if __name__ == '__main__':
    import sys
    main()