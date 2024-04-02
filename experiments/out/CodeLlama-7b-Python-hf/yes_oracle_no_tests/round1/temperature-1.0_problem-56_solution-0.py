def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    
	Include these tokens in the code: c nt =
	"""
	c=0
	n=brackets.count("<")
	if brackets=='<': return False
	elif n==0 and c==0: return True
	elif n>c:
		for i in range(len(brackets)):
			if brackets[i]=='<': c+=1
			elif brackets[i]=='>': c-=1
		if c==0: return True
	elif n<c: return False

if __name__=="__main__":
	import doctest, sys
	run_doctest = False if len(sys.argv) > 1 else True
	doctest.main(verbose = run_doctest, optionflags = doctest.FAIL_FAST)	
