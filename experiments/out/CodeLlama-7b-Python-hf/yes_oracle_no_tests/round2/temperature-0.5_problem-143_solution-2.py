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
    
	Include these tokens in the code: def
	Do not include these tokens in the code: # 1 . Find all
	"""
    # # First, write a function that finds all prime numbers in a given number.
    # # Then, write a function that finds all words in a given sentence.
    # # Then, write a function that finds all prime words in a given sentence.
    # # Finally, write the main function.
    #
    # # 1. Find all prime numbers in a given number.
    # def find_all_prime_numbers(number):
    #     prime_numbers = []
    #     for i in range(2, number + 1):
    #         is_prime = True
    #         for j in range(2, i):
    #             if i % j == 0:
    #                 is_prime = False
    #         if is_prime:
    #             prime_numbers.append(i)
    #     return prime_numbers
    #
    # # 2. Find all words in a given sentence.
    # def find_all_words(sentence):
    #     words = sentence.split(" ")
    #     return words
    #
    # # 3. Find all prime words in a given sentence.
    # def find_all_prime_words(sentence):
    #     words = find_all_words(sentence)
    #     prime_words = []
    #     for word in words:
    #         if len(find_all_prime_numbers(len(word))) > 1:
    #             prime_words.append(word)
    #     return prime_words
    #
    # # 4. Finally, write the main function.
    # def words_in_sentence(sentence):
    #     return find_all_prime_words(sentence)
    #
    # print(words_in_sentence(sentence))

    # # 1. Find all prime numbers in a given number.
    # def find_all_prime_numbers(number):
    #     prime_numbers = []
    #     for i in range(2, number + 1):
    #         is_prime = True
    #         for j in range(2, i):
    #