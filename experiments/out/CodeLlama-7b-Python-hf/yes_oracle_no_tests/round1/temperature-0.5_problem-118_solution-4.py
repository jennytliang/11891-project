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

    # First, find the index of the last consonant.
    last_consonant = -1
    for i in range(len(word)):
        if is_consonant(word[i]):
            last_consonant = i

    # Now, find the index of the second last consonant.
    second_last_consonant = -1
    for i in range(last_consonant):
        if is_consonant(word[i]):
            second_last_consonant = i

    # Now, return the vowel between the two consonants.
    if second_last_consonant == -1:
        return ""
    else:
        return get_vowel(word[second_last_consonant + 1:last_consonant + 1])

def is_consonant(ch):
    return ch.isalpha() and not ch.isupper() and not ch.islower()

def is_vowel(ch):
    return ch.lower() in ['a', 'e', 'i', 'o', 'u']

def get_vowel(word):
    for ch in word:
        if is_vowel(ch):
            return ch
    return ""












































































































































































































