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
    
	Include these tokens in the code: lambda x : x
	Do not include these tokens in the code: str
	"""

    sentences = S.split('.')
    sentences = [s.strip() for s in sentences]
    sentences = [s for s in sentences if s != '']
    return sum(1 for s in sentences if s.startswith('I'))

    # return sum(s.startswith('I') for s in S.split('.') if s.strip() != '')
    # return sum(s.startswith('I') for s in S.split('.') if s.strip())
    # return sum(s.startswith('I') for s in S.split('.'))
    # return sum([s.startswith('I') for s in S.split('.') if s.strip()])
    # return sum([s.startswith('I') for s in S.split('.')])
    # return sum(1 for s in S.split('.') if s.strip().startswith('I'))