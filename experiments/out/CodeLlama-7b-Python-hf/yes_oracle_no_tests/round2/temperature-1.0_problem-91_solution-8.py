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
    # your code here
    sentences_list = S.split('.')
    sentences_list2 = S.split('?')
    sentences_list3 = S.split('!')
    sentences_list4 = S.split(';')

    for k in range(len(sentences_list)+len(sentences_list2)+len(sentences_list3)+len(sentences_list4)-4):
        if k == 0:
            for m in ["I", "i"]:
                if sentences_list[k][0] == m or sentences_list2[k][0] == m or sentences_list3[k][0] == m or sentences_list4[k][0] == m:
                    return 1
            return 0
        for n in ["I", "i"]:
            if sentences_list[k][0] == n or sentences_list2[k][0] == n or sentences_list3[k][0] == n or sentences_list4[k][0] == n:
                return 1
        for l in ["I", "i"]:
            if sentences_list[k+1][0] == l or sentences_list2[k+1][0] == l or sentences_list3[k+1][0] == l or sentences_list4[k+1][0] == l:
                return 0

    return 0
