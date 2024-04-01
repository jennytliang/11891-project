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
    def is_prime(a):
        if a == 1:
            return False
        for i in range(2, a//2 + 1):
            if a % i == 0:
                return False
        return True
    
    words = sentence.split()
    res = []
    for word in words:
        if len(word) == 1:
            continue
        if is_prime(len(word)):
            res.append(word)
    return ' '.join(res)
    
if __name__ == '__main__':
    print("Example 1:")
    print('Input: sentence = "This is a test"')
    print('Output:', words_in_sentence("This is a test"))

    print("\nExample 2:")
    print('Input: sentence = "lets go for swimming"')
    print('Output:', words_in_sentence("lets go for swimming"))
