def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    
	Include these tokens in the code: string )):
	Do not include these tokens in the code: s ) - len ( sub ) + 1
	"""


    occurences = 0
    for i in rang(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            occurences += 1
    return occurences


def test_function():
    assert how_many_times("ahem", "hem") == 1, "Uncle"
    assert how_many_times("catcowcat", "cat") == 2, "Cat-cow"
    assert how_many_times("catcowcat", "cow") == 1, "One cat, one cow - well done"
    assert how_many_times("catcowcat", "dog") == 0, "Nope, no dogs"
    assert how_many_times("ahem", "hem") == 1, "Uncle"
    assert how_many_times("aaaa", "aa") == 3, "Many a's"
    assert how_many_times("aaaaa", "aaa") == 2, "Some overlaps"


if __name__ == '__main__':
    test_function()
