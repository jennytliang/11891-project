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