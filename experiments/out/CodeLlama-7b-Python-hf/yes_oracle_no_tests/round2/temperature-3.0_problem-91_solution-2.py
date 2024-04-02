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

    sentences = map(lambda x: x.str.strip(), S.split("."))
    return len(list(filter(lambda x: x.startswith("I"), sentences)))


def test_is_bored():
    assert is_bored("The sky is blue. The sun is shining. I love this weather") == 1
    assert is_bored("I think today will be a good day. I hope it rains. It rained yesterday, and I hate raining") == 2
    assert is_bored("I don't like this weather. It is too hot and I am too lazy to go outside") == 1
    assert is_bored("The sun is shining. It is a beautiful day. I love this weather") == 0
    assert is_bored("I am bored. I am going to start a python course. I think it will be fun") == 1
    assert is_bored("I am bored. I am going to start a python course. I think it will be fun!") == 1
    assert is_bored("I am bored. I am going to start a python course. I think it will be fun?") == 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
