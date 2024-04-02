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
	Do not include these tokens in the code: words = S . split ();
	"""
    tokens = S.split()
    words = []
    for i in range(len(tokens)):
        if tokens[i] in ['.', '?', '!']:
            if 'I' in words:
                return 1
            words = []
        else:
            words.append(tokens[i])
    return 0

print(is_bored("The sky is blue. The sun is shining. I love this weather"))