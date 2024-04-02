def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """

    def string_to_integer(fraction):
        n = fraction.split('/')
        return int(n[0]) / int(n[1])
    
    return str(string_to_integer(x) * string_to_integer(n)).endswith('.0')



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
    inputs = [['1/5', '5/1'], ['1/6', '2/1'], ['5/1', '3/1'], ['7/10', '10/2'], ['2/10', '50/10'], ['7/2', '4/2'], ['11/6', '6/1'], ['2/3', '5/2'], ['5/2', '3/5'], ['2/4', '8/4'], ['2/4', '4/2'], ['1/5', '1/5'], ['3/4', '4/3'], ['6/8', '3/4'], ['1/6', '6/1'], ['2/3', '3/2'], ['9/12', '12/9'], ['15/17', '17/15'], ['8/11', '11/8'], ['13/19', '19/13'], ['20/25', '25/20'], ['3/8', '8/3'], ['17/15', '15/117'], ['12/9', '17/15'], ['6/8', '33/4'], ['12/9', '112/9'], ['616/6', '6/1'], ['12/9', '12/9'], ['205/25', '20/25'], ['98/3', '19/13'], ['12/9', '13/19'], ['9/12', '9/12'], ['3/2', '2/3'], ['13/19', '17/15'], ['133/19', '13/19'], ['3/2', '3/2'], ['119/13', '119/13'], ['205/25', '112/9'], ['2/3', '2/3'], ['1319/13', '119/13'], ['119/13', '1319/13'], ['133/19', '616/6'], ['8/3', '3/8'], ['4/3', '19/13'], ['15/17', '3/2'], ['1112/9', '112/9'], ['225/20', '19/13'], ['119/1', '119/1'], ['23/2', '3/2'], ['68/8', '33/4'], ['13/199', '13/19'], ['2055/25', '112/9'], ['33/4', '33/4'], ['8/3', '33/2'], ['4/3', '17/15'], ['15/117', '15/117'], ['6/1', '17/15'], ['3/19', '13/19'], ['133/19', '133/19'], ['3/88', '3/8'], ['3/8', '83/3'], ['15/17', '112/9'], ['20/25', '112/9'], ['112/9', '205/225'], ['2055/25', '205/25'], ['133/19', '19/13'], ['15/117', '3/2'], ['19/13', '19/13'], ['6/8', '3/88'], ['933/4', '9/12'], ['13/1999', '13/19'], ['19/13', '19/3'], ['8/1', '8/11'], ['23/2', '616/6'], ['17/15', '15/1117'], ['15/117', '17/15'], ['119/1', '4/3'], ['8/811', '11/8'], ['33/44', '33/44'], ['1119/1', '119/1'], ['17/15', '6/8'], ['33/4', '33/34'], ['1112/9', '1112/9'], ['13/19', '3/119'], ['2/3', '22/3'], ['1/6', '1/6'], ['8/3', '8/3'], ['2225/20', '2225/20'], ['2055/25', '22/3'], ['25/20', '1199/1'], ['13/1999', '12/9'], ['119/13', '1119/13'], ['1333/19', '133/19'], ['3/88', '33/8'], ['1119/1', '4/3'], ['13/19', '13/19'], ['3/888', '3/888'], ['15/1117', '15/117'], ['13/199', '17/15'], ['33/34', '3/22'], ['3/119', '13/19'], ['13/1999', '13/1999'], ['1119/1', '1119/1'], ['61612/9', '6/6'], ['3/4', '8/3'], ['1199/1', '1199/1'], ['199/13', '19/313'], ['19/3', '19/13'], ['1119/13', '1119/13'], ['1333/19', '133/1'], ['1333/19', '1333/19'], ['25/20', '8/3'], ['2/3', '8/13'], ['23/52', '16/17'], ['11/7', '13/77'], ['99/100', '11/9'], ['3/8', '7/25'], ['467/736', '453/384'], ['37/55', '176/9'], ['597/275', '380/241'], ['943/29', '163/58'], ['857/291', '921/739'], ['468/136', '453/384'], ['3/8', '3/8'], ['921/739', '921/739'], ['111/7', '13/77'], ['7/25', '7/25'], ['467/736', '857/291'], ['176/17', '8/13'], ['453/384', '453/384'], ['176/17', '3/8'], ['163/58', '857/291'], ['943/29', '453/384'], ['5597/275775', '380/241'], ['23/52', '23/52'], ['11/9', '453/384'], ['467/736', '11/9'], ['467/736', '467/736'], ['467/736', '5597/275775'], ['4553/384', '453/384'], ['5597/275775', '163/58'], ['857/29', '921/739'], ['11/9', '176/17'], ['11/9', '5597/275775'], ['3/8', '13/77'], ['111/7', '176/669'], ['11/9', '176/9'], ['467/7636', '467/7636'], ['5597/2757775', '163/58'], ['9231/739', '921/739'], ['6467/736', '468/136'], ['5597/2757775', '176/669'], ['111/7', '111/7'], ['11/9', '453/3384'], ['3/8', '943/29'], ['11/7', '943/29'], ['11/99', '453/3384'], ['163/58', '163/58'], ['380/241', '380/241'], ['453/384', '1111/7'], ['1111/7', '11/7'], ['9943/29', '163/58'], ['4553/384', '453/38'], ['111/7', '468/136'], ['23/52', '380/241'], ['11/7', '11/7'], ['857/291', '857/291'], ['11/99', '4453/3844'], ['453/384', '7/25'], ['453/3384', '163/58'], ['176/17', '176/17'], ['5597/2757775', '857/291'], ['453/38', '3/8'], ['11/99', '44534/3844'], ['453/3384', '9943/29'], ['9943/29', '11/99'], ['453/38', '13/77'], ['13/77', '13/77'], ['92331/739', '92331/739'], ['1111/7', '3/8'], ['8/3', '8/13'], ['597/275', '597/275'], ['173/77', '173/77'], ['5597/2757775', '467/736'], ['467/7636', '3/8'], ['11/99', '921/739'], ['111/7', '467/736'], ['11/9', '11/9'], ['467/736', '4767/736'], ['3/8', '163/58'], ['921/739', '468/136'], ['3/8', '3/88'], ['9943/29', '4553/384'], ['857/291', '4453/3844'], ['468/136', '468/136'], ['380/241', '9943/29'], ['8/3', '468/136'], ['467/736', '467/7736'], ['467/7736', '467/7736'], ['380/241', '468/136'], ['468/136', '2/3'], ['9943/29', '13/77'], ['5597/2757775', '8579/291'], ['2/3', '453/38'], ['7/2', '597/275'], ['467/7636', '11/9'], ['37/55', '453/38'], ['37/55', '37/55'], ['7/25', '3/8'], ['176/669', '8/13'], ['1111/7', '13/77'], ['9943/29', '8/13'], ['999/100', '11/9'], ['1111/7', '83/8'], ['453/38', '4677/7736'], ['8/3', '468/6'], ['3080/24', '3080/241'], ['8468/6', '468/6'], ['4677/7736', '468/136'], ['173/77', '37/55'], ['45353/3', '4553/3'], ['9943/29', '11/9'], ['111/7', '1111/7'], ['5597/2757775', '161111/78'], ['467/736', '111/9'], ['467/736', '9943/29'], ['176/9', '11/9'], ['9231/739', '176/669'], ['9943/29', '453/38'], ['4674/7436', '4674/7436'], ['921/739', '468/6'], ['7/2', '999/100'], ['9999/0100', '11/9'], ['48468/636', '857/291'], ['467/7736', '16/17'], ['23/51217', '176/17'], ['453/3384', '453/3384'], ['8/3', '5597/2755775'], ['467/736', '47677/736'], ['4674/7436', '4453/3844'], ['453/384', '453/38'], ['453353/3', '45535/3'], ['163/58', '3/8'], ['6467/736', '11/9'], ['5597/2755775', '380/241'], ['3080/241', '453/384'], ['9231/739', '45535/3'], ['5597/2757775', '597/275'], ['92331/739', '468/136'], ['8857/291', '857/291'], ['233/52', '380/241'], ['1111/7', '1111/7'], ['9231/739', '5597/2755775'], ['9943/29', '191/99'], ['4767/736', '16/17'], ['9231/739', '9231/739'], ['453/38', '3080/24'], ['4688/136', '468/136'], ['4688/1386', '468/136'], ['1653/58', '857/291'], ['857/291', '453/3384'], ['3080/241', '3080/241'], ['111/99', '921/739'], ['921/739', '467/736'], ['7/2', '4677/7736'], ['4367/736', '4367/736'], ['468/336', '111/9'], ['453/38', '453/38'], ['233/52', '4367/736'], ['857/29', '857/29'], ['4/136', '468/136'], ['5597/25757775', '5597/2757775'], ['467/736', '11/19'], ['857/291', '45535/3'], ['1111/7', '468/136'], ['4367/736', '233/52'], ['467/7636', '176/669'], ['3/8', '9231/739'], ['33/8', '13/77'], ['8/13', '13/77'], ['453/38', '8/13'], ['4674/74436', '46674/7436'], ['111/17', '111/7'], ['4553/384', '233/52'], ['5597/275775', '1653/58'], ['30802/24', '3080/241'], ['467/77636', '467/77636'], ['37/55', '3/8'], ['3/8', '11/7'], ['111/17', '11/99'], ['1111/7', '5597/2757775'], ['111/9', '11/9'], ['83/8', '163/58'], ['4367/736', '83/8'], ['453/338436', '468/136'], ['8453/384', '8453/384'], ['30802/24', '467/736'], ['5597/2757775', '5597/2757775'], ['11/7', '4677/7736'], ['453/38', '33/8'], ['4688/1386', '30802/24'], ['48468/636', '467/736'], ['45535/3', '45535/3'], ['4553/384', '9999/0100'], ['333/8', '33/8'], ['5597/27557575', '5597/2755775'], ['5597/2757775', '857/7291'], ['1613/58', '5597/2757775'], ['8/13', '857/7291'], ['176/669', '453/384'], ['3080/241', '7/255'], ['453/3384', '1653/58'], ['47677/736', '23/52'], ['453/38', '4688/136'], ['453/3384', '11/9'], ['99/100', '111/17'], ['47677/7736', '4677/7736'], ['468/136', '30802/24'], ['46477/7736', '4677/7736'], ['3/8', '380/241'], ['33467/76368', '333/8'], ['9943/29', '34553/384'], ['4453/3844', '1613/58'], ['47677/7736', '11/9'], ['1653/58', '8/13'], ['4/1136', '4/1136'], ['4674/74436', '4674/744346'], ['11/7', '467/7736'], ['453353/3', '6467/736'], ['30802/24', '176/9'], ['11/7', '11/77'], ['9999/0100', '3080/241'], ['11/7', '3467/7736'], ['176/17', '176/717'], ['1613/58', '3080/241'], ['77/2', '48468/636'], ['176/669', '37/55'], ['176/9', '176/9'], ['4767/736', '9999/0100'], ['9231/739', '9221/739'], ['30802/24', '3080/24'], ['467/736', '467/7366'], ['7/255', '4688/136'], ['11711/7', '3/8'], ['8577/291', '857/291'], ['5453/84', '453/84'], ['3080/24', '3080/24'], ['11/7', '857/291'], ['161111/78', '1111/7'], ['943/29', '45111/9984'], ['468/136', '5597/25757775'], ['467/736', '4637/736'], ['11/9', '1111/7'], ['467/7336', '111/9'], ['380/241', '468/13'], ['943/29', '11/9'], ['47677/7736', '47677/7736'], ['27/2', '7/2'], ['4677/7366', '4677/7366'], ['1613/58', '57597/2757775'], ['467/77636', '597/275'], ['316533/58', '8/13'], ['11/99', '11/99'], ['9999/01', '9999/010'], ['47674/7436', '3/88'], ['453/83384', '1653/58'], ['4637/77636', '467/77636'], ['8453/384', '8433/384'], ['45553/384', '9999/0100'], ['455553/384', '4353/38'], ['455553/384', '13/77'], ['5597/2755775', '3180/241'], ['453/384', '943/29'], ['9999/010', '176/9'], ['46477/7736', '9231/739'], ['9443/29', '163/538'], ['45553/384', '453/84'], ['46477/7736', '46477/7736'], ['468/136', '453/38'], ['1653/558', '1653/58'], ['9999/0100', '9999/0100'], ['44534/3844', '44534/3844'], ['3080/1', '3080/1'], ['11/9', '911/9'], ['30802/24', '47677/7736'], ['453/3338436', '453/338436'], ['5597/2757775', '1857/7291'], ['47677/7736', '8857/291'], ['4637/77636', '9943/29'], ['3/8', '45553/384'], ['4/11136', '4/1136'], ['5597/2757775', '857/21'], ['173/77', '163/58'], ['34674/74434688', '3/88'], ['163/538', '163/538'], ['8857/291', '8857/291'], ['7/25', '453/384'], ['4637/77636', '163/58'], ['2/3', '11/9'], ['37/5', '37/55'], ['468/136', '380/241'], ['4553/384', '4637/7364'], ['467/736', '4767/4736'], ['8/13', '8/13'], ['77/2', '3/8'], ['468/13', '468/13'], ['453/338436', '1653/558'], ['435383/38', '43583/38'], ['45553/384', '453/884'], ['8857/291', '7/2'], ['11/7', '49999/0100'], ['357/55', '176/9'], ['4553/3', '163/5'], ['9221/739', '857/291'], ['911/9', '911/9'], ['467/77636', '9231/739'], ['5597/25757775', '453/3384'], ['11/99', '9943/29'], ['161111/78', '3080/1'], ['8453/384', '4637/77636'], ['4677/7736', '4677/7736'], ['308435383/384', '4637/7364'], ['16/17', '176/9'], ['85577/291', '857/291'], ['1111/7', '467/736'], ['8857/291', '233/52'], ['34674/74434688', '3/8'], ['5597/2755775', '5597/2755775'], ['176/669', '47677/736'], ['453/384', '921/739'], ['4767/36', '999/100'], ['6467/736', '4677/7736'], ['5597/25757775', '8577/291'], ['3080/241', '176/9'], ['4674/7436', '44534/3844'], ['30802/24', '47677/77366'], ['4637/77636', '46367/77636'], ['27/2', '27/2'], ['3080/241', '453/3384'], ['111/17', '1111/7'], ['176/669', '5597/275775'], ['468/1136', '27/2'], ['176/9', '46367/77636'], ['8857/291', '3/8'], ['857/7291', '1111/17'], ['30800/241', '3080/241'], ['13/77', '4677/7366'], ['4674/7436', '8857/291'], ['46477/7736', '4674/74436'], ['4453/3844', '4767/4736'], ['8453/384', '857/291'], ['7/255', '453/84'], ['111/9', '4688/136'], ['9231/739', '163/5'], ['161111/178', '161111/78'], ['3080/204', '3080/24'], ['9999/01559557575', '9999/01'], ['5453/84', '545/84'], ['6467/736', '6467/736'], ['43/384', '9999/0100'], ['8/1325', '3/8'], ['3/346768', '3/346768'], ['921/739', '3/3446768'], ['1653/58', '453/338436'], ['380/241', '9999/0100'], ['77/2', '37/55'], ['48427/236', '48427/236'], ['3/8', '23/52'], ['467/7736', '9443/29'], ['4553/384', '4553/384'], ['3080/204', '453/384'], ['380/2', '468/13'], ['857/29', '85577/291'], ['161111/78', '9999/010'], ['1111/17', '921/739'], ['316533/58', '316533/58'], ['316533/58', '11/9'], ['23/521217', '23/521217'], ['943/29', '921/739'], ['3080/241', '30830/241'], ['545/84', '3080/241'], ['7467/736', '467/7366'], ['233/52', '9221/739'], ['5453/384', '921/739'], ['111/9', '111/9'], ['47677/736', '9999/01'], ['30800/241559757775', '161111/78'], ['111/17', '111/17'], ['11/9', '111/9'], ['176/717', '453/38'], ['857/7291', '7/25'], ['468/336', '468/336'], ['8453/384', '453/3384'], ['48468/66', '48468/6'], ['1111/7', '11711/7'], ['466477/7736', '9999/010'], ['467/76', '467/7366'], ['11/77', '9999/0100'], ['47677/77366', '453/3384336'], ['476767/7736', '47677/7736'], ['1611111/78', '1611/178'], ['48468/6', '9999/010'], ['857/291', '9999/01'], ['911/9', '8857/291'], ['163/538', '467/736'], ['57597/275775', '467/736'], ['16/17', '4674/744346'], ['346477/7736', '9231/739'], ['7/2', '11711/7'], ['467/7736', '4677/7366'], ['1111/17', '161111/78'], ['11/199', '4688/1386'], ['4674/744346', '467/7636'], ['30800/241559757775', '30800/241559757775'], ['4308435383/384', '4637/7364'], ['1653/58', '111/17'], ['37/55', '161111/78'], ['4676/76', '5453/84'], ['4467/7636', '467/7636'], ['468/136', '163/5'], ['4/11136', '233/552'], ['4677/7736', '467/7636'], ['857/5291', '453/3384'], ['453/3384', '453/384'], ['453/38', '1613/58'], ['11711/7', '453/38'], ['4353/38', '380/241'], ['37/55', '1776/9'], ['4674/7436', '4674/744346'], ['357/55', '357/55'], ['9999/010', '9999/010'], ['9943/29', '48468/8636'], ['468/136', '11/77'], ['453/38', '7467/736'], ['34553/384', '857/291'], ['233/5532', '4677/7736'], ['48468/8636', '163/58'], ['1363/568', '47677/7736'], ['3080/204', '453/3384'], ['83/8', '357/55'], ['4367/736', '5597/775'], ['161111/78', '9999/0910'], ['7/255', '7/255'], ['4553/384', '4688/1386'], ['84453/384', '333/8'], ['176/669', '467/7736'], ['4853/3384', '4853/3384'], ['47677/7736', '8468/6'], ['9999/01', '7/25'], ['111/9', '3080/24'], ['6467/736', '9999/010'], ['7/25', '4767/736'], ['33467/76368', '3/8'], ['9999/0910', '4677/7736'], ['11711/7', '44534/3844'], ['8/3', '468/6136'], ['9999/01', '99999/010'], ['3080/1', '380/241'], ['4674/7436', '4637/77636'], ['11/7', '711/77'], ['2/3', '7/255'], ['11/19', '380/241'], ['34674/744346888', '3/88'], ['346874/744346888', '34674/7443646888'], ['467/7636', '46367/77636'], ['1857/7291', '1857/7291'], ['4767/736', '37/55'], ['48468/66', '4453/3844'], ['453/84', '8453/84'], ['7/255', '3080/204'], ['8453/384', '34553/384'], ['857/7291', '9231/739'], ['857/8291', '857/8291'], ['4553/384', '7/255'], ['11/77', '9221/739'], ['99999/010', '9999/010'], ['4688/1386', '13/77'], ['453/884', '4533/884'], ['818757/291', '81857/291'], ['46367/77636', '176/17'], ['34553/384', '9999/910'], ['7/2', '9943/29'], ['11/199', '48468/66'], ['453/384', '233/52'], ['4767/7736', '467/776'], ['3080/1', '43853/3384'], ['46744/744346', '4674/744346'], ['467/77636', '48468/66'], ['8857/291', '308435383/384'], ['467/77346', '9443/29'], ['34674/744346888', '3/8'], ['3/8', '33/8'], ['857/5291', '3/8'], ['921/739', '9443/29'], ['6467/7636', '111/9'], ['46744/7436', '4674/7436'], ['4674/7436', '8433/384'], ['16/17', '3180/241'], ['1653/58', '459999/0108436'], ['11/999', '453/3384'], ['467/77636', '467/736'], ['11/9', '5597/25757775'], ['30802/24', '921/739'], ['11711/7', '4367/736'], ['3080/241', '11/9'], ['176/17', '11/9'], ['308435383/384', '47677/7736'], ['233/25532', '233/25532'], ['233/552', '176/9'], ['176/6669', '453/384'], ['3/24', '30802/24'], ['176/17', '34674/7443646888'], ['6467/7366', '6467/736'], ['23/521217', '37/5'], ['6467/736', '4674/744346'], ['11/17', '467/7736'], ['11/7', '9943/29'], ['467/766', '467/766'], ['857/21', '857/21'], ['453/384', '1613/58'], ['8857/291', '921/739'], ['1/3', '3/1'], ['1/99999', '99999/1'], ['1/1', '1/1'], ['1/10', '10/100'], ['1/10', '100/10'], ['1/1000000000', '999999999/1'], ['999999999/1', '1/1000000000'], ['999999/1', '1/999999'], ['16311/9', '163/58'], ['597/275', '23/52'], ['23/52', '7/25'], ['943/29', '7/25'], ['711/7', '711/7'], ['711/7', '11/9'], ['16311/9', '163/558'], ['380/241', '943/29'], ['23/5271', '921/739'], ['16/117', '16/17'], ['163/558', '163/558'], ['3280/241', '380/241'], ['163/58', '16/17'], ['23/5', '7/25'], ['9291/739', '857/291'], ['99/100', '16311/9'], ['943/29', '380/241'], ['711/7', '11/19'], ['467/736', '163/558'], ['11/7', '380/241'], ['11/19', '921/739'], ['380/241', '8/113'], ['943/29', '943/29'], ['8/113', '8/13'], ['597/275', '23/522'], ['857/291', '921/73'], ['9176/9', '23/5'], ['380/241', '943/9'], ['16/117', '163/558'], ['8/113', '8/113'], ['23/52', '99/100'], ['8/13', '7/25'], ['16311/9', '7/25'], ['23/522', '23/522'], ['857/291', '943/29'], ['9291/739', '857/9291'], ['16/17', '380/241'], ['16/117', '16/117'], ['3280/241', '380/2'], ['943/29', '9176/9'], ['8/113', '38/113'], ['3/8', '921/73'], ['23/5', '857/291'], ['857/291', '23/5'], ['16/117', '23/5'], ['943/9', '921/739'], ['8/113', '380/241'], ['380/2', '3280/241'], ['23/5', '23/5'], ['921/73', '921/73'], ['380/2', '921/73'], ['8523/5922291', '8523/522291'], ['857/2991', '23/5'], ['597/275', '7/25'], ['16311/9', '9291/739'], ['921/739', '99/100'], ['8/113', '38/13'], ['8/113', '23/5'], ['23/252', '99/100'], ['163/558', '8523/5922291'], ['8/13', '7/725'], ['8523/5922291', '23/5922291'], ['380/2', '16311/9'], ['3880/241', '380/241'], ['711/7', '380/241'], ['921/7939', '99/100'], ['9291/739', '8577/291'], ['16163/5588', '1683/58'], ['7/25', '16311/9'], ['857/291', '9493/29'], ['7/725', '7/725'], ['921/7939', '8/113'], ['11/9', '7/725'], ['7/77225', '7/725'], ['8577/291', '8577/291'], ['943/29', '11/19'], ['11/7', '1683/58'], ['176/9', '8523/522291'], ['3803/2', '380/2'], ['380/2', '8/113'], ['23/252', '38/113'], ['9176/9', '9176/9'], ['11/9', '3880/241'], ['16/17', '16/17'], ['597/275', '8523/522291'], ['921/7939', '921/7939'], ['16311/9', '467/736'], ['9176/9', '7/25'], ['857/291', '1683/58'], ['23/5922291', '453/384'], ['921/773', '921/73'], ['597/275', '23/5'], ['9493/329', '11/19'], ['0380/241', '380/241'], ['7/25', '8577/291'], ['943/9', '16/17'], ['2/252', '138/113'], ['9493/29', '857/291'], ['9176/9', '11/7'], ['9176/79', '1683/58'], ['7/25', '176/9'], ['6116/17', '6116/17'], ['921/73', '9217/73'], ['921/7939', '921/773'], ['3921/73', '3921/73'], ['16311/9', '943/9'], ['380/241', '380/24'], ['9176/79', '38/13'], ['857/291', '9943/29'], ['16/17', '16853/58'], ['99/100', '99/100'], ['943/29', '16853/58'], ['857/2991', '857/2991'], ['23/71', '11/119'], ['23/71', '16/17'], ['23/25', '23/25'], ['23/5', '380/2401'], ['857/9291', '23/5'], ['1/9', '7/725'], ['3880/241', '943/9'], ['3803/2', '23/52'], ['4380/24', '380/24'], ['380/241', '9176/9'], ['4380/24', '3880/241'], ['7/725', '7/7275'], ['8/113', '943/9'], ['99/100', '999/100'], ['85233803/2291', '8523/522291'], ['597/275', '8/113'], ['857/29911', '857/2991'], ['18/13', '7/725'], ['943/9', '2/3'], ['8577/29911', '857/2991'], ['9493/29', '380/24'], ['9217/73', '380/2'], ['857/291', '8523/5922291'], ['999/100', '943/9'], ['11/9', '857/2991'], ['163/58', '921/73'], ['380/2401', '38/13'], ['921/7939', '23/25'], ['37/55', '0380/241'], ['16683/58', '1683/58'], ['380/241', '8577/291'], ['921/7939', '388/1313'], ['163311/9', '943/9'], ['111/9', '2/252'], ['857/291', '38/13'], ['597/275', '72/25'], ['23/5922291', '8577/291'], ['7/725', '23/25'], ['16311/9', '138/113'], ['8/13', '23/5'], ['111/9', '380/241'], ['99/100', '380/4241'], ['1716/17', '176/117'], ['943/9', '943/9'], ['380/24', '380/241'], ['921/3', '921/73'], ['380/241', '111/9'], ['03080/241', '99/100'], ['116683/5817', '16853/58'], ['2857/929', '857/929'], ['976/79', '1683/58'], ['857/929', '921/739'], ['921/739', '7/25'], ['16883/58', '1683/58'], ['163111/9', '163111/9'], ['23/5', '16/17'], ['16163/5588', '1683/588'], ['943/29', '16853/658'], ['921/7939', '111/9'], ['233/522', '23/522'], ['9291/739', '38/113'], ['857/2991', '99/100'], ['857/2591', '857/291'], ['176/9', '3921/73'], ['857/29911', '31683/5841'], ['8523/522291', '8523/522291'], ['597/27', '597/275'], ['163/9', '916311/9'], ['388/1313', '38/113'], ['176/117', '176/117'], ['16883/58', '380/241'], ['7/77225', '11/9'], ['176/9', '6176/9'], ['380/241', '3/5'], ['1/9', '11/119'], ['9291/7399', '11/9'], ['11/9', '8/13'], ['380/241', '11/9'], ['943/29', '97176/9'], ['943/29', '7/7275'], ['9493/29', '11/19'], ['380/4241', '111/9'], ['16683/58', '943/2'], ['8523/5922291', '1683/58'], ['3803/2', '16/17'], ['857/2991', '8/13'], ['857/21', '3/13'], ['380/24', '16/17'], ['23/5922291', '23/252'], ['991683/58', '921/7939'], ['921/799', '8/113'], ['380/24', '11/19'], ['991683/58', '380/2'], ['857/291', '9211/739'], ['1831/13', '7/725'], ['31683/5841', '31683/5841'], ['857/2991', '380/241'], ['11/19', '11/19'], ['16163/5588', '16163/5588'], ['380/244', '380/24'], ['711/7', '921/773'], ['8523/522291', '943/9'], ['163/558', '921/13'], ['857/2291', '38/13'], ['3921/73', '979176/9'], ['9217/73', '380/41'], ['380/244', '9176/9'], ['138/1113', '138/1183'], ['597/2975', '380/241'], ['23/25', '921/7939'], ['31683/58461', '31683/5841'], ['8577/2921', '8577/291'], ['1/373', '9291/739'], ['163/558', '163/5558'], ['138/1183', '380/241'], ['176/117', '3880/241'], ['11/9', '999/100'], ['11/19', '31683/5841'], ['31683/5841', '163/58'], ['16853/658', '943/29'], ['2/252', '31683/5841'], ['3/5', '7/25'], ['168553/658', '943/29'], ['38800/241', '943/9'], ['597/2975', '3880/241'], ['916311/9', '3916311/9'], ['8577/291', '85777/291'], ['38/241', '3880/241'], ['857/9291', '857/9291'], ['467/736', '4674/736'], ['3380/41', '380/41'], ['1/9', '1/9'], ['857/291', '23/71'], ['3803/2', '138/1113'], ['921/739', '921/13'], ['9999/9100', '999/100'], ['85388/13131', '9211/739'], ['23/522', '11/19'], ['6176/9', '11/9'], ['9291/739', '16311/9'], ['131683/584619', '16311/9'], ['857/21', '921/73'], ['7/725', '23/5922291'], ['8577/291', '111/9'], ['380/24', '380/24'], ['85738/13291', '85738/13291'], ['23/522', '4674/736'], ['597/2975', '597/2975'], ['138/113', '8/13'], ['233/522', '8577/291'], ['23/25', '380/4241'], ['116853/58', '16853/58'], ['1831/13', '99/100'], ['921/7939', '921/13'], ['168353/58', '16853/58'], ['999/100', '4674/736'], ['23/5', '116853/58'], ['16853/58', '16853/58'], ['16683/58', '7/725'], ['3803/2', '111/9'], ['11/17', '380/241'], ['9943/29', '138/113'], ['16683/58', '9999/9100'], ['163/5558', '16/17'], ['138/113', '857/291'], ['138/1183', '3804/241'], ['7/725', '111/9'], ['943/2', '857/2991'], ['8/1813', '38/13'], ['467/736', '857/21'], ['711/7', '453/384'], ['857/2991', '8523/522291'], ['16311/19', '16311/9'], ['921/7939', '11/119'], ['16311/9', '9999/9100'], ['380/241', '9423/29'], ['11/77', '11/77'], ['11/17', '7/725'], ['1/373', '23/52'], ['921/799', '921/799'], ['921/7', '9217/7'], ['7/225', '9493/29'], ['921/7939', '03080/241'], ['943/2', '1683/58'], ['716/17', '16/17'], ['163/558', '9493/29'], ['921/79379', '921/7939'], ['85777/291', '943/2'], ['3/5', '4674/736'], ['11/17', '11/17'], ['9493/29', '9493/29'], ['716/17', '3380/41'], ['168553/658', '168553/658'], ['111/9', '2857/929'], ['976/79', '976/79'], ['1168531/58', '16853/58'], ['597/2975', '138/1113'], ['16/117', '16853/58'], ['176/9', '380/4241'], ['16311/9', '921/73'], ['3921/73', '857/291'], ['85388/13131', '9211/7'], ['138/1113', '138/1113'], ['3/8', '23/5271'], ['99/100', '85388/13131'], ['16883/58', '16883/58'], ['857/91291', '23/5'], ['7/5725', '7/725'], ['23/711', '23/711'], ['3803/2', '7/725'], ['176/9', '16163/5588'], ['921/799', '85738/13291'], ['72/25', '7/25'], ['921/79339', '921/739'], ['233/522', '7/725'], ['11/77', '3/13'], ['6176/9', '111/9'], ['38/1813', '8/1813'], ['81831/13', '99/100'], ['8857/2991', '857/2991'], ['23/5922291', '58577/291'], ['11/119', '16853/58'], ['11/77', '03080/241'], ['46474/736', '4674/736'], ['131683/584619', '43280/241'], ['921/739', '163/558'], ['3/13', '23/52'], ['16163/51588', '16163/5588'], ['16/17', '8523/5922291'], ['233/25', '38/113'], ['921/7939', '3380/41'], ['7/5725', '8577/291'], ['9999/9100', '7/25'], ['3380/41', '8/113'], ['857/9291', '3/13'], ['3916311/9', '8/113'], ['168553/658', '8523/522291'], ['163311/9', '163311/9'], ['188/13', '7/725'], ['3803/2', '3803/2'], ['163/58', '2/252'], ['38/241', '380/244'], ['1616816/178558', '467/736'], ['6116/17', '16/117'], ['23/25', '8577/291'], ['23/5922291', '2/3'], ['3804/241', '38404/241'], ['11/119', '8523/5922291'], ['16/17', '9291/739'], ['16855/658', '168553/658'], ['38404/241', '8/13'], ['6116/17', '23/25'], ['8527/929', '23/25'], ['8577/29911', '8/113'], ['1/99', '1/9'], ['857/291', '9493/929'], ['6176/9', '6176/9'], ['16311/9', '16311/9'], ['921/799', '31683/5841'], ['1616816/178558', '176/9'], ['943/9', '467/736'], ['94233/29', '94233/29'], ['99/100', '921/739'], ['3803/2', '23/71'], ['380/44241', '176/9'], ['7/5725', '380/2401'], ['9176/9', '7/5'], ['1168531/58', '857/2991']]
    results = [True, False, True, False, True, True, True, False, False, True, True, False, True, False, True, True, True, True, True, True, True, True, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, True, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, True, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(simplify)