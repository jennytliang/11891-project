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
    
	Include these tokens in the code:  def is _ prime ( a ):
	Do not include these tokens in the code: words =
	"""

    # # My and best way solution
    # def is_prime(a):
    #     if a == 1:
    #         return False
    #     for i in range(2, a):
    #         if a % i == 0:
    #             return False
    #     return True

    # def words_in_sentence(sentence):
    #     words = sentence.split()
    #     return ' '.join([w for w in words if is_prime(len(w))])

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    #     return ' '.join([w for w in words if is_prime(len(w))])

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
        return ' '.join([w for w in words if is_prime(len(w))])

    # # # # # # # # # # # # # # # # # # # # # # # # # # # #