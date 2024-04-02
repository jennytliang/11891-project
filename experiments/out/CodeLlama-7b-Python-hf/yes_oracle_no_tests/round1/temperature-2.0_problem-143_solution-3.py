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
    from math import sqrt

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    words = sentence.split()
    return ' '.join(word for word in words if is_prime(len(word)))

    #############
    # Solution 2 #
    #############
    from math import sqrt

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    words = sentence.split()
    return ' '.join(word for word in words if is_prime(len(word)))

    #############
    # Solution 3 #
    #############
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    words = sentence.split()
    return ' '.join(word for word in words if is_prime(len(word)))

    #############
    # Solution 4 #
    #############
    words = sentence.split()
    return ' '.join(word for word in words if len(word) in [2, 3, 5, 7, 11, 13, 17, 19, 23, 2