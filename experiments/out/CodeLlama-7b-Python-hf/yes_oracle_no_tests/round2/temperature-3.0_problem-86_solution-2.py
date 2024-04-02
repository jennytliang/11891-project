def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    
	Do not include these tokens in the code: # My code def sort
	"""
    return ' '.join(sorted(s.split(), key=lambda x: ''.join(sorted(x))))


def test_anti_shuffle():
    assert anti_shuffle('Hi') == 'Hi'
    assert anti_shuffle('hello') == 'ehllo'
    assert anti_shuffle('Hello World!!!') == 'Hello !!!Wdlor'
    assert anti_shuffle('12345') == '12345'
    assert anti_shuffle('a b c d e') == 'abcde'
    assert anti_shuffle('Hello World!') == 'Hello World!'
    assert anti_shuffle('') == ''
    assert anti_shuffle('      ') == '      '
    assert anti_shuffle('    Hello World!!!    ') == '    Hello !!!Wdlor    '
