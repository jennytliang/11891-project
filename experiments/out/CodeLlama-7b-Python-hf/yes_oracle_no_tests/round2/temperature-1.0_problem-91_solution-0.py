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
    
	Include these tokens in the code: sentences = map ( lambda x
	Do not include these tokens in the code: ST UD ENT NOT ES
	"""

    s = S.split(" ")
    # s = S.split(" ")
    count = 0
    for i,s in enumerate(s):
        for j,v in enumerate(s):
            if v == ".":
                tmp = s[i:j+1]
                if s[0]== "I":
                    count += 1
                tmp.pop(0)
                break
            else:
                tmp = [" "]

    return count

if __name__ == "__main__":

    import doctest, sys
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS; MY_CODE_IS_CORRECT ***\n"
    else:
        sys.exit(1)