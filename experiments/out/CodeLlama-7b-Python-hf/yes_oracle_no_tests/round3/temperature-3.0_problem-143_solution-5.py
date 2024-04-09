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
    #####################
    # PSEUDOCODE
    # 1. Create a list of words in the sentence
    # 2. Create a list of prime numbers
    # 3. Create a list of words in the sentence whose lengths are prime numbers
    # 4. Return a string of the words in the sentence whose lengths are prime numbers
    #####################

    # 1. Create a list of words in the sentence
    words = sentence.split()

    # 2. Create a list of prime numbers
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    # 3. Create a list of words in the sentence whose lengths are prime numbers
    words_list = []
    for word in words:
        if len(word) in prime_numbers:
            words_list.append(word)

    # 4. Return a string of the words in the sentence whose lengths are prime numbers
    return ' '.join(words_list)


    # def is_prime(a):
    #     if a <= 1:
    #         return False
    #     for x in range(2, a):
    #         if a % x == 0:
    #             return False
    #     return True


    # def words_in_sentence(sentence):
    #     words = sentence.split()
    #     prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 