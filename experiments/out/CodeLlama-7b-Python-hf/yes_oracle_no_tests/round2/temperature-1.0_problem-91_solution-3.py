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
    
	Include these tokens in the code: sentences = map
	Do not include these tokens in the code: if len
	"""

    print(chr(27) + "[2J")
    list_ = ['<']
    words = S.split()
    if words[0] not in list_:
        k = words[:]
        del k[:2]
        n = k[:]
        a = ' '
        while a in n:
            n.pop(n.index(a))
        if words[0] and words[0] == 'I':
            print(','.join(n))
            return 1
    return 0

