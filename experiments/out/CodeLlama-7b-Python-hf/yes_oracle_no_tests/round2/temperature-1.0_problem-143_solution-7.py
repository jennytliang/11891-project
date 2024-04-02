def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    
	Include these tokens in the code: def is _ prime ( a ): return
	"""
    words=sentence.split()
    lst=[]
    for i in words:
        temp=len(i)
        temp=temp-1
        if temp > 1:
            if temp % 2 != 0:
                if temp % 3 != 0:
                    lst.append(i)
    return lst

words_in_sentence("This is a test")
words_in_sentence("lets go for swimming")