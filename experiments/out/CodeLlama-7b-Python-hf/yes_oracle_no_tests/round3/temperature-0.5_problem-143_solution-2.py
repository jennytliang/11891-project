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
    
	Do not include these tokens in the code: # # First , write a function
	"""
    # # First , write a function
    # def is_prime(number):
    #     for i in range(2, number):
    #         if number % i == 0:
    #             return False
    #     return True
    # def words_in_sentence(sentence):
    #     words = sentence.split(" ")
    #     words_length = []
    #     for word in words:
    #         if is_prime(len(word)):
    #             words_length.append(word)
    #     return " ".join(words_length)

    # # Then , write the main code
    # print(words_in_sentence("This is a test"))
    # print(words_in_sentence("lets go for swimming"))

    # # Finally , check if your code is passing the automated tests
    # # and if it is, check if it's optimal
    # # and if it is, check if it's correct

    words = sentence.split(" ")
    words_length = []
    for word in words:
        if is_prime(len(word)):
            words_length.append(word)
    return " ".join(words_length)


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
