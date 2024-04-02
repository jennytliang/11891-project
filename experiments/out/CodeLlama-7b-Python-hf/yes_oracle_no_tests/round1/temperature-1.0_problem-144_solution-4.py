def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    
	Include these tokens in the code: x 1
	Do not include these tokens in the code: num _
	"""
    n1, d1 = int(x.split('/')[0]), int(x.split('/')[1])
    n2, d2 = int(n.split('/')[0]), int(n.split('/')[1])
    return "{}".format((n1*n2) // d2) == x

simplify("1/5", "5/1")

# TEST
tests, corrects = 0, 0
import json
datapath = 'A-large-practice-6.json'
with open(datapath) as inf: 
    for n, line in enumerate(inf):
        tests += 1
        x, n = line.strip().split()
        try:
            if simplify(x, n):
                corrects += 1
        except:
            continue
print('#TESTS', tests)
print('#CORRECT', corrects)
print('{}/{} = {}'.format(corrects, tests, corrects / tests))