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
    #################
    # Simple solution
    #################
    # from math import sqrt

    # def is_prime(a):
    #     if a == 1:
    #         return False
    #     for i in range(2, int(sqrt(a)) + 1):
    #         if a % i == 0:
    #             return False
    #     return True

    # def words_in_sentence(sentence):
    #     words = sentence.split()
    #     prime_words = []
    #     for word in words:
    #         if is_prime(len(word)):
    #             prime_words.append(word)
    #     return " ".join(prime_words)

    # return words_in_sentence(sentence)

    #################
    # Optimized solution
    #################
    from math import sqrt

    def is_prime(a):
        if a == 1:
            return False
        for i in range(2, int(sqrt(a)) + 1):
            if a % i == 0:
                return False
        return True

    def words_in_sentence(sentence):
        words = sentence.split()
        prime_words = []
        for word in words:
            if is_prime(len(word)):
                prime_words.append(word)
        return " ".join(prime_words)

    return words_in_sentence(sentence)
