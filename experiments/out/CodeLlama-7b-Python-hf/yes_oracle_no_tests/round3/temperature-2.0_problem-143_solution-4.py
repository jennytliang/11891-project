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
    
	Do not include these tokens in the code: ### ######## #### ## #
	"""
    ######################
    # PSEUDOCODE
    # 1. split sentence to list of words
    # 2. create list of all prime numbers
    # 3. for each word in list of words, check if length of word is in list of prime numbers
    # 4. if so, add to new list and remove from original list of words
    # 5. join list of words with space
    ######################
    import math

    def is_prime(num):
        if num == 1:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def words_in_sentence(sentence):
        words = sentence.split()
        primes = []
        for i in range(1, len(words) + 1):
            if is_prime(i):
                primes.append(i)
        new_list = []
        for word in words:
            if len(word) in primes:
                new_list.append(word)
        return " ".join(new_list)
