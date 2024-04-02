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
    # # This is my first solution, using a list comprehension and the is_prime function.
    # # This solution takes O(n) time and O(n) space.
    #
    # # Check if the given word is a prime number.
    # def is_prime(word):
    #     n = len(word)
    #     if n == 2 or n == 3:
    #         return True
    #     if n < 2 or n % 2 == 0 or n % 3 == 0:
    #         return False
    #     i = 5
    #     while i * i <= n:
    #         if n % i == 0 or n % (i + 2) == 0:
    #             return False
    #         i += 6
    #     return True
    #
    # # Find the words in the sentence that are prime numbers.
    # def words_in_sentence(sentence):
    #     return [word for word in sentence.split() if is_prime(word)]

    # # This is my second solution, using a list comprehension and the is_prime function.
    # # This solution takes O(n) time and O(n) space.
    #
    # # Check if the given word is a prime number.
    # def is_prime(word):
    #     n = len(word)
    #     if n == 2 or n == 3:
    #         return True
    #     if n < 2 or n % 2 == 0 or n % 3 == 0:
    #         return False
    #     i = 5
    #     while i * i <= n:
    #         if n % i == 0 or n % (i + 2) == 0:
    #             return False
    #         i += 6
    #     return True
    #
    # # Find the words in the sentence that are prime numbers.
    # def words_in_sentence(sentence):
    #     return [word for word in sentence.split() if is_prime(word)]

    # This is