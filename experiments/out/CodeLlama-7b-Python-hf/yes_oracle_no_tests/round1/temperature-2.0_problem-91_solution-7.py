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
    
	Include these tokens in the code: sentences = map ( lambda x : x . strip
	"""
    sentences = map(lambda x: x.strip(), S.split('.'))
    bored_count = 0

    for sentence in sentences:
        if sentence.startswith('I'):
            bored_count += 1

    return bored_count


def is_bored_two(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    
	Include these tokens in the code: sentences = map ( lambda x : x . strip
	"""
    sentences = map(lambda x: x.strip(), S.split('.'))
    bored_count = 0

    for sentence in sentences:
        if sentence.startswith('I'):
            bored_count += 1

    return bored_count


def is_bored_three(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    
	Include these tokens in the code: sentences = map ( lambda x : x . strip
	"""
    sentences = map(lambda x: x.strip(), S.split('.'))
    bored_count = 0

    for sentence in sentences:
        if sentence.startswith('I'):
            bored_count += 1

    return bored_count


def is_bored_four(S):
    """