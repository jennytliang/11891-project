from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Do not include these tokens in the code: [ s for s in
	"""


    
    # def recurse(tmp_string, acc):

    out = [string[0]]
    out += out[-1] + string[1]

    return

def all_subparts(string: str) -> List[str]:
    """Return all (non empty) subparts of a string """
    subparts = [] 
    for i in range(len(string)): # could be used range(len(string)+1): or range(1,len(string))
            subparts.append(string[0:i])
            # print(subparts[i])
    # print (subparts[0]) # returns 'a'


    """"Return subparts list starting from string[0] all the way to the last char 'e' """
    """def subparts(string):
        x = []
        i = 0
        while i + 2 < len(s):
            x.append(s[i]+s[i+1])
            if i+2 == len(s)-1:
                x.append(s[-2]+s[-1]))
                break
            i+=1
        try:
            print(''.join(x))
        except TypeError:
            print(x)"""
        
    return



def longest_run(string: str) -> (int, int):
    """Returns a tuple of (length, pos) of the longest run of ascending letters in string """
    max_run = 0
    count_run = 0

    for i in range(len(string)-2):
        count_run = string[i] < string[i+1]
    else: 
        count_run += 1 # 2
   
    count_run += 1

    count_max, long_pos = longest_run(string[1:])
    
    if count_run > count_max:
        count_max = count_run
        pos_max = 0
    
    print(string[0] + str(count_run))
    





