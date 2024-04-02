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
    
	Do not include these tokens in the code: # Prim ality Test
	"""
    
    class MyError(Exception): pass
    class PrimeSearcher:
        def __init__(self, max_numbers=10000):
            self.is_prime = [1] * max_numbers
            self.is_prime[0] = self.is_prime[1] = 0
            for i in range(max_numbers):
                if i > 1 and self.is_prime[i]:
                    self.is_prime[i * 2::i] = [0] * ((max_numbers - 1) // i + 1)
        def find_prime_numbers_in_range(self, a, b):
            return [n for n in range(a, b) if self.is_prime[n]]
    prime_numbers = PrimeSearcher().find_prime_numbers_in_range(2, 20)
    output = list()
    for word in sentence.split():
        if len(word) in prime_numbers:
            output.append(word)
    return ' '.join(output)
    
test_cases = [
    ("This is a test", "is")
    ("lets go for swimming", "go for"),
    ("Hello world", ""),
]

results = [words_in_sentence(*test_case) for test_case in test_cases]
    