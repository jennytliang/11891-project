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
    # RW Combine
    # O(n) time | O(n) space - where n is the length of the word
    def is_vowel(ch):
        return ch in "aeiouAEIOU"
    
    vowels = list(filter(is_vowel, word))
    if len(vowels) < 2:
        return ""

    vowels_indexes = [word.index(vowel) for vowel in vowels]
    right_consonants_indexes = [i for i in range(len(word)) if is_vowel(word[i]) == False and i != len(word) - 1]

    right_consonants_vowel_indexes = []
    for i in right_consonants_indexes:
        right_consonants_vowel_indexes.append(vowels_indexes[vowels_indexes.index(i) + 1])

    return min(right_consonants_vowel_indexes, key = lambda x: abs(x - i))

def get_closest_vowel_b(word):
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
    # RW Split
    # O(n) time | O(n) space - where n is the length of the word
    def is_vowel(ch):
        return ch in