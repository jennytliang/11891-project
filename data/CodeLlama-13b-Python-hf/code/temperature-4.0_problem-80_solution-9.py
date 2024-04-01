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
    """
    if len(s) < 3 or s == "aaa" or s=="bbb" or s=="ccc":
        return False
    else:
        for i in range(2):
         if s[i] == "a":
            a = True
         if s[i] == "b":
            b = True
         if s[i] == "c":
            c = True
        return True
    if a != b and b !=c and c != a:     
        return True
    else:
        False


import re

def is_valid_ISBN(isbn):
    """The library that you are working with is expanding their online catalog,
     and in the new version all books will be represented by their ISBN instead of a book number.
      So they come up with a unique 10-digit code,
       called ISBN (International Standard Book Number),
        intended to support and standardize book bookkeeping and product identification,
         including the book's title, author, publisher and binding. 
         Given a ISBN, you should check if the ISBN that was given is valid;
          in particular the following rules need 
           to be verified:
•	There should be 10 digits, and only numbers from 0-9 should be 
       included in 
        the string
•	It should NOT contain any other characters
•	If there are leading zeroes, the ISBN code should 
        NOT start with 0
In case ISBN doesn't match to what was explained above, print "False".
For example, 1491960178 is valid, 
but 9729245500 is invalid because it contains leading zeroes
19960718233 is valid
007287086363156512 is invalid
01425465789 is invalid, this ISBN code 
      contains letters 
(not numbers) in between the numbers
1401764691301 is invalid, because it doesn't 
    have exactly 10 digits. """
        
