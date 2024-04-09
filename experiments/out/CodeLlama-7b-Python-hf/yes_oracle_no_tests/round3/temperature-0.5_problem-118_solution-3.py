def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    
	Include these tokens in the code: : str ) -> bool :
	Do not include these tokens in the code: ):
	"""



    def is_vowel(char):
        return char in "AEIOUaeiou"

    def is_consonant(char):
        return char in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"

    def find_closest_consonant(word, vowels):
        """Returns the closest consonant from the right side of the word.

        word: str
        vowels: str
        """
        for char in reversed(word):
            if is_consonant(char):
                return char

    def find_closest_vowel(word, vowels):
        """Returns the closest vowel from the right side of the word.

        word: str
        vowels: str
        """
        for char in reversed(word):
            if is_vowel(char):
                return char

    # check if vowels is a vowel
    if is_vowel(word):
        return word

    # find the closest consonant
    consonant = find_closest_consonant(word, vowels)

    # return the closest vowel from the right side of the consonant
    if consonant:
        return find_closest_vowel(word[word.rindex(consonant):], vowels)

    # return empty string
    return ""

























































































































































