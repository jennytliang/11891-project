def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    
	Include these tokens in the code: (' \
	Do not include these tokens in the code: ( [" ", "\
	'''

    whitespace = 0
    comma = 0
    for i in txt:
        if i == " ":
            whitespace += 1
        if i == ",":
            comma += 1

    if whitespace == 0 and comma == 0:
        return (ord('z') - ord('a')) // 2 + 1

    if whitespace == 0:
        return txt.split(sep=',')

    return txt.split(sep=' ')


def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    
	Include these tokens in the code: (' \
	Do not include these tokens in the code: ( [" ", "\
	'''

    if txt.count(' ') == 0 and txt.count(',') == 0:
        return (ord('z') - ord('a')) // 2 + 1

    if txt.count(' ') == 0:
        return txt.split(',')

    return txt.split(' ')


