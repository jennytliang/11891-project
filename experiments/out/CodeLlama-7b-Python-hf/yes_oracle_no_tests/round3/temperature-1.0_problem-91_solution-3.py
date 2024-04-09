def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    
	Include these tokens in the code: sentences
	Do not include these tokens in the code: sent en cel ist
	"""
    c = S.count("I")
    for i in range(c):
        if S.find("I", i) == i:
            if (S.find(".", i) == i + 1 or S.find("?", i) == i + 1 or S.find("!", i) == i + 1):
                c -= 1
    return c

def is_bored_2(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    
	Include these tokens in the code: sentences
	Do not include these tokens in the code: sent en cel ist
	"""
    c = 0
    for i in S.split(' '):
        if i.startswith('I'):
            if (S.find(".", S.find(i)) == S.find(i) + len(i) or S.find("?", S.find(i)) == S.find(i) + len(i) or S.find("!", S.find(i)) == S.find(i) + len(i)):
                c += 1
    return c



if __name__ == '__main__':
    import doctest
    doctest.testmod()
