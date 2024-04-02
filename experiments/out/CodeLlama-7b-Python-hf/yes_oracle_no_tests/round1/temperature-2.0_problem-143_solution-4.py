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
    # # This is my first attempt to solve this problem, which uses lists and
    # # the built-in isprime() function.
    # #
    # # I tried to solve this problem without using lists and built-in
    # # isprime() function, as I thought that it would be a good exercise.
    # # But I couldn't come up with a solution.
    #
    # # We'll use a list to store the words from the original sentence
    # # whose lengths are prime numbers.
    # # We'll add the words to the list as we find them.
    # words_list = []
    #
    # # We'll use another list to store the words from the original sentence.
    # # We'll add the words to the list as we find them.
    # words_to_return = []
    #
    # # We'll use a for loop to iterate through the words in the original sentence.
    # for word in sentence.split():
    #     # We'll use a nested if statement to determine if the length of the
    #     # current word is a prime number.
    #     if isprime(len(word)):
    #         # If the length of the current word is a prime number,
    #         # we'll add the word to the words_list.
    #         words_list.append(word)
    #
    # # We'll use another for loop to iterate through the words in the
    # # words_list.
    # for word in words_list:
    #     # We'll use an if statement to determine if the word is in the
    #     # original sentence.
    #     if word in sentence:
    #         # If the word is in the original sentence, we'll add it
    #         # to the words_to_return list.
    #         words_to_return.append(word)
    #
    # # We'll use a for loop to iterate through the words in the
    # # words_to_return list.
    # for word in words_to_return:
    #     # We'll use an if statement to determine if the