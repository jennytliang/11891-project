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
    
	Do not include these tokens in the code: # Your code goes here
	"""
    # Your code goes here
    word_list = s.split(' ')
    result = []
    for word in word_list:
        if word != '':
            sorted_word = ''.join(sorted(word))
            result.append(sorted_word)
        else:
            result.append('')
    return ' '.join(result)


def test_anti_shuffle():
    assert anti_shuffle('Hi') == 'Hi'
    assert anti_shuffle('hello') == 'ehllo'
    assert anti_shuffle('Hello World!!!') == 'Hello !!!Wdlor'
    assert anti_shuffle('A ttack') == 'A  ttack'
    assert anti_shuffle('Afternoon') == 'Ae  fftnnor'
    assert anti_shuffle('Afternoon  ') == 'Ae  fftnnor  '
    assert anti_shuffle('a') == 'a'
    assert anti_shuffle('') == ''
    assert anti_shuffle(' ') == ' '
    assert anti_shuffle('Hi  my name is') == 'Hi  ym eisman'
