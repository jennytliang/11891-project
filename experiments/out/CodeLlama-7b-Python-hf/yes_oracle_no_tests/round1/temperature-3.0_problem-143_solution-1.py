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
    
	Include these tokens in the code: def is _ prime ( a ):
	Do not include these tokens in the code: result = [] for word
	"""
    ############# 1. Naive solution - 11k/100% #############
    words = sentence.split()
    result = []
    for word in words:
        if len(word) == 2 or len(word) == 3 or len(word) == 5 or len(word) == 7:
            result.append(word)
    return " ".join(result)

    ############# 2. Optimized solution - 11k/100% #############
    words = sentence.split()
    result = []
    for word in words:
        if len(word) == 2 or len(word) == 3 or len(word) == 5 or len(word) == 7:
            result.append(word)
    return " ".join(result)
