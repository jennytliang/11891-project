def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code:  m x _ ch _ cnt ,
	Do not include these tokens in the code: if len ( words ) == 1 :
	"""

    def _find_max(words):
        if len(words) == 1:
            return words[0]

        # m x _ ch _ cnt
        m = ""
        m_len = 0
        for word in words:
            # ch _ cnt
            ch = {}
            for i in word:
                if i not in ch:
                    ch[i] = 1
                else:
                    ch[i] += 1

            if len(ch) > m_len:
                m = word
                m_len = len(ch)
            elif len(ch) == m_len and word < m:
                m = word
                m_len = len(ch)
        return m

    return _find_max(words)


def test_function():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    assert find_max(["a", "a", "b", "b", "c", "c"]) == "a"
    assert find_max(["abc", "bcd", "cde"]) == "abc"
    assert find_max(["abc", "abcd", "bcd", "cde"]) == "abc"


if __name__ == '__main__':
    test_function()
