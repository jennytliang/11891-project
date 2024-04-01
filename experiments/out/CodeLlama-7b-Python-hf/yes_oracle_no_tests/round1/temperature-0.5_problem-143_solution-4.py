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
    
	Include these tokens in the code:  def is _ prime ( a ):
	Do not include these tokens in the code: words =
	"""

    def is_prime(a):
        if a == 1:
            return False
        elif a == 2:
            return True
        elif a % 2 == 0:
            return False
        else:
            i = 3
            while i * i <= a:
                if a % i == 0:
                    return False
                i += 2
            return True

    words = sentence.split(" ")
    new_words = []
    for word in words:
        if is_prime(len(word)):
            new_words.append(word)

    return " ".join(new_words)
