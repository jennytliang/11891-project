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
    
	Include these tokens in the code: words = s . split (" ")
	"""
    words = s.split(' ')
    ordered_words = []
    for w in words:
        if w:
            chars = []
            for c in w:
                chars.append(c)
            chars.sort()
            ordered_words.append(''.join(chars))
        else:
            ordered_words.append(w)
    return ' '.join(ordered_words)


def test_anti_shuffle():
    assert 'Hi' == anti_shuffle('Hi')
    assert 'ehllo' == anti_shuffle('hello')
    assert 'Hello !!!Wdlor' == anti_shuffle('Hello World!!!')
    assert 'ehllo olihW' == anti_shuffle('hello world')
    assert 'Hello !!!Wdlor' == anti_shuffle('Hello World!!!')


def main():
    print("anti_shuffle('Hello World') → 'Hello !!!Wdlor'")
    print('anti_shuffle("hello") → "ehllo"')
    print()
    print("anti_shuffle('Hello World') →", anti_shuffle('Hello World'))
    print('anti_shuffle("hello") → "ehllo"')


if __name__ == '__main__':
    main()
