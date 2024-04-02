from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    
	Include these tokens in the code: max len =
	Do not include these tokens in the code: return
	"""

    if not strings:
        return None
    
    max_len = [0,0]
    for i, s in enumerate(strings):
        if len(s) > max_len[0]:
            max_len = [len(s), i]
            
    max_string_idx = max_len[1]
    return strings[max_string_idx]

    

def test_longest():
    assert longest([] ) == None
    assert longest(["a"] ) == 'a'
    assert longest(["a", "d"] ) == 'a'
    assert longest(["a", "dd"] ) == 'a'
    assert longest(['a', 'b', 'c']) == 'a'
    assert longest(['b', 'b', 'c']) == 'b'
    assert longest(['b', 'aaaaa', 'c']) == 'aaaaa'
    assert longest(['c', 'aaaaa', 'a']) == 'aaaaa'
    assert longest(['c', 'd', 'aaaaa', 'a']) == 'aaaaa'