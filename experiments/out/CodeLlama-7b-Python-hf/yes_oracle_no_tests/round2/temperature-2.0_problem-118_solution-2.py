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
    # Rough first pass:
    if len(word) < 2:
        return ""
    vowels = ['a', 'e', 'i', 'o', 'u']
    if word[-1] in vowels:
        return ""
    if word[0] in vowels:
        return ""
    for i in range(len(word)-1):
        if word[i] not in vowels:
            if word[i+1] in vowels:
                return word[i+1]
    return ""


def get_closest_vowel_solution(word):
    """
    This is the solution provided by the course.
    """
    vowels = 'aeiou'

    for i in range(len(word)-1, 0, -1):
        if word[i] in vowels:
            for j in range(i):
                if word[j] not in vowels:
                    return word[j+1]
    return ''


print(get_closest_vowel("yogurt"))
print(get_closest_vowel("FULL"))
print(get_closest_vowel("quick"))
print(get_closest_vowel("ab"))
print(get_closest_vowel("a"))
print(get_closest_vowel("b"))
print(get_closest_vowel("q"))
print(get_closest_vowel("qu"))
print(get_closest_vowel("quu"))
print(get_closest_vowel("quuu"))
print(get_closest_vowel("quuuu"))
print(get_closest_vowel("quuuuu"))
print(get_closest_vowel("quuuuuu"))
print(get_closest_vowel("quuuuuuu"))
print(get_closest_vowel("quuuuuuuu"))
print(get_closest_vowel("quuuuuuuuu"))
print(get_closest_vowel