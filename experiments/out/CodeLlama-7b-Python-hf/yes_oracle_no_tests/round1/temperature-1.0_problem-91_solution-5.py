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
    import re
    sentences = re.split('[.?!]', S)
    return len([s for s in sentences if s.startswith('I')])


def is_bored1(S):
    return sum(s.startswith('I') for s in re.split('[.?!]', S))


def is_bored2(S):
    return len(re.findall(r'^I\b', S, flags=re.MULTILINE))


def is_bored3(S):
    return len(re.findall(r'^I\S*', S, flags=re.MULTILINE))


if __name__ == '__main__':
    import doctest
    doctest.testmod()