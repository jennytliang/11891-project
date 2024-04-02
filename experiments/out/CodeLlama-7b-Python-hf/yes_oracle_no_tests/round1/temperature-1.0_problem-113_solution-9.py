def odd_count(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.

    >>> odd_count(['1234567'])
    ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    >>> odd_count(['3',"11111111"])
    ["the number of odd elements 1n the str1ng 1 of the 1nput.",
     "the number of odd elements 8n the str8ng 8 of the 8nput."]
    
	Include these tokens in the code: ans , template
	Do not include these tokens in the code: result
	"""
    
    final = []
    
    for n in lst:
        a = 0
        for i in range(len(n)):
            if int(n[i]) %2 == 1:
                a+=1
                
        ans = "the number of odd elements %sn the str%sng %s of the %snput."%(a, a, n, a)
        final.append(ans)
    return final


def count_char(word):
	'''
	Given a word, return a list whose first element is 'a' and whose second element is the length
	of the string.
	'''
	#template = ['a', "the length of the word is (the number of a’s in the word)"]
	#result =  template[0] + ', ' + template[1]
	ans = []
	ans.append('a')
	ans.append("the length of the word is " + str(word.count('a')))
	return ans

def double_each_two_digits(lst):
	'''
	Given a list of numbers, return a list whose each element is double
	the integer value of the corresponding element in the original list.
	'''
	#template = ["(the double of the number n)"]
	#result =  template[0] -> ['2n', '4n', '6n', '3n', '5n', '7n', '9n']
	from re import sub
	import re
	ans = []
	for i in lst:
		a = re.sub('^\D+(\d)\D+(\d)\D*$', '\\1', str(i))
		b = re.sub('^\D+(\d)\D+(\d)\D*$', '\\2', str(i))
		ans.append(str(int(a+b))*2)
	return ans

def count_the_words(sentence, words):
	'''
	Given a string (sentence) and a list of words, return a number indicating how many
	times the given words, appeared in the sentence.
	'''
	#