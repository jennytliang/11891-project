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
    
	Include these tokens in the code: def is
	Do not include these tokens in the code: pass get _
	"""
    vowels = "aeiouAEIOU"
    vowels_indices = []
    for i in range(len(word)):
        if word[i] in vowels:
            vowels_indices.append(i)
    vowels_indices.sort()
    if len(vowels_indices) < 2:
        return ""
    vowels_indices.reverse()
    for i in range(len(vowels_indices) - 1):
        if vowels_indices[i] < vowels_indices[i + 1] - 2:
            return word[vowels_indices[i]]
    return ""


print(get_closest_vowel("yogurt"))
print(get_closest_vowel("FULL"))
print(get_closest_vowel("quick"))
print(get_closest_vowel("ab"))
