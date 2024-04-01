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
    """
    
    for v in ['a', 'e', 'i', 'o', 'u', 'y'][-5:]:
        cons = None
        for idx, letter in enumerate(reversed(word), reverse=True):
            if is_consonant(letter, v):
                cons=letter
                break
        if cons and v and word.rindex(v) < word.rindex(cons) < word.find(v, idx):
            return v
    
    return ""


def get_closest_vowel2(phrase):
    vow_dic = {'A': 'Y', 'C': 1, 
               'G': 2, 'H': 0, 'N': 1, 'U': 1}

