def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    ans = 1
    while n > 0:
        d = str(n)[0]
        n /= 10
        if str(n)[0] == d:
            ans *= int(d)
    return ans        




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
    inputs = [[5], [54], [120], [5014], [98765], [5576543], [2468], [951], [246], [135797531], [888], [182135], [703], [999], [111], [1001], [3], [952], [889], [998], [2], [182136], [25], [701], [4], [24], [997], [247], [6], [953], [135797532], [7], [248], [23], [996], [135797533], [995], [994], [891], [26], [8], [112], [22], [950], [702], [1000], [704], [182137], [893], [993], [135797534], [135797535], [245], [249], [9], [244], [890], [47], [992], [700], [135797530], [705], [243], [27], [182134], [887], [46], [894], [699], [45], [707], [892], [182138], [182139], [1002], [113], [1], [88], [706], [250], [110], [949], [698], [242], [11], [135797529], [1003], [109], [135797536], [182133], [43], [135797538], [241], [71], [114], [28], [135797539], [10], [89], [954], [240], [44], [886], [115], [70], [991], [323456789101112131415161718192021222324252627282930313233343536], [182937457814614279640075438629345987263878749129823578184719333882443], [8843924584737538929273870549395092387583092748327447402387489518947358439582352948], [124834738571930288374895092375830274843252127479238048384758941827309258429539458173975894729347584], [3902482539585903843732859374089573948579380957409378540930757943758435987234095873947598343], [13579], [123456789], [945], [1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253], [182937457814614279640075438629345987263878749129823578184719333882442], [182937457814614279640075438629345987263878749129823578184719333882444], [123456788], [123456787], [944], [124834738571930288374895092375830274843252127479238048384758941827309258429539458173975894729347585], [124834738571930288374895092375830274843252127479238048384758941827309258429539458173975894729347583], [1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515254], [3902482539585903843732859374089573948579380957409378540930757943758435987234095873947598344], [323456789101112131415161718192021222324252627282930313233343535], [1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515252], [3902482539585903843732859374089573948579380957409378540930757943758435987234095873947598342], [182937457814614279640075438629345987263878749129823578184719333882441], [182937457814614279640075438629345987263878749129823578184719333882445], [943], [1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515251], [8843924584737538929273870549395092387583092748327447402387489518947358439582352947], [323456789101112131415161718192021222324252627282930313233343537], [323456789101112131415161718192021222324252627282930313233343534], [124834738571930288374895092375830274843252127479238048384758941827309258429539458173975894729347587], [323456789101112131415161718192021222324252627282930313233343538], [124834738571930288374895092375830274843252127479238048384758941827309258429539458173975894729347586], [182937457814614279640075438629345987263878749129823578184719333882446], [942], [182937457814614279640075438629345987263878749129823578184719333882448], [124834738571930288374895092375830274843252127479238048384758941827309258429539458173975894729347582], [182937457814614279640075438629345987263878749129823578184719333882447], [941], [124834738571930288374895092375830274843252127479238048384758941827309258429539458173975894729347581], [8843924584737538929273870549395092387583092748327447402387489518947358439582352946], [3902482539585903843732859374089573948579380957409378540930757943758435987234095873947598341], [123456786], [8843924584737538929273870549395092387583092748327447402387489518947358439582352949], [13578], [1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515255], [1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515256], [8843924584737538929273870549395092387583092748327447402387489518947358439582352945], [3902482539585903843732859374089573948579380957409378540930757943758435987234095873947598346], [8843924584737538929273870549395092387583092748327447402387489518947358439582352944], [8843924584737538929273870549395092387583092748327447402387489518947358439582352950], [53], [940], [52], [182937457814614279640075438629345987263878749129823578184719333882440], [1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515257], [1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515250], [946], [73], [947], [182937457814614279640075438629345987263878749129823578184719333882449], [55], [3902482539585903843732859374089573948579380957409378540930757943758435987234095873947598340], [323456789101112131415161718192021222324252627282930313233343539], [16], [69], [15], [13577], [3902482539585903843732859374089573948579380957409378540930757943758435987234095873947598345], [3902482539585903843732859374089573948579380957409378540930757943758435987234095873947598347], [30], [124834738571930288374895092375830274843252127479238048384758941827309258429539458173975894729347588], [74], [64], [1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515249], [1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515258], [72], [17], [8843924584737538929273870549395092387583092748327447402387489518947358439582352951], [14], [51], [95], [94], [123456785], [57], [8843924584737538929273870549395092387583092748327447402387489518947358439582352943], [32], [65], [62], [68], [182937457814614279640075438629345987263878749129823578184719333882439], [123456784], [18], [33], [323456789101112131415161718192021222324252627282930313233343533], [96], [76], [124834738571930288374895092375830274843252127479238048384758941827309258429539458173975894729347589], [948], [75], [13580], [13], [182937457814614279640075438629345987263878749129823578184719333882450], [123456783], [1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515248], [100], [11111111111111111111], [22222222222], [333333333333], [13581], [123456790], [3902482539585903843732859374089573948579380957409378540930757943758435987234095873947598348], [3902482539585903843732859374089573948579380957409378540930757943758435987234095873947598349], [13576], [8843924584737538929273870549395092387583092748327447402387489518947358439582352942], [8843924584737538929273870549395092387583092748327447402387489518947358439582352941], [13582], [8843924584737538929273870549395092387583092748327447402387489518947358439582352940], [123456791], [8843924584737538929273870549395092387583092748327447402387489518947358439582352939], [323456789101112131415161718192021222324252627282930313233343532], [13583], [8843924584737538929273870549395092387583092748327447402387489518947358439582352938], [21], [49], [20], [13585], [123456792], [323456789101112131415161718192021222324252627282930313233343531], [99], [48]]
    results = [5, 5, 1, 5, 315, 2625, 0, 45, 0, 99225, 0, 15, 21, 729, 1, 1, 3, 45, 9, 81, 0, 3, 5, 7, 0, 0, 567, 7, 0, 135, 99225, 7, 0, 3, 81, 297675, 405, 81, 9, 0, 0, 1, 0, 45, 7, 1, 7, 21, 27, 243, 99225, 496125, 5, 9, 9, 0, 9, 7, 81, 7, 99225, 35, 3, 7, 3, 7, 0, 9, 81, 5, 49, 9, 3, 27, 1, 3, 1, 0, 7, 5, 1, 81, 9, 0, 1, 297675, 3, 9, 99225, 9, 3, 99225, 1, 7, 1, 0, 893025, 1, 9, 45, 0, 0, 0, 5, 7, 81, 83053267329375, 2374385525072174368125, 9200959088342885342286486328125, 47338934509524145086063972158203125, 149749111277833459456445972784093017578125, 945, 945, 45, 83439724563916998046875, 791461841690724789375, 791461841690724789375, 105, 735, 9, 236694672547620725430319860791015625, 142016803528572435258191916474609375, 27813241521305666015625, 49916370425944486485481990928031005859375, 415266336646875, 27813241521305666015625, 49916370425944486485481990928031005859375, 791461841690724789375, 3957309208453623946875, 27, 27813241521305666015625, 64406713618400197396005404296875, 581372871305625, 83053267329375, 331372541566669015602447805107421875, 83053267329375, 47338934509524145086063972158203125, 791461841690724789375, 9, 791461841690724789375, 47338934509524145086063972158203125, 5540232891835073525625, 9, 47338934509524145086063972158203125, 9200959088342885342286486328125, 49916370425944486485481990928031005859375, 105, 82808631795085968080578376953125, 105, 139066207606528330078125, 27813241521305666015625, 46004795441714426711432431640625, 49916370425944486485481990928031005859375, 9200959088342885342286486328125, 46004795441714426711432431640625, 15, 9, 5, 791461841690724789375, 194692690649139662109375, 27813241521305666015625, 9, 21, 63, 7123156575216523104375, 25, 49916370425944486485481990928031005859375, 747479405964375, 1, 9, 5, 735, 249581852129722432427409954640155029296875, 349414592981611405398373936496217041015625, 3, 47338934509524145086063972158203125, 7, 0, 50063834738350198828125, 27813241521305666015625, 7, 7, 46004795441714426711432431640625, 1, 5, 45, 9, 525, 35, 27602877265028656026859458984375, 3, 5, 0, 0, 21369469725649569313125, 105, 1, 9, 249159801988125, 9, 7, 426050410585717305774575749423828125, 9, 35, 15, 3, 3957309208453623946875, 315, 5562648304261133203125, 1, 1, 0, 531441, 15, 945, 49916370425944486485481990928031005859375, 449247333833500378369337918352279052734375, 105, 9200959088342885342286486328125, 9200959088342885342286486328125, 15, 9200959088342885342286486328125, 945, 248425895385257904241735130859375, 83053267329375, 45, 27602877265028656026859458984375, 1, 9, 0, 75, 945, 83053267329375, 81, 0]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(digits)