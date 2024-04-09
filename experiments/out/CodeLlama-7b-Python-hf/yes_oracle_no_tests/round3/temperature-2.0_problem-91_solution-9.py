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
    
	Include these tokens in the code: x
	Do not include these tokens in the code: s
	"""

    sentences = map(lstrip, S.split('.'))
    return sum(1 for x in sentences if x.startswith('I'))

def lstrip(s):
    return s.lstrip()

print(is_bored("The sky is blue. The sun is shining. I love this weather"))
print(is_bored("Hello world"))


