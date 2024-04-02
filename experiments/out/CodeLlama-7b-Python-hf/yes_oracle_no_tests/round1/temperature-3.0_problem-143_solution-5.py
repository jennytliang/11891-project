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
    
	Include these tokens in the code: def is _ prime ( a ):
	Do not include these tokens in the code: result = [] for word
	"""
    ############# 1. Naive solution #############
    # def is_prime(a):
    #     for i in range(2, a):
    #         if a % i == 0:
    #             return False
    #     return True
    
    # def words_in_sentence(sentence):
    #     result = []
    #     for word in sentence.split():
    #         if is_prime(len(word)):
    #             result.append(word)
    #     return " ".join(result)

    ############# 2. Optimized solution #############
    # def is_prime(a):
    #     for i in range(2, int(a ** 0.5) + 1):
    #         if a % i == 0:
    #             return False
    #     return True
    
    # def words_in_sentence(sentence):
    #     result = []
    #     for word in sentence.split():
    #         if is_prime(len(word)):
    #             result.append(word)
    #     return " ".join(result)

    ############# 3. Better solution #############
    # def is_prime(a):
    #     for i in range(2, int(a ** 0.5) + 1):
    #         if a % i == 0:
    #             return False
    #     return True
    
    # def words_in_sentence(sentence):
    #     result = []
    #     for word in sentence.split():
    #         if is_prime(len(word)):
    #             result.append(word)
    #     return " ".join(result)

    ############# 4. Optimized solution #############
    def is_prime(a):
        return not any(a % i == 0 for i in range(2, int(a ** 0.5) + 1))
    
    def words_in_sentence(sentence):
        return " ".join(word for word in sentence.split() if is_