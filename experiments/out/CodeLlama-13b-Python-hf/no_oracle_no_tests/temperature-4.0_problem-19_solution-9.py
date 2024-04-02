from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # valid_nums = sorted(list(map(str, list(range(0, 10))))) # or valid_nums = ['zero'] through 'nine'
    valid_nums = list(range(10))
    numlist = []

    for number in numbers.split(" "):
        numlist += next((i for i in valid_nums if i==number.replace('zero','') and i[1:]) or [number])

    sorted_numlist, i = (list(reversed(numlist)),0) if (numlist!=valid_nums) else (numlist,[])
    while i < len(sorted_numlist):
        sorted_numlist[i] = 0 if sorted_numlist[i] is numlist[-1] else 'zero'
        i += 1
    
    res_string = " ".join([str(val) for val in sorted(numlist[-1::-1])]).lstrip()

    return f"{'invalid input':=''.join(['return',' this', ' '])}".join(['','',res_string]).lstrip('=') or ("invalid input" if all(' '.join(numbers)==num_str or s_char=='O' for num_str in ('-zero-','-one-','' if ('' in numbers): '-two-' '','-.three.','-.four.','-.five.', '-six','.','-nine') else '') and any((' '.join(numbers) == i) or i in numbers if i in  ['-one.', 'nine.'] and 'a'!='c' or ['.', 'I', ".", ' ']==[1] and '-a'=='c' or (True in ('a'=='I') and s_chars) else 5 for i in ["-three.", "seven.", "-two.", "zero."]))
    # The below code does not work with 'five' in "zero eight five six", but does work with five in "six five four three two one zero"

    return f"{'invalid input':=''.strip()}{'return'|'this '}{''.join(['', '', ' ', '', '', '', 'inva']}{'alid i'}{'inp'}[2 if 'five' in 'se'*[1]+[''][None]=={2:True} or [1]!=1 else 0:2]}"
        # This code below is also not working well



def find_numbers(numbers:str, find:int) -> List[int]:
    """  Input a list of numbers as space-delimited string
    and a number find to match
    >>> find_numbers('three one five', 12)
    'one three'      # or a List[] or a list
    """
    valid_numbers = sorted(set(list(map(int, [num.replace('zero', '') for num in sorted(set(num.split('three')))]))))
    return next((str(valid_numbers[num_i]) for num in valid_numbers if next((v if v % num == 0 and num*len(valid_numbers)-1 == find else find - num for num in range(num, valid_numbers[num_i], -1)), (next((int(n1)+n2)*n3 + n4 if n1 is str(valid_numbers.index(0)) or n1=='one' else -n5+n6*n2 for num in nums[n:]) for num in list(zip(n.replace('-','one '), n.replace(' ',''), n.replace('one ')) if len(n)==5 and sum(int(n2)==n+1 if n1 == n*n else n-1 == n+n2 or n-n4*(n3/3*n2) in [1,-1,-1*2*3 if True and False*1*2==4*5 or n in numbers*n for n0 in num] else 2 for n1, n2, n3, n4 in (n, n, int(n.replace('three', '-five')[-1::-1][1]), 'four').split('*'))==3), n4*n5 if str(n2.count(0)) == n6[-2] == n7 == n5 == (n8-1)*n9 for num, n5, n6, n1, n5, n7,n8, n9 in (num for num in nums)) if sum((-1*1==n1+n2+n3==n5 if n1 == 1*n +1 or int(n1) or n2 == (n3*n7)-1 else 1+1 in (n4, n6) + (n5, )+[n1] if n4.index(n3)+1 == n5 or n1 in nums and (n1-2)*n8+2 == n7 and (n5+n1+n2)-n8-2 == n6*n6+n4 if n1 is False*(n5-n3) + n6 and n6*n4 == n2+(n3+n4/2*n6)+n3*n1+n4/6*n7 else ((n5+n6)+n7==1 +n4*n1-n1*n8+n8 if n4 == 1 else (n3+1+1)+(n3+(n5-1)*n1) if n3 == n1*n1*n4 else n6+(n9+n1)+(n9-n1)/(n6+n7) if n3 is False-n6+n8*3 else 2*n3*2 else -1+2*2+1-1 if n5 in ('one','four') else -3/n6+n4*n5)) == 1 else -1 * n9 if n3 is n4+n4*n5 or n2 == 1+n4 or n3.count(n5*(-1/4)*n6)*n5 + n4*n6 or n3-n1*n1-n3*n5 + n6-n9+n3*n9*n9 or n3-n6 +(n9+n1)*n4+n3*n8 if True and n3 is 0 or n5 else n4*n3 else -n3+2
    )



import numpy as np

def is_floats(x) -> bool:
    # check if it is float; List[float]; Tuple[float]
    if isinstance(x, float):
        return True
    if isinstance(x, (list, tuple)):
        return all(isinstance(i, float) for i in x)
    if isinstance(x, np.ndarray):
        return x.dtype == np.float64 or x.dtype == np.float32
    return False


def assertion(out, exp, atol):
    exact_match = out == exp

    if atol == 0 and is_floats(exp):
        atol = 1e-6
    if not exact_match and atol != 0:
        np.testing.assert_allclose(out, exp, atol=atol)
    else:
        assert exact_match


def check(candidate):
    inputs = [[''], ['three'], ['three five nine'], ['five zero four seven nine eight'], ['six five four three two one zero'], ['four eight two'], ['nine'], ['one six two four nine'], ['two seven eight zero five'], ['nine zero'], ['seven three one'], ['two two three three four five six'], ['zero five four one seven eight two six'], ['nine eight seven six five four three two one zero'], ['two zero nine four five six'], ['nine eight seven six five four one zero'], ['two zero nine'], ['four eight'], ['zero five four one seven'], ['six'], ['two two four five six'], ['zero five four one'], ['zero five seven'], ['four two'], ['four'], ['two six'], ['two two five six'], ['seven'], ['zero five four zero five four one seven eight two six'], ['zero five one seven eight two six'], ['four four eight two'], ['seven three'], ['nine eight seven five four three two one zero'], ['two four five six'], ['zero four one'], ['zero seven eight two six'], ['zero five eight two six'], ['zero'], ['one six'], ['nine six'], ['two seven eight five'], ['two'], ['two three three four five six'], ['zero five four seven'], ['nine eight seven one zero'], ['four five six'], ['two nine'], ['two two three'], ['nine eight seven six five two one zero'], ['zero five six'], ['zero five'], ['zero five two six'], ['zero five four zero four one seven eight two six'], ['four eight two two three'], ['five four one seven eight two six'], ['nine seven six five two one zero'], ['nine eight seven six zero'], ['two nine seven six five two one zero'], ['two four six'], ['nine one zero'], ['four six'], ['zero five four'], ['zero two six'], ['zero five one'], ['nine six five two one zero'], ['two nine eight seven six five four one zero'], ['zero four one seven'], ['two zero nine four zero four one'], ['one zero five six'], ['nine seven six five two zero'], ['two nine eight seven six five four one zero one zero'], ['two nine seven six five two one zero five two six'], ['one'], ['nine eight seven five four three two one'], ['two seven'], ['nine eight seven six'], ['zero five one seven six'], ['nine one zero five four one seven eight two six'], ['zero two'], ['two four zero four one'], ['zero five four zero five four one seven'], ['two two four five'], ['zero one seven eight two six'], ['nine two six'], ['nine one zero five four one six'], ['two two seven eight zero five four five six'], ['two four zero four'], ['two zero six'], ['two three'], ['two nine seven six five two one zero four five six'], ['nine six five two three three four five six one zero'], ['nine eight one zero'], ['two four'], ['four two nine eight seven six five four one zero'], ['two two'], ['nine seven six five two one'], ['one six two nine'], ['zero five four one seven eight six'], ['nine seven four six'], ['five six'], ['two zero nine four one'], ['zero five four one eight two six'], ['nine one zero five four one'], ['one two three four five six seven eight nine'], ['nine eight seven six five four three two one'], ['five seven eight six nine four zero two one three'], ['four six nine eight seven one five zero two three'], ['seven one zero five two four eight six nine three'], ['zero one two three four five six seven eight nine'], ['two four six eight zero one three five seven nine'], ['nine seven five three one eight six four two zero'], ['one zero three four two six five seven eight nine'], ['seven five zero four nine eight two six one three'], ['five'], ['eight'], ['four six nine eight five zero two three'], ['one two three three'], ['two nine eight seven six five four three two one seven nine'], ['zero one two five six seven eight nine'], ['five four six nine eight seven one five zero two three two one three'], ['nine eight seven six five four two one'], ['one two one four'], ['one one one one one'], ['one two'], ['four four two six nine two zero'], ['nine eight seven six five two three two one'], ['nine eight seven two one'], ['one zero three nine'], ['nine eight'], ['seven one zero five three'], ['zero two three']]
    results = ['', 'three', 'three five nine', 'zero four five seven eight nine', 'zero one two three four five six', 'two four eight', 'nine', 'one two four six nine', 'zero two five seven eight', 'zero nine', 'one three seven', 'two two three three four five six', 'zero one two four five six seven eight', 'zero one two three four five six seven eight nine', 'zero two four five six nine', 'zero one four five six seven eight nine', 'zero two nine', 'four eight', 'zero one four five seven', 'six', 'two two four five six', 'zero one four five', 'zero five seven', 'two four', 'four', 'two six', 'two two five six', 'seven', 'zero zero one two four four five five six seven eight', 'zero one two five six seven eight', 'two four four eight', 'three seven', 'zero one two three four five seven eight nine', 'two four five six', 'zero one four', 'zero two six seven eight', 'zero two five six eight', 'zero', 'one six', 'six nine', 'two five seven eight', 'two', 'two three three four five six', 'zero four five seven', 'zero one seven eight nine', 'four five six', 'two nine', 'two two three', 'zero one two five six seven eight nine', 'zero five six', 'zero five', 'zero two five six', 'zero zero one two four four five six seven eight', 'two two three four eight', 'one two four five six seven eight', 'zero one two five six seven nine', 'zero six seven eight nine', 'zero one two two five six seven nine', 'two four six', 'zero one nine', 'four six', 'zero four five', 'zero two six', 'zero one five', 'zero one two five six nine', 'zero one two four five six seven eight nine', 'zero one four seven', 'zero zero one two four four nine', 'zero one five six', 'zero two five six seven nine', 'zero zero one one two four five six seven eight nine', 'zero one two two two five five six six seven nine', 'one', 'one two three four five seven eight nine', 'two seven', 'six seven eight nine', 'zero one five six seven', 'zero one one two four five six seven eight nine', 'zero two', 'zero one two four four', 'zero zero one four four five five seven', 'two two four five', 'zero one two six seven eight', 'two six nine', 'zero one one four five six nine', 'zero two two four five five six seven eight', 'zero two four four', 'zero two six', 'two three', 'zero one two two four five five six six seven nine', 'zero one two three three four five five six six nine', 'zero one eight nine', 'two four', 'zero one two four four five six seven eight nine', 'two two', 'one two five six seven nine', 'one two six nine', 'zero one four five six seven eight', 'four six seven nine', 'five six', 'zero one two four nine', 'zero one two four five six eight', 'zero one one four five nine', 'one two three four five six seven eight nine', 'one two three four five six seven eight nine', 'zero one two three four five six seven eight nine', 'zero one two three four five six seven eight nine', 'zero one two three four five six seven eight nine', 'zero one two three four five six seven eight nine', 'zero one two three four five six seven eight nine', 'zero one two three four five six seven eight nine', 'zero one two three four five six seven eight nine', 'zero one two three four five six seven eight nine', 'five', 'eight', 'zero two three four five six eight nine', 'one two three three', 'one two two three four five six seven seven eight nine nine', 'zero one two five six seven eight nine', 'zero one one two two three three four five five six seven eight nine', 'one two four five six seven eight nine', 'one one two four', 'one one one one one', 'one two', 'zero two two four four six nine', 'one two two three five six seven eight nine', 'one two seven eight nine', 'zero one three nine', 'eight nine', 'zero one three five seven', 'zero two three']
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(sort_numbers)