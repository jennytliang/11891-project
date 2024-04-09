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
    
	Include these tokens in the code: (" ")
	Do not include these tokens in the code: ()
	"""

    words = s.split(' ')
    result = []
    for word in words:
        if word != '':
            result.append(sorted(list(word)))
        else:
            result.append('')
    return ' '.join(result)


def anti_shuffle_2(s):
    return ' '.join(sorted(s.split(' '), key=sorted))


if __name__ == '__main__':
    print(anti_shuffle('Hello World!!!'))
    print(anti_shuffle('Hi'))
    print(anti_shuffle('hello'))
    print(anti_shuffle(''))
    print(anti_shuffle('a'))
    print(anti_shuffle('ab'))
    print(anti_shuffle('abc'))
    print(anti_shuffle('abcd'))
    print(anti_shuffle('abcde'))
    print(anti_shuffle('abcdef'))
    print(anti_shuffle('abcdefg'))

    print(anti_shuffle_2('Hello World!!!'))
    print(anti_shuffle_2('Hi'))
    print(anti_shuffle_2('hello'))
    print(anti_shuffle_2(''))
    print(anti_shuffle_2('a'))
    print(anti_shuffle_2('ab'))
    print(anti_shuffle_2('abc'))
    print(anti_shuffle_2('abcd'))
    print(anti_shuffle_2('abcde'))
    print(anti_shuffle_2('abcdef'))
    print(anti_shuffle_2('abcdefg'))
