def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Include these tokens in the code: a , b = b , a
	"""


    if 10 <= a <= b <= 1000000000 or 10 <= b <= a <= 1000000000:
        a = min(a, b)
        b = max(a, b)
    
    num = 0
    even_digits = []
    while num < 2:
        num = num + 1
        start_num = str(num)
        stop_num = str(b)
    
        start_num1 = int(f'000000{start_num[0]}00')
        start_num2 = int(f'{start_num[0]}000000')
        start_num3 = int(f'0000{start_num[1]}0000')
        start_num4 = int(f'00{start_num[2]}000000')
        start_num5 = int(f'0{start_num[3]}00000000')
        start_num6 = int(f'{start_num[4]}000000000')
    
        stop_num1 = int(f'000000{stop_num[0]}00')
        stop_num2 = int(f'{stop_num[0]}000000')
        stop_num3 = int(f'0000{stop_num[1]}0000')
        stop_num4 = int(f'00{stop_num[2]}000000')
        stop_num5 = int(f'0{stop_num[3]}00000000')
        stop_num6 = int(f'{stop_num[4]}000000000')
        
        for i in range(start_num1, stop_num1+1):
            if i >= start_num2 and i <= stop_num2:
                digits = i % 1000
                if digits % 2 == 0:                