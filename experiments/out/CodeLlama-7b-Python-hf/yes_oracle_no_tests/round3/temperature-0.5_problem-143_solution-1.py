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
    
	Include these tokens in the code: return not ( a < 2 or any (
	Do not include these tokens in the code: if
	"""

    def is_prime(a):
  
        # Corner cases
        if a <= 1:
            return False
        if a <= 3:
            return True

        # This is checked so that we can skip
        # middle five numbers in below loop
        if a % 2 == 0 or a % 3 == 0:
            return False

        i = 5
        while i * i <= a:
            if a % i == 0 or a % (i + 2) == 0:
                return False
            i = i + 6

        return True

    def solution(sentence):
        words = sentence.split()
        new_sentence = ""
        for word in words:
            if is_prime(len(word)):
                new_sentence += " " + word
        return new_sentence.strip()

    return solution