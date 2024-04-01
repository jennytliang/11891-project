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
    # # Answer 1:
    # # O(n) time | O(n) space
    # def is_prime(a):
    #     if a == 2 or a == 3:
    #         return True
    #     if a < 2 or a % 2 == 0 or a % 3 == 0:
    #         return False
    #     for i in range(5, int(a ** 0.5) + 1, 6):
    #         if a % i == 0 or a % (i + 2) == 0:
    #             return False
    #     return True

    # def words_in_sentence(sentence):
    #     words = sentence.split(" ")
    #     return " ".join([word for word in words if is_prime(len(word))])
    # return words_in_sentence(sentence)

    # # Answer 2:
    # # O(n) time | O(n) space
    # def words_in_sentence(sentence):
    #     words = sentence.split(" ")
    #     return " ".join([word for word in words if len(word) == len(list(filter(lambda x: len(word) % x == 0, range(2, len(word) + 1))))])
    # return words_in_sentence(sentence)

    # # Answer 3:
    # # O(n) time | O(n) space
    # def words_in_sentence(sentence):
    #     words = sentence.split(" ")
    #     return " ".join([word for word in words if len(word) == len(list(filter(lambda x: len(word) % x == 0, range(2, len(word) + 1))))])
    # return words_in_sentence(sentence)

    # # Answer 4:
    # # O(n) time | O(n) space
    # def words_in_sentence(sentence):
    #     words = sentence.split(" ")
    #     return " ".join([