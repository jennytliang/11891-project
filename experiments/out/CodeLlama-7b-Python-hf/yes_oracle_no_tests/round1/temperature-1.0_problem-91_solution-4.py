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
    # Split sentence:
    sentences = map(lambda x: x.strip(), S.split("."))

    # Count boredness:
    bored = sum(1 for e in sentences if e[0] == 'I')

    return bored


def is_bored_regex(S):
    import re
    # Write a regular expression:
    regexp = r"(I|i)"
    
    # Count boredom. Use a lambda function if necessary
    bored = len([m for m in re.finditer(regexp, S)])

    return bored

def is_bored_string(S):
	bored = 0
	while '.' in S:
		p = S.index('.')
		text = S[:p]
		if text[0:2] == 'I ' or text[0:2] == 'I.':
			bored += 1
		S = S[p+1:]
	return bored