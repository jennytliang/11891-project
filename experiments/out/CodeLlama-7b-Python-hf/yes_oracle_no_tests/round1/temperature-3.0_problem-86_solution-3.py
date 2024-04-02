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
    
	Do not include these tokens in the code: if not s : return
	"""
    return ' '.join([sorted(word, key=lambda x: ord(x)) for word in s.split()])
    
    
def test_anti_shuffle():
    assert anti_shuffle('Hi') == 'Hi'
    assert anti_shuffle('hello') == 'ehllo'
    assert anti_shuffle('Hello World!!!') == 'Hello !!!Wdlor'
    assert anti_shuffle('aabbc') == 'ababc'
    assert anti_shuffle('aabbcddd') == 'ababcddd'
    assert anti_shuffle('aabbcc') == 'abcabc'
    assert anti_shuffle('aabbccd') == 'abcabcd'
    assert anti_shuffle('') == ''


if __name__ == '__main__':
    test_anti_shuffle()
