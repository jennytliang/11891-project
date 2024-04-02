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
    
	Do not include these tokens in the code: # # Answer 1 :
	"""
    "".lower()
    "".isdigit()
    "".isalpha()
    "".isalnum()
    "".isascii()
    "".isdecimal()
    "".isnumeric()
    "".isspace()
    "".istitle()
    "".isprintable()
    "".isidentifier()
    "".islower()
    "".isupper()
    "".isunicode()
    "".join()
    "".rsplit()
    "".split()
    "".format()
    "".find()
    "".center()
    "".count()
    "".partition()
    "".rpartition()
    "".replace()
    "".expandtabs()
    "".startswith()
    "".endswith()
    "".strip()
    "".zfill()
	
	# Answer 1:
    def words_in_sentence(sentence):
        words = sentence.split()
        return " ".join([word for word in words if len(word) in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]])
	
	# Answer 2:
    def words_in_sentence(sentence):
        return " ".join([word for word in sentence.split() if len(word) in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]])

	# Answer 3:
   