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
    
	Do not include these tokens in the code: # My and best way solution
	"""
    return ' '.join(word for word in sentence.split() if len(word) == 2 or len(set(word)) == len(word) and all(
        (lambda x: x > 1 and not x & (x - 1))(len(word))))
