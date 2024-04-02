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
    res = ""

    for i in range(len(word) - 2, -1, -1):
        if is_vowel(word[i]):
            last_i = i
            break
    else:
        return res
    for i in range(last_i + 1, len(word) - 1):
        if is_vowel(word[i]):
            res = word[i]
            break
    return res

def is_vowel(letter):
    return letter in ['a','e','i','o','u']

get_closest_vowel("yogurt") # "u"
get_closest_vowel("FULL") # "U"
get_closest_vowel("quick") # ''
get_closest_vowel("ab") # ''
