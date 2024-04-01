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
    
	Include these tokens in the code:  def is _ v owel ( ch
	Do not include these tokens in the code: ow els =
	"""

    vowels = "aeiou"
    last_consonant = ""
    for i in range(len(word) - 1, -1, -1):
        if word[i] in vowels:
            return word[i]
        elif word[i] not in vowels:
            last_consonant = word[i]
    return ""

    # def get_closest_vowel(word):
    #     vowels = "aeiou"
    #     last_vowel = ""
    #     for i in range(len(word) - 1, -1, -1):
    #         if word[i] in vowels:
    #             return word[i]
    #         elif word[i] not in vowels:
    #             last_vowel = word[i]
    #     return ""

    # return last_vowel if not last_vowel else ""


assert get_closest_vowel("yogurt") == "u", "get_closest_vowel('yogurt') == 'u'"
assert get_closest_vowel("FULL") == "U", "get_closest_vowel('FULL') == 'U'"
assert get_closest_vowel("quick") == "", "get_closest_vowel('quick') == ''"
assert get_closest_vowel("ab") == "", "get_closest_vowel('ab') == ''"
