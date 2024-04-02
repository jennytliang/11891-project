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

    i = word[::-1].find("a")
    if i == 0:
        i = word[::-1].find("e")
    if i == 0:
        i = word[::-1].find("i")
    if i == 0:
        i = word[::-1].find("o")
    if i == 0:
        i = word[::-1].find("u")
    if i <= 0:
        return ""
    i = word.find(word[::-1][i])
    #print(word[i], word[i + 1])
    if not is_vowel(word[i]) and is_vowel(word[i + 1]):
        return word[i + 1]
    i += 1
    while not is_vowel(word[i]) and i <= word[::-1].find("a") and \
         i <= word[::-1].find("e") and i <= word[::-1].find("i") and \
         i <= word[::-1].find("o") and i <= word[::-1].find("u") and i <= len(word):
        i += 1
    if i <= len(word):
        return word[i]
    else:
        return ""

def is_vowel(c):
    return c == "a" or c == "e" or c == "I" or c == "i" or c == "o" or c == "u"
