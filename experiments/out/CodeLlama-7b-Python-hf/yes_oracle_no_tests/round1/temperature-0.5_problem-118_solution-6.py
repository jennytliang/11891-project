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

    #vowels = "aeiou"
    vowels = "aeiou"
    vowels_dict = {}
    for vowel in vowels: vowels_dict[vowel] = 0

    # remove the first and last char
    #word = word[1:-1]
    #print(word)

    # reverse the word
    #word = word[::-1]

    for i in range(len(word)):
        if word[i] in vowels:
            vowels_dict[word[i]] += 1

    #print(vowels_dict)

    # get the closest vowel
    closest_vowel = ""
    closest_vowel_count = 0
    for vowel in vowels:
        if vowels_dict[vowel] > 0 and vowels_dict[vowel] > closest_vowel_count:
            closest_vowel = vowel
            closest_vowel_count = vowels_dict[vowel]

    #print(closest_vowel)

    # reverse the word
    #word = word[::-1]

    #print(word)

    # find the closest vowel in the reversed word
    #closest_vowel_index = word.rfind(closest_vowel)
    #print(closest_vowel_index)

    # find the first char before the closest vowel
    #closest_vowel_index = word.find(closest_vowel)
    #print(closest_vowel_index)

    # find the first char before the closest vowel
    #closest_vowel_index = word.rfind(closest_vowel)
    #print(closest_vowel_index)

    # get the first char before the closest vowel
    #if closest_vowel_index > 0:
    #    closest_vowel_index -= 1
    #    closest_vowel = word[closest_vowel_index]

    #return closest_vowel

