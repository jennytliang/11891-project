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
    
	Include these tokens in the code: ( lambda
	"""

    sentences  = S.split(".") + S.split("?") + S.split("!")
    return sum(1 for s in sentences if s.strip().startswith("I"))

assert is_bored("The sky is blue. The sun is shining. I love this weather") == 1
assert is_bored("I love this weather. The sun is shining. I love this weather") == 2
assert is_bored("The sky is blue. The sun is shining. The moon is shining") == 0