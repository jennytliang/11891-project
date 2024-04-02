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
    # 1st brute-force solution
    # O(n^2) time | O(n) space
    # def wordsInSentence(sentence):
    #     # TODO: Write your code here
    #     sentence = sentence.split(" ")
    #     new_sentence = []
    #     for word in sentence:
    #         if is_prime(len(word)) == True:
    #             new_sentence.append(word)
    #     return " ".join(new_sentence)

    # 2nd optimized solution
    # O(n^2) time | O(n) space
    # def wordsInSentence(sentence):
    #     # TODO: Write your code here
    #     sentence = sentence.split(" ")
    #     new_sentence = []
    #     for word in sentence:
    #         if is_prime(len(word)) == True:
    #             new_sentence.append(word)
    #     return " ".join(new_sentence)

    # 3rd optimized solution
    # O(n) time | O(n) space
    # def wordsInSentence(sentence):
    #     # TODO: Write your code here
    #     sentence = sentence.split(" ")
    #     new_sentence = []
    #     for word in sentence:
    #         if is_prime(len(word)) == True:
    #             new_sentence.append(word)
    #     return " ".join(new_sentence)

    # 4th optimized solution
    # O(n) time | O(1) space
    # def wordsInSentence(sentence):
    #     # TODO: Write your code here
    #     sentence = sentence.split(" ")
    #     new_sentence = []
    #     for word in sentence:
    #         if is_prime(len(word)) == True:
    #             new_sentence.append(word)
    #     return " ".join(new_sentence)

    # 5th optimized solution
    # O(n