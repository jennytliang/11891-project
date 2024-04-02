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
    # #Answer 1:
    # def is_prime(a):
    #     return a > 1 and all(a % i for i in range(2, int(a ** 0.5) + 1))

    # def words_in_sentence(sentence):
    #     sentence = sentence.split(" ")
    #     for word in sentence:
    #         if is_prime(len(word)):
    #             print(word, end=" ")

    # words_in_sentence(sentence)

    # #Answer 2:
    # def words_in_sentence(sentence):
    #     sentence = sentence.split(" ")
    #     for word in sentence:
    #         if isPrime(len(word)):
    #             print(word, end=" ")

    # words_in_sentence(sentence)

    # # Answer 3:
    # def words_in_sentence(sentence):
    #     sentence = sentence.split(" ")
    #     for word in sentence:
    #         if isPrime(len(word)):
    #             print(word, end=" ")

    # words_in_sentence(sentence)

    # # Answer 4:
    # def words_in_sentence(sentence):
    #     sentence = sentence.split(" ")
    #     for word in sentence:
    #         if isPrime(len(word)):
    #             print(word, end=" ")

    # words_in_sentence(sentence)

    # Answer 5:
    def words_in_sentence(sentence):
        sentence = sentence.split(" ")
        for word in sentence:
            if isPrime(len(word)):
                print(word, end=" ")

    words_in_sentence(sentence)


words_in_sentence("This is a test")
