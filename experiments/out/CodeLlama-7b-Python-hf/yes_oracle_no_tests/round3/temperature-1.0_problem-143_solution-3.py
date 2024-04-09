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
    
	Do not include these tokens in the code: ### ################ ## # #
	"""
    ##############
    # Solution 1 #
    ##############
    # O(n) time | O(n) space

    # def words_in_sentence(sentence):
    #     words = sentence.split()
    #     prime_words = []
    #     for word in words:
    #         if is_prime_word(word):
    #             prime_words.append(word)
    #     return " ".join(prime_words)

    # def is_prime_word(word):
    #     if len(word) == 1:
    #         return True

    #     for i in range(2, len(word)):
    #         if len(word) % i == 0:
    #             return False

    #     return True

    ##############
    # Solution 2 #
    ##############
    # O(n) time | O(n) space

    # def words_in_sentence(sentence):
    #     words = sentence.split()
    #     prime_words = []
    #     for word in words:
    #         if is_prime(len(word)):
    #             prime_words.append(word)
    #     return " ".join(prime_words)

    # def is_prime(n):
    #     for i in range(2, n):
    #         if n % i == 0:
    #             return False

    #     return True

    ##############
    # Solution 3 #
    ##############
    # O(n) time | O(n) space

    def words_in_sentence(sentence):
        words = sentence.split()
        prime_words = []
        for word in words:
            if is_prime(len(word)):
                prime_words.append(word)
        return " ".join(prime_words)

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
               