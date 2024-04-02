def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    
	Do not include these tokens in the code: fo os = list ()
	"""


    if len(s) < 3:
        re
    
is_happy(s):
is_happy(s):

def is_happy(s):
    import re
    if len(s) < 3:
        return False
    
    if re.search([\w{0,4}]+', s):
        return False
    
    return True

def is_happy(str_input):
    if len(str_input) < 3: return False
    return not bool(re.search(r'\w{1}\w+\w{1}', str_input))

import re
from math import prod
n = int(input())
for _ in range(n):
    s = input()
    if len(s)<3 or bool(re.search(r'(\w{1}.+?)\1',s)): print("not good")
    else: print("good")

import re
from math import prod
n = int(input())
for _ in range(n):
    s = input()
    if len(s)<3 or bool(re.search(r'.+?(\w{1}).+?\1',s)) and sum([10-prod(j.ascii_value() for j in i) if len(i)==3 else 0 for i in re.findall('..?',s)])<0: print(s," -> not good")
    else: print(s," -> good")

import re
m=int(input())
for _ in range(m):
    x=input()
    print("good") if (x and x[0]!='a' and len(x)>2 and not re.search('[aeiouiy]',x) and not re.search('(.).\\1',x)) else print("not good")

