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
    ##############
    # Solution # 1
    ##############
    # from math import sqrt
    # def is_prime(n):
    #     for i in range(2, int(sqrt(n)) + 1):
    #         if n % i == 0:
    #             return False
    #     return True

    # def words_in_sentence(sentence):
    #     words = sentence.split()
    #     return ' '.join([word for word in words if is_prime(len(word))])

    ##############
    # Solution # 2
    ##############
    # from math import sqrt
    # def is_prime(n):
    #     for i in range(2, int(sqrt(n)) + 1):
    #         if n % i == 0:
    #             return False
    #     return True

    # def words_in_sentence(sentence):
    #     words = sentence.split()
    #     return ' '.join([word for word in words if is_prime(len(word))])

    ##############
    # Solution # 3
    ##############
    # from math import sqrt
    # def is_prime(n):
    #     for i in range(2, int(sqrt(n)) + 1):
    #         if n % i == 0:
    #             return False
    #     return True

    # def words_in_sentence(sentence):
    #     words = sentence.split()
    #     return ' '.join([word for word in words if is_prime(len(word))])

    ##############
    # Solution # 4
    ##############
    # from math import sqrt
    # def is_prime(n):
    #     for i in range(2, int(sqrt(n)) + 1):
    #         if n % i == 0:
    #             return False
    #     return True

    # def words_in_sentence(sentence):
    #     words = sentence.