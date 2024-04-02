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
    #################
    # Simple solution
    from re import compile
    
    # get all words
    words = re.split(r'\s+', sentence)
    # go over the words and check for prime
    prime_length_words = [token for token in words if len(token) and len(token) in (2, 3, 5, 7, 11, 13, 17, 19)]
    
    return ' '.join(prime_length_words)
    #################
    # O(n1 + n2)?
    def is_prime(a):
        if a < 2: return False
        for i in range(2, a):
            if a % i == 0:
                return False
        return True


    tokens = sentence.split(' ')
    return ' '.join([token for token in tokens if is_prime(len(token))])


