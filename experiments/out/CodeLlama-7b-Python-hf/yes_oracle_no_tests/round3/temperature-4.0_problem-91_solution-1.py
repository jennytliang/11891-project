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
    
	Include these tokens in the code: (( S
	"""

    sentences = map(lambda x: x.str.strip(), S.split('.'))
    return sum(map(lambda x: x.startswith('I'), sentences))


S = "The sky is blue. The sun is shining. I love this weather"
assert is_bored(S) == 1

S = "I love this weather"
assert is_bored(S) == 1

S = "The sky is blue. The sun is shining"
assert is_bored(S) == 0

S = "The sky is blue. The sun is shining."
assert is_bored(S) == 0

S = "The sky is blue. The sun is shining! I love this weather"
assert is_bored(S) == 1

S = "The sky is blue. The sun is shining? I love this weather"
assert is_bored(S) == 1

S = "The sky is blue. The sun is shining. I love this weather! The sunset is beautiful"
assert is_bored(S) == 2
