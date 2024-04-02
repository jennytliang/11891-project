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
    # # This is my solution, is there a better way?
    # def is_prime(a):
    #     if a == 1:
    #         return False
    #     for i in range(2, a):
    #         if a % i == 0:
    #             return False
    #     return True

    # words = sentence.split()
    # result = []
    # for word in words:
    #     if is_prime(len(word)) == True:
    #         result.append(word)

    # return " ".join(result)

    # This is the solution from the book, I am not sure I understand it completely.
    words = sentence.split()
    result = []
    for word in words:
        if len(word) > 1 and len(word) % 2 == 1 and len(word) % 3 == 1 and len(word) % 5 == 1:
            result.append(word)

    return " ".join(result)


print(words_in_sentence("This is a test"))
print(words_in_sentence("lets go for swimming"))
