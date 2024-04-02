def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    # A float represents the absolute difference
    if value[:1] == "-":
        int_value = int((float(value) - 0.1) // 1) # int = -5.8 = -6.0
        print(" - abs_value {} ".format(abs(value)))

    else:
        int_value = int(value + 0.5) # int = abs(-5.8 or 6.0) or 5 and 6
        raise NotImplementedError
    # value_from_zero is a list with the integer and the absolute_difference
    value_from_zero: list(int_number, abs_distance) = [int_value, abs(value -  int)]
    return int_value
############################################################ INITIAL TESTING ###############################
import pytest

@pytest.mark.parametrize('arg1, expected', [
    ('-2.7', -3), ('1', 1),
])
def test_closest_integer_1(arg1, expected):
    # test_case = {"abr": [2, [['1.5', '2.5'], ['-10', '-2.1']], True], "assertion": [-2, [['1.5'], ['-10']]], "position": [1], "message": "Expected -2." }
    # test case
    actual = closest_integer(arg1,)

    # testing the value
    # actual -> 1 actual value from method
    # expected or gold -> the excepted value from the method
    # assert < actual value or > <expected value > <error message>, < <position>

    # The pytest will stop and will print the reason why it happened and will show the line and method name too
    # the line of code is the one which is wrong from the function and show the exact part of the problem
    # if this not used then only error message is shown and you may not aware which one is wrong
    # if this assertion used then, you may correct the position and the value of that line from the method
    assert actual == expected, "TestCase failed for value: {}".format(arg1)

    return None



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
    inputs = [['10'], ['14.5'], ['-15.5'], ['15.3'], ['0'], ['-2.8'], ['3.6'], ['5.5'], ['-6.5'], ['0.5'], ['1.6'], ['-1.6'], ['0.0003'], ['99.99'], ['-99.99'], ['-99.9'], ['00'], ['999.99'], ['99.9999'], ['99.999'], ['9.999'], ['999.999'], ['000'], ['09.99900'], ['-999.99'], ['99.9'], ['-99'], ['-6.'], ['0900'], ['0000'], ['-6.00000'], ['6'], ['-999'], ['999'], ['11.6'], ['-6.00099900'], ['111.6'], ['00900'], ['-66.'], ['11.'], ['-9111.699'], ['-6.65'], ['5'], ['0009000'], ['-99.'], ['-9.'], ['-99000'], ['-5'], ['900.999'], ['911.600'], ['-66666.'], ['-9111.6919'], ['999.9999'], ['-090109111.6919'], ['-9111.19'], ['009090'], ['-6.000999006'], ['9999.99'], ['0009000000'], ['-91111.691'], ['999000.999'], ['-6.00'], ['-6.000999900'], ['-090109111.6919999'], ['-6.9096'], ['911'], ['-6.000000'], ['-666666.'], ['66666.'], ['9999.9999'], ['9.9'], ['1'], ['999.99999'], ['-699.990'], ['-66.6000'], ['9999'], ['00090000'], ['0099090'], ['00009000'], ['9'], ['-919'], ['000600'], ['-9900'], ['00090099990'], ['-6666666.'], ['.9096'], ['00090000000'], ['00600'], ['9.9999'], ['111.'], ['99'], ['00090000009.999000'], ['-6999.99000'], ['0.000'], ['000900'], ['-66666666.'], ['000900000000'], ['-9111191.691'], ['99990099090.99'], ['99999'], ['0090900'], ['-60.00099900'], ['-66966666.'], ['-111.900090099990900'], ['-54.9999'], ['0.0001'], ['12345678.54321'], ['-87654321.12345'], ['0.0000000009'], ['1.234567890000000001'], ['-1.234567890000000001'], ['-5.5'], ['1.2345678900040000001'], ['0.00000000009'], ['0.000000000009'], ['0.9'], ['-787654321.12345'], ['1.0001'], ['1.01'], ['-87654321.123345'], ['4.9999'], ['11'], ['10.2345678900000000001'], ['10.23456789000000000001'], ['1.0'], ['-187654321.123345'], ['1.'], ['-51.234567890000000001'], ['0.09'], ['-9'], ['-51.2354567890000000001'], ['0.'], ['1.001'], ['1.011'], ['-51.27890000000001'], ['5.55'], ['-91.01'], ['-87654321.212345'], ['-51.278900000000001'], ['10.234567890000000000091'], ['0.000000000000'], ['11.99'], ['55.5'], ['1.00001'], ['-51.278590000000001'], ['0.00000000'], ['1234567821'], ['111'], ['01'], ['-51.1234567890000000001'], ['11.9'], ['-5787654321.12345'], ['1.00'], ['1111'], ['00.0000000000000'], ['-599.5'], ['001'], ['00.00000000000000'], ['11111'], ['0.0000000010'], ['10.23456789000000000011101'], ['911.99'], ['10.23456789000000011111000091'], ['111111'], ['10.00001'], ['000.000000000000000'], ['-51.123456789001111100000001'], ['-91.'], ['00000000'], ['0.0000000000000'], ['10001'], ['-511.23545678900000500001'], ['-687654321.12345'], ['-578000000007654321.12345'], ['-51.1223456789001111100000001'], ['-5780000000076254321.162345'], ['-01.234567890000000001'], ['0.0'], ['000.00000000000000000'], ['-687654321.152345'], ['-5787.12345'], ['10.2345678900000001'], ['5.555'], ['1111.'], ['00.0001'], ['-54.99999'], ['1111111'], ['1.1001'], ['-51.2345678900000002001'], ['0.011111'], ['12534567821'], ['1.0000011'], ['9111.9900'], ['1000101'], ['12345678.521'], ['1.0111'], ['10.234567890000001'], ['555.5'], ['-51.20000000001'], ['101.234567890000001'], ['1.0099'], ['911001.99'], ['-787654321.12'], ['1.00111'], ['-54.999'], ['-191.01'], ['-5780007.12345'], ['-7876521.12345'], ['-599'], ['0010.234567890000000000091000000'], ['1.000001'], ['125345678221'], ['10.0000000010'], ['-687654321.122345'], ['-5780017.12345'], ['1.10001010'], ['100001'], ['111.9'], ['-51.12340001'], ['10.234567890000000001'], ['91000000'], ['99.99999'], ['10.21'], ['9911.99'], ['-051.278900000000001'], ['11100'], ['-5787.122345'], ['4.94999'], ['-051.123456789001111100000001'], ['10.234556789000000000011101'], ['1.1001010'], ['12534567'], ['000000000'], ['-511.235456789000005000001'], ['00.'], ['-51.2789000'], ['101'], ['0101'], ['125345678.521'], ['123456782101.2345678900000011'], ['654321.12345'], ['-6876542345'], ['0111111101'], ['-87654321.123485'], ['-0051.123456789001111100000001'], ['1.000011011'], ['-51.1234001'], ['-57008000000007654321.12345'], ['-5780000000076254654321.123452345'], ['11111111'], ['-876514321.212345'], ['9911.919'], ['-00.55'], ['94.9999'], ['-570080000000076543221.12345'], ['55'], ['000.0000000000000000'], ['-57817654321.12345'], ['1.00111100015'], ['-0000921.12345'], ['-5700800.12345'], ['00.000001'], ['111111111'], ['9100'], ['995'], ['-51.279989000'], ['-0.000000000099599'], ['10.2345567890000000000111091001'], ['10.000001'], ['-876543345'], ['10.234556789000000011101'], ['-5787.123345'], ['10.234567890001'], ['10.2345567189000000000011101'], ['0000.0000'], ['3231.12345'], ['601111111101345'], ['-876000.000000000000000543345'], ['94999'], ['00.000000000000011111'], ['1111111111'], ['0.1011111'], ['10.2345678900000011'], ['10.23456789000000001'], ['100011.0011110001501'], ['12345678.543211'], ['-55.5'], ['011'], ['-27890000000001'], ['0010.234567890000000601111111101345000091000000'], ['11.1011'], ['-87654'], ['-26876542345'], ['-9599.5'], ['0101.234567890000001'], ['109100'], ['-5787.123'], ['10.23000091'], ['990.001'], ['-87654321.1213485'], ['5125345678215'], ['111.10111'], ['111.5510111'], ['125345678221111'], ['9955'], ['-574321.12345'], ['-51.02789000'], ['-5.55'], ['-8761.0154'], ['1911.9925345678221'], ['-68765424345'], ['11.00001000'], ['-51.2785900000000001'], ['9995100'], ['123475678.521'], ['0.000000'], ['000.'], ['-59654321.12345'], ['-2687654245'], ['-278900000'], ['1000.00000000000000001111'], ['-26876540010.234567890000000010000002345'], ['-57101817654321.12345'], ['5.5125345678215555'], ['1000012345678.5432111'], ['-51.1234567890011111000000'], ['4.994999'], ['1.00111101'], ['494.9999'], ['94.99999'], ['654321.123345'], ['.12345'], ['-9999955'], ['-57121.12345'], ['-99999955'], ['-51.23456789000000002001'], ['654321.122345'], ['-51234567820.10111111'], ['111.1'], ['-57121.125345'], ['604555.55'], ['000.0001253456700000000000000'], ['-151.0279000'], ['1001'], ['10.001'], ['-9999995'], ['0010.2345678900000000091000000'], ['00125345678.521000000'], ['-8769955543345'], ['10.2300'], ['-99999995'], ['-51.12314567890011111000500001'], ['0000.'], ['1100010.234567890001'], ['0.0111011'], ['-00009121.12345'], ['5.5551'], ['-51.1234567890011511100000001'], ['11001'], ['10.234569100000078900000000001'], ['99501015'], ['0000.00000'], ['-51.27859000000001'], ['-268555.576542345'], ['10.234100015678900000011'], ['1111.5510111'], ['-0.00000099599'], ['00000.0000'], ['-.27859000000001'], ['-154.949990'], ['1.0011110'], ['1000.000125345670000000000000011111'], ['12345678.5251'], ['1100010.2934567890001'], ['1111.11011'], ['5.51253345678215555'], ['94.99991111119'], ['111.511'], ['0.00000099550009'], ['00.00001'], ['-876543211001.123345'], ['99.001'], ['0.011'], ['110.00001'], ['0.0000000000099'], ['10001011'], ['0.00000000010'], ['-51.202789000'], ['12345678.5431'], ['111001'], ['10.230'], ['-91.011'], ['1911.99253452678221'], ['-51.2729989000'], ['110010.9'], ['9911.999'], ['11.000001000'], ['9911999'], ['6045555.55'], ['01111111101'], ['-51.2789000000001'], ['-9991.011'], ['0.0000000'], ['-187654321.1345'], ['-268765410.000001245'], ['1000101.0011110001501'], ['10.2341006015678900000011'], ['1253456782211111.0'], ['9499'], ['5123475678.521'], ['19111.99253452678221'], ['10.12345678900000000001'], ['1111.50111'], ['-876514321.21234'], ['789000001.123345'], ['-051.02789000'], ['-2687654235'], ['10011'], ['9911.9999'], ['-5787.1233'], ['1909100'], ['-51.23001'], ['1000.000000000000000001111'], ['.011'], ['-51.027890000'], ['-268765421.0000145'], ['-999.011'], ['100.001'], ['-999999955'], ['0.000000000000000000000000000000000000000000000000000000000000000000000000000001'], ['1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'], ['-1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'], ['-0.000000000000000000000000000000000000000000000000000000000000000000000000000000001'], ['-0'], ['-0.5'], ['9999999999999999999999999999999999999999999999999999999999999.5'], ['-9999999999999999999999999999999999999999999999999999999999999.5'], ['0.00001'], ['-1.23405678900000000001'], ['-8761.12345'], ['-1.2034567890000000001'], ['-454.9999'], ['1.2345607890000000001'], ['-1.201345678900000000001'], ['-1.2013456789000000000001'], ['-876544321.12345'], ['1.2345678900000000001'], ['-876654321.12345'], ['-1.20134560789000000000001'], ['1.23456078900000000001'], ['-8765421.12345'], ['-2345'], ['-234'], ['-1.2345607890000000001'], ['0.000001'], ['-87654432.12345'], ['-1'], ['-1.20134567890000000000001'], ['-54.9'], ['-454.59999'], ['-1.234056789000000000001'], ['-1.20134567899000000000001'], ['-1.2013945678900000000001'], ['-1.20345672890000000001'], ['12678.54321'], ['-1.234055670001'], ['.5'], ['-24345'], ['12678.254321'], ['12678.543251'], ['-2334'], ['-23'], ['-1.2340567890000000001'], ['-87565421.12345'], ['-1.20304567890000000001'], ['-1.2034567890001'], ['-1.201345678900000000000091'], ['-243545'], ['-11.234055670001'], ['1.230456789000000001'], ['-1.230304567890000000001'], ['-21.23456789000000000013'], ['-1.201394567890000001'], ['-1.20134567899000000000'], ['-454.'], ['-1.23405567000'], ['-1.203045678900000000901'], ['00.0000000009'], ['-1.203456728900000000401'], ['-234523'], ['126784.2544321'], ['-1.234560789000000000010000000001'], ['-41.20134560789000000000001'], ['-245'], ['-23412345678.54321'], ['-2344'], ['1.237890000000001'], ['9999.99999'], ['-2234'], ['-87654321.121345'], ['1.234560789000000000091'], ['000001'], ['-1.2013456780900000000001'], ['000000'], ['-1.2013456078900000300'], ['00.00000000009'], ['-1.2303045678900000000001'], ['-875654221.12345'], ['12678.5432'], ['-2435545'], ['0.0000001'], ['-22234'], ['-1.2345607890000000000100000700001'], ['-1.2303045067890000000001'], ['-1.23456078900100000000100000700001'], ['-222324'], ['-1.20134567809000000000001'], ['-1.230304501'], ['-2'], ['-1.2030456708900000000901'], ['-8235412345678.5'], ['-87654321.123450000000'], ['-876654321.125345'], ['-2312678.54325134'], ['-1.2345678900000050001'], ['123456678.54321'], ['-1.23405670001'], ['-1.203456724890000000001'], ['-1.201345678900000000000000000001'], ['-2223224'], ['99999.99999'], ['-200.00000000009'], ['-24'], ['-1.23400000000000001'], ['-87654321.1213435'], ['999999999'], ['-8745'], ['-23434'], ['-22324'], ['-323'], ['-22434'], ['-1.20139456789000000050001'], ['0.000000009009'], ['-541.234567890000000000199999'], ['-8745654221.12345'], ['00005'], ['-2312678.543251334'], ['-24512345678.54321'], ['999999.99999'], ['-10.00001'], ['-1.201'], ['123456678.543221'], ['-1.23456078900000050001'], ['-8235412345678.25'], ['-22'], ['99.999999'], ['-31.2303045067890000000001'], ['999999.999999'], ['00999.999990001'], ['-1.20131'], ['1.234560789000000000001'], ['-87654432.1234'], ['1.2345607890000000000091'], ['1234566678.543221'], ['-87654432.212345'], ['-1.234056711'], ['-299.9999992434'], ['-1.23030450678900000030001'], ['-1.23456078900000000001'], ['-454.59'], ['-1.2034567289000200000401'], ['-1.234105678900000000001'], ['-5.555'], ['-87654321.12145'], ['-877654321.12345'], ['-2434123456738.54321'], ['39456789009000000001'], ['-1.201345670809000000000001'], ['-11.201'], ['-224'], ['-544.95999'], ['-1.2101'], ['-1.2013456708090008000000001'], ['-243554500'], ['-876754321.12134335'], ['-5944.95999'], ['1.23456078900000000000091'], ['000.00000000009'], ['-41.0000001'], ['1.234560578900000000001'], ['-87456542121.12345'], ['-24341'], ['1.234560789000000000000091'], ['-1.23030567890000000001'], ['1.2345060578900000000001'], ['-1.2013435678900000000001'], ['-1.230305678890000000001'], ['1.234500000'], ['-1.23900000000001'], ['-875654221.123445'], ['-1.2341050678900000000001'], ['-8890090000000013435'], ['-1.201394567890'], ['-1.2021345678900000000000000000001'], ['1.23457890000000001'], ['-1.2034567289'], ['-876543211.121345'], ['1.23435678900000000001'], ['-1.230405670001'], ['-5000054.99999'], ['-872654321.121345'], ['-1.203456728890000000001'], ['-1.2013645678900000000001'], ['-88990090000000013435'], ['-2222324'], ['-5941.23450000095999'], ['1.2304567890000000901'], ['-13.234056789000000000001'], ['01.23456078900000000'], ['-45554.59'], ['12678.85432'], ['-2312678.5432511334'], ['-1.20345678900000000001'], ['-88900900080000013435'], ['-2424345'], ['-1.2134560789000000000010000000001'], ['0000000'], ['000001.234560789000000000000911'], ['-454.99'], ['-1.23456001'], ['-871.12345'], ['1.234560789000001'], ['-1.234560789001000000001000007600001'], ['-1.23030456789000000001'], ['-8765421.122345'], ['-1.201345678909000000000001'], ['-812345'], ['-1.203045607890000000001'], ['-8776654321.12345'], ['-594.9999'], ['3456789000000000001'], ['-001'], ['-594.9'], ['-876654321.142345'], ['-2435544500'], ['-1.23456078900000001'], ['9999999'], ['-871.125'], ['-21.234567890000000003'], ['-24355450099.9999'], ['-8765443241.12345'], ['-8766543821.142345'], ['-1.2013456789000000000000091'], ['-5944.959999'], ['1.2345300000'], ['-11.2343055670001'], ['-1.2034560728900000000401'], ['61.23435678900000000001'], ['-1.20134569078900000300'], ['-1.2034567248900005000001'], ['999999'], ['-0304567089000000901'], ['-234123455678.54321'], ['-1.20345672890000000000001'], ['012678.543210'], ['-1.203456789000000100001'], ['-1.2034567248900000000001'], ['00.000000000009'], ['-455554.59'], ['-876654342345'], ['-29999934'], ['-244'], ['-11.234305567004301'], ['-1.234000000000000001'], ['-876543211.1215'], ['-1.201394567890000000000'], ['0.00000010001'], ['-1.201394567890000000050001'], ['-23126578.54325134'], ['1234566178.54321'], ['-1.2013945678900000000050001'], ['1234566781.543221'], ['-5944.995999'], ['0000000001.2345607890000000001'], ['991.23453000009999999'], ['-000052'], ['4512345678.54321'], ['-82354123645'], ['1.23045678900000901'], ['-594.99949'], ['-10.0000'], ['-23126781.543251334'], ['-1.2013456789090000000900001'], ['-1.23141050678900000000001'], ['-45.59'], ['54.9'], ['00000'], ['-1.2011'], ['-234123456728.54321'], ['-22312678.543251334'], ['-5954.9999'], ['0.0009'], ['-991.23453000009999999001'], ['-1.21345607890000000000100000000011'], ['-1.201345670809000000000999999001'], ['100901'], ['1.2304567890000000001'], ['1.23400091'], ['123456378.54321'], ['-1.203045670890000000001'], ['-1.2013456750809000000000001'], ['-1.2034567890'], ['-1.2034567289000000000401'], ['-1.2345678900000000001']]
    results = [10, 15, -16, 15, 0, -3, 4, 6, -7, 1, 2, -2, 0, 100, -100, -100, 0, 1000, 100, 100, 10, 1000, 0, 10, -1000, 100, -99, -6, 900, 0, -6, 6, -999, 999, 12, -6, 112, 900, -66, 11, -9112, -7, 5, 9000, -99, -9, -99000, -5, 901, 912, -66666, -9112, 1000, -90109112, -9111, 9090, -6, 10000, 9000000, -91112, 999001, -6, -6, -90109112, -7, 911, -6, -666666, 66666, 10000, 10, 1, 1000, -700, -67, 9999, 90000, 99090, 9000, 9, -919, 600, -9900, 90099990, -6666666, 1, 90000000, 600, 10, 111, 99, 90000010, -7000, 0, 900, -66666666, 900000000, -9111192, 99990099091, 99999, 90900, -60, -66966666, -112, -55, 0, 12345679, -87654321, 0, 1, -1, -6, 1, 0, 0, 1, -787654321, 1, 1, -87654321, 5, 11, 10, 10, 1, -187654321, 1, -51, 0, -9, -51, 0, 1, 1, -51, 6, -91, -87654321, -51, 10, 0, 12, 56, 1, -51, 0, 1234567821, 111, 1, -51, 12, -5787654321, 1, 1111, 0, -600, 1, 0, 11111, 0, 10, 912, 10, 111111, 10, 0, -51, -91, 0, 0, 10001, -511, -687654321, -578000000007654272, -51, -5780000000076254208, -1, 0, 0, -687654321, -5787, 10, 6, 1111, 0, -55, 1111111, 1, -51, 0, 12534567821, 1, 9112, 1000101, 12345679, 1, 10, 556, -51, 101, 1, 911002, -787654321, 1, -55, -191, -5780007, -7876521, -599, 10, 1, 125345678221, 10, -687654321, -5780017, 1, 100001, 112, -51, 10, 91000000, 100, 10, 9912, -51, 11100, -5787, 5, -51, 10, 1, 12534567, 0, -511, 0, -51, 101, 101, 125345679, 123456782101, 654321, -6876542345, 111111101, -87654321, -51, 1, -51, -57008000000007651328, -5780000000076254543872, 11111111, -876514321, 9912, -1, 95, -570080000000076546048, 55, 0, -57817654321, 1, -921, -5700800, 0, 111111111, 9100, 995, -51, 0, 10, 10, -876543345, 10, -5787, 10, 10, 0, 3231, 601111111101345, -876000, 94999, 0, 1111111111, 0, 10, 10, 100011, 12345679, -56, 11, -27890000000001, 10, 11, -87654, -26876542345, -9600, 101, 109100, -5787, 10, 990, -87654321, 5125345678215, 111, 112, 125345678221111, 9955, -574321, -51, -6, -8761, 1912, -68765424345, 11, -51, 9995100, 123475679, 0, 0, -59654321, -2687654245, -278900000, 1000, -26876540010, -57101817654321, 6, 1000012345679, -51, 5, 1, 495, 95, 654321, 0, -9999955, -57121, -99999955, -51, 654321, -51234567820, 111, -57121, 604556, 0, -151, 1001, 10, -9999995, 10, 125345679, -8769955543345, 10, -99999995, -51, 0, 1100010, 0, -9121, 6, -51, 11001, 10, 99501015, 0, -51, -268556, 10, 1112, 0, 0, 0, -155, 1, 1000, 12345679, 1100010, 1111, 6, 95, 112, 0, 0, -876543211001, 99, 0, 110, 0, 10001011, 0, -51, 12345679, 111001, 10, -91, 1912, -51, 110011, 9912, 11, 9911999, 6045556, 1111111101, -51, -9991, 0, -187654321, -268765410, 1000101, 10, 1253456782211111, 9499, 5123475679, 19112, 10, 1112, -876514321, 789000001, -51, -2687654235, 10011, 9912, -5787, 1909100, -51, 1000, 0, -51, -268765421, -999, 100, -999999955, 0, 1000000000000000049861653971908893017010268485438462151574892930611988399099305815384459015356416, -1000000000000000049861653971908893017010268485438462151574892930611988399099305815384459015356416, 0, 0, -1, 9999999999999999493871352970740188669636450110134100730839040, -9999999999999999493871352970740188669636450110134100730839040, 0, -1, -8761, -1, -455, 1, -1, -1, -876544321, 1, -876654321, -1, 1, -8765421, -2345, -234, -1, 0, -87654432, -1, -1, -55, -455, -1, -1, -1, -1, 12679, -1, 1, -24345, 12678, 12679, -2334, -23, -1, -87565421, -1, -1, -1, -243545, -11, 1, -1, -21, -1, -1, -454, -1, -1, 0, -1, -234523, 126784, -1, -41, -245, -23412345679, -2344, 1, 10000, -2234, -87654321, 1, 1, -1, 0, -1, 0, -1, -875654221, 12679, -2435545, 0, -22234, -1, -1, -1, -222324, -1, -1, -2, -1, -8235412345679, -87654321, -876654321, -2312679, -1, 123456679, -1, -1, -1, -2223224, 100000, -200, -24, -1, -87654321, 999999999, -8745, -23434, -22324, -323, -22434, -1, 0, -541, -8745654221, 5, -2312679, -24512345679, 1000000, -10, -1, 123456679, -1, -8235412345678, -22, 100, -31, 1000000, 1000, -1, 1, -87654432, 1, 1234566679, -87654432, -1, -300, -1, -1, -455, -1, -1, -6, -87654321, -877654321, -2434123456739, 39456789008999997440, -1, -11, -224, -545, -1, -1, -243554500, -876754321, -5945, 1, 0, -41, 1, -87456542121, -24341, 1, -1, 1, -1, -1, 1, -1, -875654221, -1, -8890090000000013312, -1, -1, 1, -1, -876543211, 1, -1, -5000055, -872654321, -1, -1, -88990090000000008192, -2222324, -5941, 1, -13, 1, -45555, 12679, -2312679, -1, -88900900080000008192, -2424345, -1, 0, 1, -455, -1, -871, 1, -1, -1, -8765421, -1, -812345, -1, -8776654321, -595, 3456789000000000000, -1, -595, -876654321, -2435544500, -1, 9999999, -871, -21, -24355450100, -8765443241, -8766543821, -1, -5945, 1, -11, -1, 61, -1, -1, 999999, -304567089000000896, -234123455679, -1, 12679, -1, -1, 0, -455555, -876654342345, -29999934, -244, -11, -1, -876543211, -1, 0, -1, -23126579, 1234566179, -1, 1234566782, -5945, 1, 991, -52, 4512345679, -82354123645, 1, -595, -10, -23126782, -1, -1, -46, 55, 0, -1, -234123456729, -22312679, -5955, 0, -991, -1, -1, 100901, 1, 1, 123456379, -1, -1, -1, -1, -1]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(closest_integer)