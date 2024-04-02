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
    
	Include these tokens in the code: map ( lambda x : x
	Do not include these tokens in the code: S
	"""

    sentencelist = S.split('.')
    sentencelist = sentencelist + S.split('?')
    sentencelist = sentencelist + S.split('!')
    boredcount = 0
    for sentence in sentencelist:
        if sentence.strip().startswith('I'):
            boredcount = boredcount + 1
    return boredcount


def is_bored2(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored2("Hello world")
    0
    >>> is_bored2("The sky is blue. The sun is shining. I love this weather")
    1
    
	Include these tokens in the code: map ( lambda x : x
	Do not include these tokens in the code: S
	"""
    return sum(map(lambda x: x.startswith('I'), S.split('.')))


def is_bored3(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored3("Hello world")
    0
    >>> is_bored3("The sky is blue. The sun is shining. I love this weather")
    1
    
	Include these tokens in the code: map ( lambda x : x
	Do not include these tokens in the code: S
	"""
    return len(filter(lambda x: x.startswith('I'), S.split('.')))


def is_bored4(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a