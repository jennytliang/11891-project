def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x _ ch _ cnt , ans =
	Do not include these tokens in the code: if not words or len (
	"""
    length = len(words)
    if not words or length == 0: return
    #m, x_ch, cnt, ans
    m = max_x_ch = max_cnt = ans = ""
    for word in words:
        cnt = len(set(list(word)))
        if max_x_ch < word or (max_x_ch == word and max_cnt < cnt):
            max_cnt = cnt
            max_x_ch = word
    return max_x_ch
    
def find_max_length(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the length of the longest word(
    in letters). Don't use len() function of Python.
    
    find_max_length(["Python", "Ruby"]) == 6
    find_max_length(["Python", "Pear"]) == 5
    find_max_length(["Python"]) == 6
    """
    length = len(words)
    if not words or length == 0: return
    cnt = m = 0
    for word in words:
        if m < len(word):
            m = len(word)
            cnt = 1
        elif m == len(word):
            cnt += 1
    return m if cnt == 1 else 0



if __name__ == "__main__":
    words = list(map(str, input("Enter a string to seperate with commas:\n").split(",")))
    print("The maximum width word is: ", find_max(words))
    print("The maximum unique character words are: ", find_max_length(words))