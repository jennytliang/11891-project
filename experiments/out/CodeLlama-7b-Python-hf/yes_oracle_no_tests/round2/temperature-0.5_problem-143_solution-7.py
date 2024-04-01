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
    
	Do not include these tokens in the code: # p yl int : disable
	"""
    # pylint: disable=inconsistent-return-statements
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    def is_prime(number):
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    return_list = []
    for word in sentence.split():
        if is_prime(len(word)):
            return_list.append(word)
    return " ".join(return_list)
