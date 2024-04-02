from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    nest_count = []

    paren_string = "(" + paren_string

    for i in range(len(paren_string)):

        if paren_string[i] == "(":
            nest_count.append(0)
        elif paren_string[i] == ")":
            pop = nest_count.pop()
            nest_count.append(pop + 1)

    return nest_count


def validate(number: int):
    first = number % 10
    second = number // 10

    if first == second:
        return True
    else:
        return False


def validate_numbers(numbers):
    total = 0

    for x in numbers:
        if validate(x):
            total += x
        else:
            print("No it is not valid")
            return 0

    return total


if __name__ == "__main__":
    print(parse_nested_parens("(()()) ((())) () ((())()())"))
    pass
    # numbers = [553, 262, 1, 390]
    # print(validate_numbers(numbers))
