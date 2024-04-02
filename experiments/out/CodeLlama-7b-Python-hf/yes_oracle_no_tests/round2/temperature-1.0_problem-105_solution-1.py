def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    
      If the array is empty, return an empty array:
      arr = []
      return []
    
      If the array has any strange number ignore it:
      arr = [1, -1 , 55] 
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
      return = ['One']
    
	Include these tokens in the code: def to _ word ( x : int ) ->
	"""


def main():
    print("**By Length**")
    test_main(by_length)


class Word:
    def __init__(self, word='', value=1):
        self.word = word
        return None

    def __str__(self):
        line = "({}, {})".format(self.word, self.value)
        return line

    def __repr__(self):
        return str(self.word)

    def sort(self, words, words_by_length):
        sorted_words = sorted(words, key=lambda x: len(x.word))
        print("In: {}".format(str(sorted_words)))
        l = len(str(sorted_words[0]))
        if words_by_length.get(l):
            words_by_length[l] = words_by_length[l] + sorted_words
        else:
            words_by_length[l] = sorted_words
        return None


class WordList:
    def __init__(self, words=list()):
        self.words = words
        return None

    def __str__(self):
        line = str([str(s) for s in self.words])
        return line

    def __repr__(self):
        return str([s.word for s in self.words])


class WordSort:
    def __init__(self):
        self.result = WordList()
        self.words_by_length = {}
        return None

    def __str__(self):
        line = str(self.result)
        return line

    def __repr__(self):
        return str(self.result.words)

    def sort(self, words):
        print('In: ' + str(words))
        for word in words:
            if WordList.is_number(word):
                w = Word().getIntFromWord(word)
                print('Number: {}'.format(w))
                w_value = w.value
                w_word = w.word
                ws = WordList.createWord(w_value