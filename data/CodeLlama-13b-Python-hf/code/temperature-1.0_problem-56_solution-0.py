def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    count = 0
    for b in brackets:
        if b == "<":
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    return count == 0


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('<>') == True
    assert candidate('<><>') == True
    assert candidate('<<><>>') == True
    assert candidate('><<>') == False
    assert candidate('<') == False

if __name__ == '__main__':
    check(correct_bracketing)
