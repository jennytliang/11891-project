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
    
	Include these tokens in the code: def is _ v owel ( ch : str )
	"""
    vowels = "AEIOU"

    def is_vowel(ch):
        return ch in vowels
    word_rev = word[::-1]
    for letter in word_rev:

        if (letter == "a" or letter== "e" or letter == "i" or letter == "o" or letter == "u"):
            continue
        else:
            word_rev = word_rev[word_rev.index(letter):]

            def is_consonant(ch):
                return ch in vowels

            flag = 0
            for rletter in word_rev:
                if is_vowel(rletter) == True:
                    return rletter
                else:
                    continue
            return ""
