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
    
	Include these tokens in the code: ((
	"""

    sentences = map(lambda x: x.str.strip(), S.split('.'))
    sentences = filter(lambda x: x != '', sentences)
    sentences = map(lambda x: x.split(' '), sentences)
    sentences = filter(lambda x: x[0] == 'I', sentences)
    return len(list(sentences))


def is_bored_2(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!''.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """

    sentences = S.split('\.|\?|!')
    sentences = filter(lambda x: x != '', sentences)
    sentences = map(lambda x: x.split(' '), sentences)
    sentences = filter(lambda x: x[0] == 'I', sentences)
    return len(list(sentences))
