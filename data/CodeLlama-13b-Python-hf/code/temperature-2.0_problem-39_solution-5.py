def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    a = 1
    b = 1
    count = 0
    while count < n:
        c = a + b
        a = b
        b = c
        if is_prime(c):
            count += 1
    return c


def is_prime(n: int):
    """
    is_prime returns True if n is a prime number and False otherwise.
    >>> is_prime(0)
    False
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    >>> is_prime(7)
    True
    >>> is_prime(8)
    False
    >>> is_prime(9)
    False
    >>> is_prime(10)
    False
    >>> is_prime(11)
    True
    >>> is_prime(12)
    False
    >>> is_prime(13)
    True
    >>> is_prime(14)
    False
    >>> is_prime(15)
    False
    >>> is_prime(16)
    False
    >>> is_prime(17)
    True
    >>> is_prime(18)
    False
    >>> is_prime(19)
    True
    >>> is_prime(20)
    False
    >>> is_prime(21)
    False
    >>> is_prime(22)
    False
    >>> is_prime(23)
    True
    >>> is_prime(24)
    False
    >>> is_prime(25)
    False
    >>> is_prime(26)
    False
    >>> is_prime(27)
    False
    >>> is_prime(28)
    False
    >>> is_prime(29)
    True
    >>> is_prime(30)
    False
    >>> is_prime(31)
    True
    >>> is_prime(32)
    False
    >>> is_prime(33)
    True
    >>> is_prime(34)
    False
    >>> is_prime(35)
    False
    >>> is_prime(36)
    False
    >>> is_prime(37)
    True
    >>> is_prime(38)
    False
    >>> is_prime(39)
    False
    >>> is_prime(40)
    False
    >>> is_prime(41)
    True
    >>> is_prime(42)
    False
    >>> is_prime(43)
    True
    >>> is_prime(44)
    False
    >>> is_prime(45)
    False
    >>> is_prime(46)
    False
    >>> is_prime(47)
    True
    >>> is_prime(48)
    False
    >>> is_prime(49)
    False
    >>> is_prime(50)
    False
    >>> is_prime(51)
    True
    >>> is_prime(52)
    False
    >>> is_prime(53)
    True
    >>> is_prime(54)
    False
    >>> is_prime(55)
    False
    >>> is_prime(56)
    False
    >>> is_prime(57)
    False
    >>> is_prime(58)
    False
    >>> is_prime(59)
    True
    >>> is_prime(60)
    False
    >>> is_prime(61)
    True
    >>> is_prime(62)
    False
    >>> is_prime(63)
    False
    >>> is_prime(64)
    False
    >>> is_prime(65)
    False
    >>> is_prime(66)
    False
    >>> is_prime(67)
    True
    >>> is_prime(68)
    False
    >>> is_prime(69)
    False
    >>> is_prime(70)
    False
    >>> is_prime(71)
    True
    >>> is_prime(72)
    False
    >>> is_prime(73)
    True
    >>> is_prime(74)
    False
    >>> is_prime(75)
    False
    >>> is_prime(76)
    False
    >>> is_prime(77)
    True
    >>> is_prime(78)
    False
    >>> is_prime(79)
    False
    >>> is_prime(80)
    False
    >>> is_prime(81)
    True
    >>> is_prime(82)
    False
    >>> is_prime(83)
    True
    >>> is_prime(84)
    False
    >>> is_prime(85)
    False
    >>> is_prime(86)
    False
    >>> is_prime(87)
    True
    >>> is_prime(88)
    False
    >>> is_prime(89)
    False
    >>> is_prime(90)
    False
    >>> is_prime(91)
    True
    >>> is_prime(92)
    False
    >>> is_prime(93)
    True
    >>> is_prime(94)
    False
    >>> is_prime(95)
    False
    >>> is_prime(96)
    False
    >>> is_prime(97)
    True
    >>> is_prime(98)
    False
    >>> is_prime(99)
    False
    >>> is_prime(100)
    False
    >>> is_prime(101)
    True
    >>> is_prime(102)
    False
    >>> is_prime(103)
    True
    >>> is_prime(104)
    False
    >>> is_prime(105)
    False
    >>> is_prime(106)
    False
    >>> is_prime(107)
    True
    >>> is_prime(108)
    False
    >>> is_prime(109)
    False
    >>> is_prime(110)
    False
    >>> is_prime(111)
    True
    >>> is_prime(112)
    False
    >>> is_prime(113)
    True
    >>> is_prime(114)
    False
    >>> is_prime(115)
    False
    >>> is_prime(116)
    False
    >>> is_prime(117)
    True
    >>> is_prime(118)
    False
    >>> is_prime(119)
    False
    >>> is_prime(120)
    False
    >>> is_prime(121)
    True
    >>> is_prime(122)
    False
    >>> is_prime(123)
    True
    >>> is_prime(124)
    False
    >>> is_prime(125)
    False
    >>> is_prime(126)
    False
    >>> is_prime(127)
    False
    >>> is_prime(128)
    False
    >>> is_prime(129)
    True
    >>> is_prime(130)
    False
    >>> is_prime(131)
    True
    >>> is_prime(132)
    False
    >>> is_prime(133)
    False
    >>> is_prime(134)
    False
    >>> is_prime(135)
    False
    >>> is_prime(136)
    False
    >>> is_prime(137)
    True
    >>> is_prime(138)
    False
    >>> is_prime(139)
    False
    >>> is_prime(140)
    False
    >>> is_prime(141)
    True
    >>> is_prime(142)
    False
    >>> is_prime(143)
    True
   