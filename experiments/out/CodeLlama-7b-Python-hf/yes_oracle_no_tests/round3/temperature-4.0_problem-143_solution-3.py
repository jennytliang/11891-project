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
    #############
    # Solution 1 #
    #############
    # import math
    # def is_prime(n):
    #     if n <= 1:
    #         return False
    #     for i in range(2, int(math.sqrt(n)) + 1):
    #         if n % i == 0:
    #             return False
    #     return True

    #############
    # Solution 2 #
    #############
    import math

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    words = sentence.split(' ')
    return ' '.join([word for word in words if is_prime(len(word))])


    # # or
    # return ' '.join(filter(lambda word: is_prime(len(word)), sentence.split(' ')))


    # #############
    # # Solution 3 #
    # #############
    # import math
    # def is_prime(n):
    #     if n <= 1:
    #         return False
    #     for i in range(2, int(math.sqrt(n)) + 1):
    #         if n % i == 0:
    #             return False
    #     return True

    # words = sentence.split(' ')
    # return ' '.join([word for word in words if is_prime(len(word))])

    # # or
    # return ' '.join(filter(lambda word: is_prime(len(word)), sentence.split(' ')))


    # #############
    # # Solution 4 #
    # #############
    # import math
    # def is_prime(n):
    #     if n <= 1:
    #         return False
    #     for i in range(2, int(math.sqrt(n)) + 1):
    #         if n % i == 0:
   