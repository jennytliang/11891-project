def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Include these tokens in the code: ), 2 , - 1 ):
	Do not include these tokens in the code: )):
	"""


    ans = text
    for i in range(le(ans)):
        if ans[i] == ' ':
            ans = ans[:i] + "_" + ans[i + 1:]
        else:
            pass
    for i in range(le(ans)):
        if ans[i] == '  ':
            ans = ans[:i] + "-" + ans[i + 1:]
        else:
            pass
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
    inputs = [['Example'], ['Mudasir Hanif '], ['Yellow Yellow  Dirty  Fellow'], ['Exa   mple'], ['   Exa 1 2 2 mple'], ['Hello,   world!'], ['happy 123'], ['Hey    there!'], ['  spaces  every  where  '], ['NoSpacesHere'], ['This is  a  test'], ['Testing     1  2   3'], ['Hello World'], ['Hello   World'], ['   Hello World'], ['This is  a  tesst'], ['This is  a  tes'], ['This is  a This is  a  tes test'], ['Hello r  World'], ['This is  a Hello r  World tsesst'], ['This is  a This is  a  tes test  spaceNoSpacesHere '], ['Thish is  a  tesst'], ['HelloNoSpacesHere,   world!'], ['Hey   e there!'], ['  spaces  eveThis is  a This This is  a This is  a  tes test  spaceNoSpacesHere is  a  tes testry  where  '], ['happy 123  spaces  every  where  '], ['  spaces  eveThis is  a This  This is  a This ishappy 123  a  tes test  spaceNoSpacesHere is  a  tes testry  where  '], ['Hello r  Word'], ['This is  a sst'], ['  spaces  eveThis is  a This This is  a This is  a  tes test  spaceNoSpacesHello r  WorldHere is  a  tes testry  where  '], ['  spaces  eveery  where  '], ['happy1233'], ['  spaces  eveThis is  a This This is  a This is  a  tes test  spaceNoSpacesHeNoSpacesHerello r  WorldHere is  a  tes testry  where  '], ['happy 123 p spaces  every  where  '], ['  spaces  eveThis is  a This This is  a This is  tes testry  where  '], ['Thish isThis is  a Hello r  World tsTesting     1  2   3 a  This is  a ssttesst'], ['Helleo World'], ['happyw 123 p spacees  every  where  '], ['Thish is  a  tesHey    there!st'], ['happyw 123 p spacees  This is  a sstevery  wher  '], ['  spaces  every  w here  '], ['Th is is  a This is  a  tes test'], ['This is   a This is  a  tes test  spacoeNoSpacesHere '], ['  spaces  eveThis is  a This  This is  a This is happy 123  a  tes test  spaceNoSpacesHere is  a  tes testry  where  '], ['Thihappyw 123 p spacees  This is  a sstevery  wher  s is  a Hello r  Woreld tsesst'], ['  spaces  eveThis is  a This This is  a This is  a  tes test  spaceNoSpacesHtry  where  '], ['happThis is  a  tessty'], ['This is  a T  spaces  eveThisTh is is  a This is  a  tes test is  a This  This is  a This ishappy 123  a  tes test  spaceNoSpacesHere is  a  tes testry  where  his is  a  tes test'], ['This is Thish is  a  tesHey    there!st a This is  a  tes test  spaceNoSpacesHere '], ['Thish is  asst'], ['  spaces  everThis is  a This is  a  tes testy  where  '], ['This is  This is  a T  spaces  eveThisTh is is  a This is  a  tes test is  a This  This is  a This ishappy 123  a  tes test  spaceNoSpacesHere is  a  tes testry  where  his is  a  tes testa  tes'], ['  spaces  eveThis tis  a This This is  a This is  a  tes test  spaceNoSpacesHere is  a  tes testry  where  '], ['  spaces  eveThis is  a This This is  a This is  a  tes test  spaceNoSpacesHello r   WorldHere is  a  tes testry  where  '], [' happyw 123 p spacees  every  where  '], ['happyw 123 p spacees  This is  a sstevery  whser  '], ['  spaces  eveThis is  a This This is  a This is  a This is  a  tes test  spaceNoSpacesHere This is  tes testry  where  '], ['haappy1233'], ['Testing   Hey   e there!  1  2   3'], ['Hello r   spaces  eveThis is  a This This is  a This is  a  tes test  spaceNoSpacesHello r   WorldHere is  a  tes testry  where   Word'], ['Testing   s  1  2   3'], ['Th is is  a This is  a  tes teHello,   world!st'], [''], ['ThThis is  a Hello r  World tsesstis is  a sst'], ['This is  This is  a T  spaces  eveThisThh is is  a This is  a  tes test is  a This  This is  a This ishappy 123  a  tes test  spaceNoSpacesHere is  a  tes testry  where  his is  a  tes testa  tes'], ['This is  sst'], ['NoSere'], ['ThTthis is  a Hello r  World tsesstis is  a sst'], ['This is  a This is  a  tes test  spaceNioSpacesHere '], ['This iis  a sst'], ['Thihappyw 123 p spacees  Thi s is  a sstevery  wher  s is  a Hello r  Woreld tsesst'], ['This is  a This istest'], ['Helleo Worldhappyw 123 p spacThis iis  a sstees  every  where  '], ['Hello r  Worlld'], ['Testing This is  a sst  e there!  1  2   3'], ['ere!st'], ['This is  a This is  a  t  spaces  eveThis is  a This This is  a This is  a This is  a  tes test  spaceNoSpacesHere This is  tes testry  where  est'], ['Hhappy 123 p spaces  every  where  ello r  Word'], ['He  spaces  eveThis is  a This This is  a This is  a This is  a  tes test  spaceNoSpacesHere This is  tes testry  where  llo,   wod!'], ['rCMrcvK'], ['This sis  a  tes'], ['  spaces  eveThis is  a This This is  a This is  a This is  a  tes test  spaceNoSpacesHere This is  tes testr  where  '], ['  spaThis  This is  a This ishappy 123  a  tes test  spaceNoSpacesHere is  a  tes testry  where  '], ['Th is is  a This is  aHey   e there!  tes test'], ['Thish Helleo Worldhappyw 123 p spacThis iis  a sstees  every  where  is  a  tesHey    there!st'], ['Hello r   spaces  eveThis is  a This This is  a This is  a  tes test  spaceNoSpacesHellThish isThis is  a Hello r  World tsTesting     1  2   3 a  This is  a ssttessto r   WorldHere is  a  tes testry  where   Word'], ['Th is is  a This is  a  tes teTHello,   world!st'], ['ThTthis sis  a Hello r '], ['Thihappyw 123 p  spaces  eveThis is  a This This is  a This is  a  tes test  spaceNoSpacesHtry  where   spacees  This is  a sstevery  wher  s is  a Hello r  Woreld tsesst'], ['  spaces  everThis is  a This is  a  tes tThish Helleo Worldhappyw 123 p spacThis iis  a sstees  every  where  is  a  tesHey    there!stesty where  '], ['NoSer'], ['Thish Helleo Worldhappyw 123 p spacThis iis  a sstees  every  where  ishappy 123 p spaces  every  where    a  tesHey    there!st'], ['Hello rr  Word'], ['Hello r   spaces  eveThis is  a This This iThis is  Hey   e there!a This is  a  tes tests  a This is  a  tes test  spaceNoSpacesHellThish isThis is  a Hello r  World tsTesting     1  2   3 a  This is  a ssttessto r   WorldHere is  a  tes testry  where   Word'], ['HeThis is  a This istestlWlo World'], ['NoS'], ['Testing   Hey   e there!  1  2 This is  a This is  a  tes test  spaceNoSpacesHere   3'], ['  spaces  eveThis is  a This This is  a This is  a This is  a  tes test  spaceNoSpacesHere This is  tes testry  where '], ['NSooSerre'], ['Hello r   spaces  eveThis is  a This This iThis is  Hey   e there!a This is  a  tes tests  a This is  a  tes test  spaceNoSpacesHellThish isThis is  a Hello r  World happy 12Testing   s  1  2   33  spaces  every  where  tsTesting     1  2   3 a  This is  a ssttessto r   WorldHere is  a  tes testry  where   Word'], ['This is  This is  a T  spaces  eveThisTh is is  a This is  a  tes test is  a This  This is  a This ishappy 123  a  tes test  spaceNoSpacesHere is  a  tesHello r   spaces  eveThis is  a This This iThis is  Hey   e there!a This is  a  tes tests  a This is  a  tes test  spaceNoSpacesHellThish isThis is  a Hello r  World tsTesting     1  2   3 a  This is  a ssttessto r   WorldHere is  a  tes testry  where   Word testry  where  his is  a  tes testa  tes'], ['Helo r  Worlld'], [' happyw 123 p spacees  every  whhere  '], ['HTh is is  a This is  a  tehappy 123  spaces  everyHello r   spaces  eveThis is  a This This is  a This is  a  tes test  spaceNoSpacesHello r   WorldHere is  a  tes testry  where   Wordo,   world!stey   !'], ['Thish isThis is  a Hello r  World tsTesting 3 a  This is  a ssttesst'], ['   Exa 1 2 2\nmple\tExample   3'], ['   A-B-*_--C   '], ['---a-a-a---b-b-b-c-c-c---'], ['Big gaps    between words    in this sentence'], ['          '], ['    '], ['         '], ['Exa 1 2 2 mple'], ['Example  1'], ['    Example   2'], ['    Example   2    Example   2'], ['  E  Example   2'], ['this'], ['----a-a-a---b-b-b-c-c-c---'], ['     '], ['his'], ['words'], ['ExampleEthisxa3e  1'], ['Exx1'], ['  his   '], ['gaps'], ['ggaps'], ['ggga'], ['  his    '], ['   Ex     2\nmple\tExample   3'], ['---a-a-a---b-b-b-c-c-c---     '], ['Example    Example   2    Example   2  1'], ['A-B-*_--C'], ['EEx'], ['Exa'], ['   A-B-*_-E-C   Ex     2\nmple\tExample   3'], ['---a-ac-c---      '], ['ExampleEthisxa3e'], ['  his     '], ['2'], ['in'], ['  E  Egapsxample   2'], ['  ExampleE  Expample   2'], ['   Exa 1 2 Exa2\nmple\tExample   3'], ['  E  Ega psxample   2---sa-ac-c---'], ['ExampleeEthisxa3e'], ['zPb'], ['ExampleEt  E  Ega psxample   2---sa-ac-c---hisxa3e'], ['hsis'], ['  E  Example  2'], ['   A-B-*_-E-C   Ex     2\nmple\tExample  m 3'], ['EExample  1Ex'], ['  his    EExample'], ['psxample'], ['ExampleEthitsxa3e'], ['1'], ['----a-aa-a---b-b-b-c-c-c---'], ['---a--a-a---b-b-b-c-c-c---'], ['hsExampleEthisxa3es'], ['Expample'], ['his  ExampleE  Expample   2'], ['sentence'], ['Exa2'], ['   Exa 1 2 2\nmple\tExample   2---sa-ac-c---'], ['   Exa 1 2 Exa2\nmple\tEx3'], ['   '], ['   Exa 1 2 2\nmple\tExample 3'], ['ExampleEtEhisxa3e  1'], ['    E  Ega psxample   2---sa-ac-c--- A-B-*_-E-C   Ex     2\nmple\tExample   3'], ['hsE2xampleEthisxa3es'], ['Example    Example   2    Examle   2  1'], ['  hExampleEthitssxa3eis    EExample'], ['          EEx'], ['thits'], ['----a-a-a---b-b-b-c-c-c---ExampleEtEhisxa3e'], ['---a-ac-c---'], ['      psxample EEx'], ['E'], ['    his    A-B-*_--C   '], ['TnYIFZqaAz'], ['between'], ['zEx3Pbb'], ['gs'], ['      '], ['---a--a-a---b-b-b-c-c--c---'], ['   Ex     2\nmple\tExample   3i'], ['   Exa mpleample   3'], ['  hismpleample     '], ['thitts'], ['ExampleEt  E  Ega psxample   2---sa-ac-c---h-isxa3e'], ['  '], ['  his  hismpleample '], ['---a--a-a---b-b-b--c-c-c---'], ['word'], ['thi  E   Exa 1 2 2\nmple\tExample 3  2'], ['---a-ac-   A-B-*_-E-C   Ex     2\nmple\tExample   3c---'], ['Exampl   eEthishiExamlesxa3e  1'], [' Exx1   '], ['ggap'], ['  hExampleEthitssxa3eis    EExampple'], ['E  x3'], ['  his  h  hismpleample     ismpleample '], ['R'], ['   Ex     2\nmple\tExample   ExampleEi'], ['ExampleEtEhisxa3e  1gggaps'], ['hsExmampleEthisxa3es'], ['ExaxmpleEthitsxa3e'], ['   Exa 1ExampleEtEhisxe  1gggaps   3'], ['gss'], ['           '], ['hhis'], ['gggga'], ['Exampl'], ['ExampleEtExampl   eEthishiExamlesxa3e  1'], ['    his    A-B-*           _--C   '], ['ExampleEtExampl'], ['hhi---a-a-a---b-b-b-c-c-c---s'], ['---a--a-a---b-b-b-c-c--'], ['Big gaps    between words    i2---sa-ac-c---n this sentence'], ['Exam    Example   2pleEtEhisxa3e  1'], ['2---sa-ac-c---'], ['11'], ['dwords'], ['betweeExampleEthisxa3e  1n'], ['hhi---a-a-a---  E  Ega psxample   2---sa-ac-c---b-b-b-c-c-c---s'], ['E  E2---sa-ac-c---b-b-b-c-c-c---sx'], ['hhi-    his    A-B-*           _--C   --a-a-a---'], ['hsExampthitsleEthisxa3es'], ['ismpleample'], ['hhi---a-a-a---'], ['hsExampleEtheisxa3es'], ['   Exa mp  leample   3'], ['ExampleEt  E  Ega psxample   2---sa-ac-c---h-isx'], ['EleEatEhisxa3e  1'], ['  hs'], ['---a--a-a---b-      psxample EExb-b-c-c--'], ['s'], ['ExExamplampleEthisxa3e'], ['   his  h  hismpleample     ismpleample '], ['---a-ac-ca---'], ['  hExa  hsmpleEthitssxa3eis    EExample'], ['A-B-*_  hExampleEthitssxa3eis    EExampple-E-C'], ['ExExamplampleEt  E  Example   2hisxggggaa3e'], ['---a-a-a----c---     '], ['Exampitsxa3e'], ['----a-a-a---b-hsmpleEthitssxa3eisb-b-c-c-c---'], ['thtis'], ['---a-ac-c-thitts-'], ['hihis'], ['---a-a  ExampleE  Expample   2  3c---'], ['wo'], ['Exaword'], ['thhisis'], ['hhi-'], ['    his     A-B-*_-E-C   Ex     2\nmple\tExample  m 3thitssxa3eis    EExample-C   '], ['zPPb'], ['EExampple-E-C'], ['E  c-c-c---sx'], ['i2---sa-ac-c---n'], ['    his   Exx1   --C   '], ['ExampleEtEhisxa3e'], ['hhi---a-a-a---c-c---s'], ['Exmpl'], ['3'], ['Rhsis'], ['sjRboRkSy'], ['2---sa-ac-c---h-isx'], ['mples'], ['Exa3c---leEtEhisxa3e'], ['hsE    his   Exx1   --C   xmampleEthisxa3es'], ['i2---sa-a-c-c---n'], ['   Exa 1 2 Exa2\nmpl'], ['thi'], ['hsExampleExthisxa3es'], ['hh'], ['hhhis'], ['hsE    his   Exx1   --C   xmampleEthis   Exa mp  leample   3xa3es'], ['EExample-C'], ['2  2   '], ['2---sa-ac-c---h-isxa3e'], ['3xa3es'], ['his  ExampleE  E3thitssxa3eisxpample   2'], ['Exam'], ['---a-ac-   A-B-*m_-E-C   Ex     2\nmple\tExample   3c---'], ['2----sa-ac-c---'], ['thhiss'], ['wodhhi-s'], ['FoFlZTDagW'], ['   Exa 1 2 2\nmple\tExBig gaps    between words    i2---sa-ac-c---n this sentenceample 3'], ['ExampleEtExpampl'], ['   Exa 1 2 2\nmple\tExa---a-ac-mple 3'], ['   Exa mp  leample   3Example  1'], ['Exa---a-ac-mple'], ['sgs'], ['---a-thits-a-a---b-b-'], ['xmampleEthisxa3es2  ExaxmpleEthitsxa3e3c---'], ['his  ExampleE     2'], ['  ---a-ac-c---       Example   2'], ['3c---'], ['ggagp'], ['EFoFlZTDagWE'], ['hs'], [' p ExaxmpleE  Expample   2'], ['111'], ['ggagExampleEtEhisexa3gep'], ['   Exal mp  leample   3'], ['gapshhi---a-a-a---  E  Ega psxample   2---sa-ac-c---b-b-b-c-c-c---s'], ['ga Exx1   s'], ['---a-a-a----c---'], ['wwo'], ['   Exa 1ExampleEtEhmisxe  ggaps   3'], ['A-B-*'], ['    Example   2    Example words  2'], [' Ex3  Ex     2\nmple\tExample   3i'], ['thhi'], ['iin'], ['--a-a-a---'], ['his  ExapmpleE  E3thitssxa3eisxpample   2'], ['---a-ac-c-a---'], ['jgOtGgdMm'], ['ExampleEt  E  Ega pshhi---a-a-a---b-b-b-c-c-c---sxample   2---sa-ac-c--11-h-isx'], ['1gggaps'], ['-E  c-c-c---sxxample EExb-b-c-c--'], ['hhi-hhh'], ['   Exa 1gaps   3'], ['hsExampleExthi  hssxa3es'], ['----a--a-a---b-b-b-c-c--c---'], [' p Exax  Expample   2'], ['ExExameplampleEthisxa3e'], ['thi  E   Exa 1 2 2\nmple\tExampExampleEtle 3  2'], ['hsmpleeEthishiExamlesxa3eEthitssxa3eis'], ['---a-a-aExampleEt  E -c---hisxa3e--c---'], ['  hExampxleEtEhisxa3e  1ile'], ['EleEatEhisxa3e'], ['ExampleEi'], ['wo_--C'], ['Exampl   eEthish iExamlesxa3e  1'], ['c-c-c---sxxample'], ['   Exple   3'], ['  his '], ['   hi s  h  hismpleample     ismpleample '], ['gapshhi---a-a-a---  E  Ega psxample   2---sa-ac-c----b-b-b-c-c-c---s'], ['  E  Ega psxa   Ex     2\nmple\tExample   3mple   2---sa-ac-c---'], ['A-B-*_'], ['     his   Exx1   --C       '], ['sentenceample'], ['ggs'], ['    Example   2    Example   2   Exa 1ExampleEtEhisxe  1gggaps   3'], ['c-c-c----sx'], ['hsmpleEthitssxa3eis'], ['  his  hi2hisxggggaa3e '], ['----a-ac-c-thitts-'], ['2   2   '], ['Ex3ampleEtEhisxa3e  1'], ['his  Exam   A-B-*_-E-C   Ex     2\nmple\tExample  m 3pleE  mE3thitssxa3eisxpample   2'], ['   Ex     2\nmple---a-a-a----c---\tExample  eEi'], ['   Exa 1 2 2\nmple\tExBig gaps    between words    i2---sa-ac-c---n this sentenceeample 3'], ['-E'], ['---a--a-a---b-b-Example  1-c--c---'], ['  E  Ega psxample   2---sa-ac-c-  E  Example   2--'], [' Exx   Ex     2\nmple\tExamhhple   3i1   '], ['hsExampleExthi  hssxA-B-*_--Ca3es'], ['    his    A-B-*          3i1 _--C   '], ['E2---sa-ac-c---b-b-b-c-c-c---sx'], ['  E 2 Example   2'], ['A-B*--*_--C'], ['gapshhi---a-a-a---'], ['thi  E   Exa 1 2 2\nmple\tExampExamplE  c-c-c---sxeEtle 3  2'], ['cc-cggs-c---sxxcample'], ['hhi---a-a-a---b-b-b--c-c-c---s'], ['sggs'], ['  EExb-b-c-c--  Example   2'], ['ss'], ['   Eexa 1 2 2\nmple\tExample 3'], ['gapshhi---a-2---sa-ac-c---hisxa3e---'], ['mple---a-a-a----c---'], ['xmampleEthisxa3es'], ['ggss'], ['E E x3'], ['sjRboRkS'], ['  his   hi2hisxgEleEatEhisxa3egggaa3e '], ['EEE'], ['ExampleEtExampl   eEthishiExamlesxa3e  e1'], ['hhh'], ['   his     '], ['22--'], ['   3'], ['---a--a-a---b-b-b-c-bismpleample'], ['c-c-c---sxxamplthi  E   Exa 1 2 2\nmple\tExampExampleEtle 3  2e'], ['   A-B-*_-E-C   Ex     2\nmple\tExamp1gggapsle  m 3'], ['Examle'], ['    Example   2    Example words  22'], ['tshitts'], ['2---sssa-ac-c---h-isxa3e'], ['his  ExExampl   eEthishiExamlesxa3e  1ampleE  Expample   2'], ['Examhhple'], ['hsE'], ['hisExampBig gaps    between words    in this sentenceleEthisxa3es'], ['ExampleEtEhisx'], ['senteExamplnce'], [' p ExaxmpleE  Expample a  2'], ['dwoc-c-c---sxeEtlerds'], ['Exal'], ['hsmpleeEthishiExame1lesxa3eEthitssxa3eis'], ['E sc-c-c---sx'], ['worrd'], ['Exam    Example   2pleEA-B-*_-E-CtEhisxa3e  1'], ['Eexa'], ['betweeExasxa3e  1n'], ['sss'], ['ExampleEtEhis3xa3e'], ['   A-B-*_-E-C   Ex     2\nmple\tExampsenteExamplnce1gggapsle  m 3'], ['2---sa-ac-c-Exax--'], ['Eampl'], ['IclExampleEthisxa3e  1'], ['---a--a-a---b-b--Example  1-c--c---'], ['bet3e  1n'], ['---a-a--a----c---'], ['hsExampleExthi ExampleEi hssxA-B-*_--Ca3es'], ['EExx'], ['IclExample'], ['fwlMxhGm'], [' sentenceleEthisxa3esc-c---'], ['hjnY'], ['2   2'], ['2hsExampleExtEleEatEhisxa3e  1hi2--'], ['ga'], ['    Example   2    Exampxle   2'], ['ExamxpbetweeExasxa3e  1nl'], ['---a-thits-a-a- sentenceleEthisxa3esc-c-----b-b-'], ['ybsTcN'], ['dw   his     ords'], ['2---sa-ac--c---'], ['htsExampthitsleEthisxa3es'], ['hsihis'], ['ihihis'], ['  E  ExaExx2'], ['---a-thits-a-a- sentenceleEthisxa3esc-c-----bggagp-b-'], ['EExampple'], ['Exmp---a--a-a---b-b-Examplel'], [' sRentenceleEthisxa3esc-c--'], ['-   '], ['ExampleEmtExampl   eEthishiExamlesxa3e  e1'], ['  ExampleE  Expamplp2'], ['---a-thits-a-a- sentenceleEthisxa3esc-c-----his  ExampleE  Expample   2b-b-'], ['Exampthhisisa3e'], ['--C'], ['KsMcxuu'], ['ce-c-c---sxxample'], ['22  2   '], ['_--C'], ['EExpampl'], ['xmamspleEthisxae3es'], ['-ExapmpleEc-thitts-'], ['his  Exam   A-B-*_-E-C   Ex     2\nmple\tExample  m 3pleE  mE3thitssxa3ei   2'], ['ple'], ['3Example    Example   2    Example   2   Exa 1ExampleEtEhisxe  1gggaps   3'], ['ExampleEtExampl   eEthishiExamlesxa3e p e1'], ['1gapszzPPb'], ['DQaiLlVsgN'], ['    his     A-B-*_-E-C   Ex     2\nmple\tExample  m 3thitssxa3eis    EExample  hismpleample     -C   '], ['ExamplhsEteEthitsxa3e'], ['ExampleEt  E  Ega psxample   2---sa-abetweeExasxa3e  1n-isx'], ['Ku   A-B-*_-E-C    Ex     2\nmple\tExample   3Mcxuu'], ['ssgs'], ['---a-thits-a-a- sentenceleEt p ExaxmpleE  Expample a  2-b-b-'], ['ExaxmpleEthitsxa3e3c---'], ['ExampleEt   E  Ega pshhi---a-a-a---b-ggsb-b-c-c-c---sxample   2---sa-ac-c--11-h-isx'], ['sentenceleEthisxa3esc-c---'], ['thmple'], ['ssss'], ['cc-cggss-c---sxxcample'], ['Ku   A-B-*_-E-C    Ex     2\nmple\tExample   cc-cggs-c---sxxcample3Mcxuu'], ['  hExampleEthitssxa3eis Ex3ampleEtEhisxa3e  1   EExample'], ['sentenceleEthisxa3esc-c-----his'], ['3Mcxu     u'], ['gsss'], ['   A-B-*_-E-C   Ex    hismpleamplegapsle  m 3'], ['---a-thits-a-a  his    ---b-b-'], ['zExmplPb'], ['EExammle'], ['---a-a  ExampleE  Exp-ample   2  3c---'], ['EF2---sa-ac-c--11-h-isxoFlZTDagWE'], ['  his EF2---sa-ac-c--11-h-isxoFlZTDagWE'], ['hExampleEthitssxa3eis'], ['hsExampaleEtheisxa3es'], ['h'], ['T'], ['_wo_--C'], ['2hsExampleExtEleEatEh-isxa3e  1hi2--'], ['A-B---C'], ['2hsExampleExtEleEatEh-is-'], ['   Ex     2ple   3i'], ['his  ExampleE      2'], ['  his   ExampExampleEtle EExample'], ['mE3thitssxa3eisxpample'], ['    his     A-B-*_-E-C   Ex     2\nmple\tExample  m 3thitssx   A-B-*_-E-C   Ex     2\nmple\tExample  m 3a3eis    EExample-C   '], ['c-c-c---sxxamplthi  E   Exa2 2\nmple\tExampExampleEtle 3  2e'], ['    his   Exx1 Exa2--C   '], ['2pleEtEhisxa3e'], ['xal'], ['    Example   2     Example words  22'], ['Examxpbetw--CeeExasxa3e  1nl'], ['hhi---a-a-a---b-b-bKu-c-c-c---s'], ['2----sa-aciin-c---'], ['rpfY'], ['c-c-c---sxeEtle'], ['---a--a-a---b-b-Example'], ['----a-aa-a2-b-b-c-c-c---'], ['Examxpbetweel'], ['ExampExamplE'], ['wodhhi-ws'], ['1ileExBig'], [' ExampleEtEhisx  Exa mp  leample   3'], ['2hsExampleEis-'], ['zExmbplPb'], ['2  2---a-a--a----c---   '], ['----a-a-a---b-b-b-c-c-c---ExamplceEtEhisxa3e'], ['2---sa-abetweeExasxa3e'], ['Ega'], [' ExampleEtEhis  his   ExampExampleEtle EExamplex  Exa mp  lmeample   3'], ['---a--ba-a---b-b-b-c-bismpleample'], ['beteweeExasxa3e  1n'], ['Exa1ExampleEtEhmisxemple  1'], ['hhi----a-thits-a-a- sentenceleEthisxa3esc-c-----bggagp-b-hhh'], ['3pleE'], ['wordss'], ['---a-a'], ['Exa3c--i-leEtEhisxa3e'], ['EExam  E  ExaExx2ple  1Ex'], ['hhihh'], ['---a---b-b-b-c-c-c---ExampleEtEhisxa3e'], ['plethmple'], ['xalxmamspleEhhhi---a-a-a---b-b-b--c-c-c---sthisxae3es'], ['g    his    A-B-*_--C   gs'], ['hiss'], ['n'], ['gsentencele-a---'], ['PzPPb'], ['2---sa-ac---c---'], ['3Example'], ['  hjnYExample'], ['--CC'], ['---a--a-a---b-'], ['--CExampleEmtExamplC'], ['Examxpbe2   2tw--CeeExasxa3e  1nl'], ['22EExample-C--'], ['     his   Exx1   --C       d'], ['EExc-c-c---sxeEtlepampl'], ['ExampleEt  E  Ega psxample   2---sa-ac-c---hisxa3eE'], ['1   Exa 1 2 2\nmple\tExBig gaps    between words    i2---sa-ac-c---n this sentenceample 3aps'], ['hExampxleEtEhisxa3e'], ['sentenceleEthicsxa3esc-c---'], ['mplees'], ['   Ex     2\nmple\tExample   ExmampleEi'], ['         Example   2    Example   2   Exa 1ExampleEtEhisxe  1gggaps   3      '], ['gW'], ['htsExampthitsleEthisxahhi---a-a-a---b-b-bKu-c-c-c---s3es'], ['i2---s-a-a-c-c---n'], ['sentenceleEt3mplehicsxa3esc-c---'], ['---a--a-a---b-b-b-c-c----'], ['  his  h  hismplhsExampleExthi ExampleEi hssxA-B-*_--Ca3eseample     ismpleample '], ['wordrd'], ['thitExampExampleEtles'], ['   A-B-*_-E- C   Ex     2\nmple\t    E  Ega psxample   2---sa-ac-c--- A-B-*_-E-C   Ex     2\nmple\tExample   3ampsenteExamplnce1gggapsle  m 3'], ['  E  xaExx2'], ['xaE sentenceleEthisxa3esc-c---'], ['zP----a-a-a---b-b-b-c-c-c---ExamplceEtEhisxa3e'], ['tsthitts'], ['3apswd'], ['ExExamplampleEt  E  Example   2hisxggaa3e'], ['thitteEthishts'], ['A-B-*m_-E-C'], ['sentenceleEthisxaa3es'], ['ExampleEt  E  Ega psxample   2---sa-ac-c---hisxa3e-C'], ['3thitssx'], ['---E  c-c-c---sxxample EExb-b-c-c----a-a-a---b-b-b-c-c-c---ExamapleEtEhisxa3e'], ['    Examp2pleEtEhisxa3eExample   2'], ['s3thitssxa3eis'], ['    his    A-BA-B-*_  hExampleEthitssxa3eis    EExampple-E-C-*           _--C   '], ['  hExampleEthitssxahsE2xampleEthisxa3es3eis    EExam'], ['1ampleE'], ['mE3tshitssxa3eisxpample'], ['2---sa-ac-c--  Exx1   -h-isxa3e'], ['   shis     '], ['A-B-*mA_-E-C'], ['ExExamplampleEt  E  Example   2hisx'], ['ithits'], ['---a--a-a---b-   Ex     2\nmple\tExample   ExmampleEib-b--c-c-c---'], ['hismpleamplegapsle'], ['nn'], ['hsE    his   Exx1   --CE   xmampleEthisxa3es'], ['Exeamggapsle'], [' s ExampleeEthisxa3e'], ['ExampsenteExamplnce1gggapsle'], ['bExametweeExasxa3e  1n'], ['---a--a-a---b-   Ex     2\nmple\tExample   ExmampleEib-b--cc-c-c---'], ['E1ExampleEtEhisxeaEzExmplPbEEE'], ['   Exa 1ExampleEtEEhmisxe  ggaps   3'], ['gaTnYIFZqaAzpshhi---a-a-a---'], ['2-    his     A-B-*_-E-C   Ex     2\nmple\tExample  m 3thitssxa3eis    EExample-C   --sa-ac---c---'], ['    his    A-BA-B-*_  hEx  hExampleEthitssxa3eis    EExamppleampleEthitssxa3eis    EExampple-E-C-*           _--C   '], ['cc-cggss-c---sxxcgapshhi---a-2---sa-ac-c---hisxa3e----ample'], ['   A-B-*_-E-C   Ex     2\nmple\tExample  E  c-c-c---sx3'], ['ExpampA-B-*_le'], ['2hsExampleExtEleEasRentenceleEthisxa3esc-c--tE2   2h-is-'], ['sRentenceleEthisxa3esc-c--'], ['thitExmE3thitssxa3eisxpampleampExampleEtles'], ['hisExampBig gaps    between words    in this sentenceleEthisxa3 es'], ['   Ex     22\nmple\tExample   3'], ['Exa-E'], ['hhis2---sa-ac-c---h-isx'], ['2---sa-ac-c-i--h-isxa3e'], [' '], [' a b c '], [' a  b  c '], ['        '], [' a   b c  '], ['ABC'], ['1 2 3'], ['百度是中国最大的搜索引擎'], ['Big gaps    between words    in thce'], ['Big gaps    between words    in this sen3tence'], ['  Big gaps    between words    in thce      '], ['        mple'], ['  Big        '], ['mple'], ['  Big gaps    between words    Big gaps    between words    in this sen3tencein thce          '], ['  Big            Example   2'], ['Exa 1 2 2 mplle'], ['   gaps'], ['wor  Big gaps    between words    Big gaps    between words    in this sen3tencein thce          ds'], ['thce'], ['mmple'], ['   Example  1 '], ['    Example 2'], ['sen3tence'], ['mmpleExample  1'], ['  Big            ExamExaple   2'], ['Big'], ['     Example   2   '], ['Exa 1 2 2 mpsen3tencee'], ['ExamExaple'], ['Exxa'], ['   A-BExample   '], [' Big gaps    between words    in thce  '], ['Big gap        mples    between words    in thce'], ['     gaps A-B-*_--C   '], ['sen3tencein'], ['se3n3tence'], ['Big gaps    between words     in this sen3tence'], ['mmpleExample'], ['mplExa 1 2 2 mpsen3tenceees'], ['Exa 1 2 2 mpl  Big            ExamExaple   2e'], ['mmpleE1'], ['   A-B-*_--C  Big gaps    between words    in this sen3tence- '], ['   A-gapsB-*_--C   '], ['t Big gaps    between words    in thce  his'], ['Exa 1 2 2 mpExample  1sen3tencee'], ['  Big gaps    between words    in thce      fKqrpAGA'], ['EExample  1'], ['  Big gaps    between words   o in thce      '], ['th   Exa 1 2 2\nmple\tExample   3s'], ['BiBg'], ['mfKqrpAGApleE1'], ['EExampEle  1'], ['BWnXAhX'], ['                    '], ['sen3tenncein'], ['EExa'], ['Ex     mmpleE1   ample  1'], ['mpsen3tenceees'], [' Big gap        mples    between words    in thce'], ['   A-gaps-B-*_*--C   '], ['  Big gaps    between words   o in thce          '], ['Ex    Example 2xa'], ['EExample'], ['   A-gaps-B-*_*s--C   '], ['         sen3tenncein'], ['   le   '], ['Exa 1 2 2 m'], ['tthhce'], ['Exa 1 2 2 mpsent3tencee'], ['Exa 1 2  2 m'], ['   A-B-*_--C   mplExa'], ['A-gapsB-*_--C'], ['BWnXAh'], ['fKqrpAGA'], ['Exa 1 2 2 mp'], ['Big gaps    bet ween words    in this sentence'], ['se3n3ntence'], ['EExa 1 2 2 mpsent3tencee2xa'], ['    ExampleEx    Example 2xa 2'], ['   A-B--*_--C   mplExa'], ['se3n           3tence'], ['Exa 1 2 2 mpl  Big            ExamExa 1 2 2 me'], ['ample'], ['th   Exae 1 2 2\nmple\tExample   3s'], ['BBig'], ['   A-x   '], ['   A-gapsB- '], ['ExxEa'], ['     gEExampleaps A-B-*_--C   '], ['sen3tence-'], ['Bg'], ['    2'], ['ExxA-xEa'], ['                   '], ['mplExa'], [' Big gaps    between words   Big         in thce  '], ['ttse3n           3tencehhce'], ['EEpxample'], ['A-gapsB-**_--C'], ['pBig gap        mples    between wo rds    in thce'], ['  Big            Exaple   2'], ['m'], ['sce'], ['EEpxampl'], ['xExxEA-xEa'], ['2xa'], ['ExamExaplae'], ['mmpleEmexample  Big gaps    between words   o in thce          1'], ['Big 3tenceds    in thce'], ['gap'], ['   A-B-*---a-a-a---b-b-b-c-c-c---_--C   '], ['ExamEA-gapsB-*_---Caple'], ['isenn3tenncein '], ['   le    '], ['me'], ['ggasen3tenceinp'], ['Ex    Examplxe 2xa'], ['BWnnX'], ['EEpxampl     '], ['tthhcewords'], ['A-_B--*_--C'], ['    le    '], ['EEx  a'], ['     gA-B-*---a-a-a---b-b-b-c-c-c---_--CEExampleaps A-B-*_--C   '], ['bet'], ['  Big   Exa 1 2 2\nmple\tExample   3        '], ['mpl   A-x   '], ['thh'], ['   x Example   2'], ['mplExa 1 2 2 mpsen3tenEExceees'], ['A-gapsB--**_--C'], ['  Big gaps    between words    A-xin thce      fKqrpAGA'], ['   x Example   2gap'], ['A-gapsB-'], ['mm'], ['Big gaps    bet ween words    in this senbtence'], ['3tenceds'], ['2e'], ['     gaps A-B-*_--C  msen3tenceinp thce'], ['     gaps A-B-*_--C  msen3tenceinp thcae'], ['mpscelle'], ['se3n'], ['Exaa'], ['    A-gapsB- '], ['EEExa 1 2 2 mpl  Big            ExamExaple   2e'], ['ExamExbetweenlae'], ['   Exa 1 2 2\nmple\tE  Big gaps    between words   o in thce          xample   3'], ['isenn3tenncein'], ['     ExampleEx    Example 2xa 2'], ['BWn  Big        XAh'], ['ExampleEx'], ['ggasen3tenceinpsce'], ['Big gaps    bet ween words    in this senbtenc   A-gapsB- e'], ['   x ExamEEpxample 2'], ['  in thce          '], ['2Big gaps    between words    in thcee'], ['tbet'], ['sen3tencte'], ['A-gapsB--**_--C Big gap        mples    between words    in thce'], ['Big gaps    between wocrds     in this sen3tence'], ['  Big   1 2 2\nmple\tExample   3 '], ['sen3tenecein'], ['2xExa 1 2 2 mpsen3tenceea'], ['A-gaps-B-*_*--C'], ['isennmpsen3tencee3tenncein '], ['mpsen3tenceeees'], ['mpsent3tencee2xa'], ['A-gapsB--**_--C Big gap        mples    between words    in thceEExample'], ['betmples'], ['  Big ga ps    between words    Big gaps    between words    in this sen3tencein thce          '], ['Exa 1 2 2 mpsen32tencee'], ['Big gaps    between words   '], ['pBiggap'], ['mpsen3tenEExceees'], ['rds'], ['BiBgg'], ['mmpleExample  ExampleEx1'], ['mmpl  Big gaps    between words   o in thce          eExample  1'], ['   ExampExaplele  1 '], ['Big gaps  A-gapsB--**_--C Big gap        mples    between words    in thce  between words   '], ['Exa 1 2 2  ampsen3tencee'], ['mplle'], ['se3n   A-gapsB- -C   '], ['Big gaps    between words    in this sen3tenwce'], ['tthhwords'], ['pBig gap        mples in thce'], ['am    A-gapsB- ExamExaple'], ['BWnXsenbtenceAhX'], ['CWSrjljyFR'], ['Big gaps    bet weens    in this senbtenc   A-gapsBmplExa 1 2 2 mpsen3tenEExceees- e'], ['amplmmpleExample  ExampleEx1'], ['ttse3n           3tencehhce    Example   2'], ['gaa'], ['    Ethcele  1 '], ['    Example  2'], ['th   Exa 1 2 2\nm3s'], ['   Exa 1 2 2\nmple\tE  Big gaps    betwe2Big gaps    between words    in thceeen words   o in thce          xample   3'], ['e'], ['   ExampExaplelea  1 '], ['A-gapsB--**_--C Big gap        mples    between words n   in thce'], ['sen3tenc  Big gaps    between words   o in thce          te'], ['weens'], ['   A-B--*_--C   mExampleplExa'], ['mExampleplExa'], ['th   Exa 1 2 2\nmple\tExample   3smp'], ['wse3n3ntenceor'], ['eExample'], ['Exa    ExampExaplele  1 1 2 2  ampsen3tencee'], ['isennmpsen3tencee3tennceinbet'], ['se3n   A-gap -C 3  '], ['mmpleExample gA-B-*---a-a-a---b-b-b-c-c-c---_--CEExampleaps ExampleEx1'], ['bets'], ['mp'], ['   A-Bb-c-c-c---_--C   '], ['EEpx'], ['   A-B-- *_--C    mplExa'], ['ExamEA-gapsB-*_a--m-Cap'], ['  Bi           Exaple   2'], ['pBig gap   *_--C     mples    between wo rds    in thce'], ['BWnX         Ah'], ['xExxEA-xEaExae'], ['sen3tenc'], ['mmpleExample p 1'], ['tthh'], ['isennmpsen3teEExampEle    Example  2ncee3tennceinbet'], ['  a                 '], ['  Big gaps    between wordae      fKqrpAGA'], ['BWnX         mmpleExample p 1Ah'], ['     Ethcele  1 '], ['ebS'], ['A-gaps-B-*_*s--C'], ['eaxa'], ['rrds'], ['sece-'], ['pBig gap   *_--C     mples    bet   A-gaps-B-*_*--C   ween wo rds    in thce'], ['A**_--C Big g ap        mples    bempl   A-x   hce'], ['t Biig gaps    between wordshis    in thce  his'], ['ExamExaEple'], ['     Example   2mpsen3tenceea   '], ['BWnXAxExxEA-xEaExaeX     Ethcele  1 '], ['ps'], ['a'], ['isennmpsen3tencee3tennceintbet'], ['ExampExaplelea'], ['   Exa 1 2 2\nmple\tE  Big gaps    betwe2Big gaps    between words xExxEA-xEaExae   in thceeen words   o in thce          xample   3'], ['pmp'], ['n           3tencehhce'], ['rNfUBspa'], ['     Epxample   2   '], ['wocrds'], [' Ex    Examplxe 2xaA-B-*_--C   mplExa'], ['rNfteUBspa'], ['Bigmpsent3tencee    in this sentence'], ['esen3tencempsen3tenEExceee3s-'], ['        mpl  Big            ExamExaple   2e'], ['EEEpx'], ['t Biig gaps    between wordshis    in thce t his'], ['   x xample 2'], ['betmeples'], ['th   Exa 1 2 2\nm3sBig gaps    between words    in thce'], ['te'], ['  Big            ExamExaple   2ExamExbetweenlae'], ['XRSIx'], ['BWnXAXhX'], ['     A-gapsB-    ExamEEpxamplemplExa'], ['  Big   1 2 2\nmple\tEx2ample   3 '], ['A-gapsB-B*_--C'], ['th   Big     gaps    bet ween words    in this senbtenc   A-gapsB- eExa 1 2 2\nmple\tEx  3smp'], ['mpsece-lExa'], ['tth'], ['  mpsent3tencee                 '], ['ExagmEA-gapsB-*_---Caple'], ['ggasen3tenp'], ['mmpleEsen3tenc  Big gaps    between words   o in thce          temexample  Big gaps    between words   o in thce          1'], ['m3sBig'], ['Exa 1 2 '], ['BWnXhceAh'], ['smpl   A---a-a-a---b-b-b-c-c-c----x   ece-'], ['XBWX'], ['A-B-*_-C'], ['  Big gaps    betwneen words   o in thce      '], ['  a                  '], ['sp'], ['mpsen3tenEExceees-'], ['EExampEle'], ['BWnXAXhEEpxamplX'], ['3tencehhce'], ['   A-B--*mm_--C   mExampleplExa'], ['     gaps-- C  msen3tenceinp thcae'], ['Exa 1 2 2 m psen3tencee'], ['lmmple'], ['secn3tExa 1 2 2 mpsent3tenceeencte'], ['Exaisennmpsen3tencee3tennceinbet1 2 '], ['   Exa 1 2 2\nmple\tE  Big gaps    betwe2Big gaps    between words xExxEA-xEaEhxae   in thceeen words   o in thce          xample   3'], ['    Examaple  2'], ['tben            3tencehhcebt'], ['betmEx    Example 2xaples'], ['ebBig gaps    between words     in this sen3tenceetween'], ['A-B-*---a-a-a---b-b-b-c-c-c---_--C'], ['senbtenc'], ['BWn i Big         XAh'], ['mmpleEsen3tenc'], ['Examplxe'], ['th   Exa 1 2 2\nmple\tExampale   3smp'], ['tthhX'], ['sen3tenwce'], ['EExEampEle'], ['mpsen33tenceees'], ['  e A-B--*mm_--C   mExampleplExa'], ['tthhrwords'], ['ebese3n   A-gap -C 3  tsExxEa'], ['Big gaps    between words    in this sebSentencte'], ['     x ExamEEpxample 2  Example 2'], ['Ex2ample'], ['betms'], ['  Big gaps    betweentthhcewords words   o in thce      '], ['smpl   A---a-a-a---b-b-b-c--c-c----x   ece-'], ['m    le    ple'], ['BWnXpAXhEEpxamplX'], ['mmpleEsen3tenc  Big gaps    beBWnX         Ahtween words   o in thce          temexample  Big gaps    between words   o in thce          1'], ['gga   A-x   sen3tencce'], ['pl   A-B-*_--C  Big gaps    between words    in this sen3tence- ee'], ['mpsen3ttenceemmpleExample  1s'], ['mpsecmpscellee-lExa'], ['plmmple'], ['lmmpletthhcewords'], ['wo  Big            EEExample  1ds'], ['Big gaps    between words    in s sentence'], ['am'], ['Big gaps    bet ween words    in tsentence'], ['epBig gap        mples in thce'], ['psen3tencee'], ['A-gapsB--**_s--C'], ['Big gaps    between words    iExaen this sen3tenwce'], ['th   Exa 1 2 2\nmmple\tExampale   3smp'], ['meaxaplle'], ['   Exa 1 2 2\nmple\tE  Big gaps    betwe2Big gapmpsen3tenEExceees-between words xExxEA-xEaExae   in thceeen words   o in thce          xample   3'], ['pBgig'], ['A-gap--**_s--C'], ['mmmpleExample'], ['mExa 1 2 2 mpl  Big            ExamExaple   2ee'], ['ExampleEx1'], ['ggasenp3tenp'], ['XBWXX'], ['betwneen'], ['2hcee'], ['BWnplX'], ['2xExa'], ['pBgiBg'], ['EA---a-a-a---b-b-b-c-c-c----x2 mpsent3tencee'], ['t Biig gaps  e  between wordshis    in thce  his'], ['Big  gaps    between words    in this sen3tence'], ['bteet'], ['mpsen33temmpleEmexample  Big gaps    between words   o in thce          1nceees'], ['BWnAXAh'], ['BWnXAXhEEpxampllX'], ['senbtence'], ['ampl3tencehhcele'], ['mfKqrpAGAlpleE1'], ['   A-gaps-B-*_*Bigmpsent3tencee    in this sentence--C -  '], ['  Bigi        '], ['mmpleExA-_B--*_--Cample p 1'], ['   Exa 1 2 2\nmple\tE  Big gaps    betwe2Big gaps    between words xEx     xEA-xEaExae   in thceeen words   o in thce          xample   3'], ['smpl   A---a-a-a---bisennmpsen3tencee3tenncein-b-b-c--c-c----x   ece-'], ['A-Bb-c-c-c---_--C'], ['tbsenbtencet'], ['Big gaps    bet weens    in this senbtenc   A-gapsBmplsExa 1 2 2 mpsen3tenEExceees- e'], ['Exaisennmpsen3tencee3tennceinbet1'], ['   xExxEA-xEaExae  Ethcele  1 '], ['Bmpsent3tenceetween words   '], ['A-Bf-*_-mfKqrpAGApleE1C'], ['crdsExamplxe'], ['betmEx    Epxample 2xaples'], ['A-gapsBmplsExa'], ['mmmp'], [' Big gaps    between words   Big         in '], ['   A-B--ExamEA-gapsB-rNfUBspa*_---Caple*_--C   mplEx'], ['mpsen33temmpleEe          1nceees'], ['senbteenc'], ['ExapleEx'], ['thisebBig'], ['mpl   A-C-x   '], ['EamExbetwe    Ethcele  1 enlae'], ['Exa 1 2 2 mpExample  1  Big        sen3tencee'], ['ebBigmp'], ['pBig gap   *_--C     mples    ebSbetween wo rds    in thce'], ['E   Ethcele  1 enlae'], ['mmmm'], ['mpsen3ttenceemmpple'], ['1nceees']]
    results = ['Example', 'Mudasir_Hanif_', 'Yellow_Yellow__Dirty__Fellow', 'Exa-mple', '-Exa_1_2_2_mple', 'Hello,-world!', 'happy_123', 'Hey-there!', '__spaces__every__where__', 'NoSpacesHere', 'This_is__a__test', 'Testing-1__2-3', 'Hello_World', 'Hello-World', '-Hello_World', 'This_is__a__tesst', 'This_is__a__tes', 'This_is__a_This_is__a__tes_test', 'Hello_r__World', 'This_is__a_Hello_r__World_tsesst', 'This_is__a_This_is__a__tes_test__spaceNoSpacesHere_', 'Thish_is__a__tesst', 'HelloNoSpacesHere,-world!', 'Hey-e_there!', '__spaces__eveThis_is__a_This_This_is__a_This_is__a__tes_test__spaceNoSpacesHere_is__a__tes_testry__where__', 'happy_123__spaces__every__where__', '__spaces__eveThis_is__a_This__This_is__a_This_ishappy_123__a__tes_test__spaceNoSpacesHere_is__a__tes_testry__where__', 'Hello_r__Word', 'This_is__a_sst', '__spaces__eveThis_is__a_This_This_is__a_This_is__a__tes_test__spaceNoSpacesHello_r__WorldHere_is__a__tes_testry__where__', '__spaces__eveery__where__', 'happy1233', '__spaces__eveThis_is__a_This_This_is__a_This_is__a__tes_test__spaceNoSpacesHeNoSpacesHerello_r__WorldHere_is__a__tes_testry__where__', 'happy_123_p_spaces__every__where__', '__spaces__eveThis_is__a_This_This_is__a_This_is__tes_testry__where__', 'Thish_isThis_is__a_Hello_r__World_tsTesting-1__2-3_a__This_is__a_ssttesst', 'Helleo_World', 'happyw_123_p_spacees__every__where__', 'Thish_is__a__tesHey-there!st', 'happyw_123_p_spacees__This_is__a_sstevery__wher__', '__spaces__every__w_here__', 'Th_is_is__a_This_is__a__tes_test', 'This_is-a_This_is__a__tes_test__spacoeNoSpacesHere_', '__spaces__eveThis_is__a_This__This_is__a_This_is_happy_123__a__tes_test__spaceNoSpacesHere_is__a__tes_testry__where__', 'Thihappyw_123_p_spacees__This_is__a_sstevery__wher__s_is__a_Hello_r__Woreld_tsesst', '__spaces__eveThis_is__a_This_This_is__a_This_is__a__tes_test__spaceNoSpacesHtry__where__', 'happThis_is__a__tessty', 'This_is__a_T__spaces__eveThisTh_is_is__a_This_is__a__tes_test_is__a_This__This_is__a_This_ishappy_123__a__tes_test__spaceNoSpacesHere_is__a__tes_testry__where__his_is__a__tes_test', 'This_is_Thish_is__a__tesHey-there!st_a_This_is__a__tes_test__spaceNoSpacesHere_', 'Thish_is__asst', '__spaces__everThis_is__a_This_is__a__tes_testy__where__', 'This_is__This_is__a_T__spaces__eveThisTh_is_is__a_This_is__a__tes_test_is__a_This__This_is__a_This_ishappy_123__a__tes_test__spaceNoSpacesHere_is__a__tes_testry__where__his_is__a__tes_testa__tes', '__spaces__eveThis_tis__a_This_This_is__a_This_is__a__tes_test__spaceNoSpacesHere_is__a__tes_testry__where__', '__spaces__eveThis_is__a_This_This_is__a_This_is__a__tes_test__spaceNoSpacesHello_r-WorldHere_is__a__tes_testry__where__', '_happyw_123_p_spacees__every__where__', 'happyw_123_p_spacees__This_is__a_sstevery__whser__', '__spaces__eveThis_is__a_This_This_is__a_This_is__a_This_is__a__tes_test__spaceNoSpacesHere_This_is__tes_testry__where__', 'haappy1233', 'Testing-Hey-e_there!__1__2-3', 'Hello_r-spaces__eveThis_is__a_This_This_is__a_This_is__a__tes_test__spaceNoSpacesHello_r-WorldHere_is__a__tes_testry__where-Word', 'Testing-s__1__2-3', 'Th_is_is__a_This_is__a__tes_teHello,-world!st', '', 'ThThis_is__a_Hello_r__World_tsesstis_is__a_sst', 'This_is__This_is__a_T__spaces__eveThisThh_is_is__a_This_is__a__tes_test_is__a_This__This_is__a_This_ishappy_123__a__tes_test__spaceNoSpacesHere_is__a__tes_testry__where__his_is__a__tes_testa__tes', 'This_is__sst', 'NoSere', 'ThTthis_is__a_Hello_r__World_tsesstis_is__a_sst', 'This_is__a_This_is__a__tes_test__spaceNioSpacesHere_', 'This_iis__a_sst', 'Thihappyw_123_p_spacees__Thi_s_is__a_sstevery__wher__s_is__a_Hello_r__Woreld_tsesst', 'This_is__a_This_istest', 'Helleo_Worldhappyw_123_p_spacThis_iis__a_sstees__every__where__', 'Hello_r__Worlld', 'Testing_This_is__a_sst__e_there!__1__2-3', 'ere!st', 'This_is__a_This_is__a__t__spaces__eveThis_is__a_This_This_is__a_This_is__a_This_is__a__tes_test__spaceNoSpacesHere_This_is__tes_testry__where__est', 'Hhappy_123_p_spaces__every__where__ello_r__Word', 'He__spaces__eveThis_is__a_This_This_is__a_This_is__a_This_is__a__tes_test__spaceNoSpacesHere_This_is__tes_testry__where__llo,-wod!', 'rCMrcvK', 'This_sis__a__tes', '__spaces__eveThis_is__a_This_This_is__a_This_is__a_This_is__a__tes_test__spaceNoSpacesHere_This_is__tes_testr__where__', '__spaThis__This_is__a_This_ishappy_123__a__tes_test__spaceNoSpacesHere_is__a__tes_testry__where__', 'Th_is_is__a_This_is__aHey-e_there!__tes_test', 'Thish_Helleo_Worldhappyw_123_p_spacThis_iis__a_sstees__every__where__is__a__tesHey-there!st', 'Hello_r-spaces__eveThis_is__a_This_This_is__a_This_is__a__tes_test__spaceNoSpacesHellThish_isThis_is__a_Hello_r__World_tsTesting-1__2-3_a__This_is__a_ssttessto_r-WorldHere_is__a__tes_testry__where-Word', 'Th_is_is__a_This_is__a__tes_teTHello,-world!st', 'ThTthis_sis__a_Hello_r_', 'Thihappyw_123_p__spaces__eveThis_is__a_This_This_is__a_This_is__a__tes_test__spaceNoSpacesHtry__where-spacees__This_is__a_sstevery__wher__s_is__a_Hello_r__Woreld_tsesst', '__spaces__everThis_is__a_This_is__a__tes_tThish_Helleo_Worldhappyw_123_p_spacThis_iis__a_sstees__every__where__is__a__tesHey-there!stesty_where__', 'NoSer', 'Thish_Helleo_Worldhappyw_123_p_spacThis_iis__a_sstees__every__where__ishappy_123_p_spaces__every__where-a__tesHey-there!st', 'Hello_rr__Word', 'Hello_r-spaces__eveThis_is__a_This_This_iThis_is__Hey-e_there!a_This_is__a__tes_tests__a_This_is__a__tes_test__spaceNoSpacesHellThish_isThis_is__a_Hello_r__World_tsTesting-1__2-3_a__This_is__a_ssttessto_r-WorldHere_is__a__tes_testry__where-Word', 'HeThis_is__a_This_istestlWlo_World', 'NoS', 'Testing-Hey-e_there!__1__2_This_is__a_This_is__a__tes_test__spaceNoSpacesHere-3', '__spaces__eveThis_is__a_This_This_is__a_This_is__a_This_is__a__tes_test__spaceNoSpacesHere_This_is__tes_testry__where_', 'NSooSerre', 'Hello_r-spaces__eveThis_is__a_This_This_iThis_is__Hey-e_there!a_This_is__a__tes_tests__a_This_is__a__tes_test__spaceNoSpacesHellThish_isThis_is__a_Hello_r__World_happy_12Testing-s__1__2-33__spaces__every__where__tsTesting-1__2-3_a__This_is__a_ssttessto_r-WorldHere_is__a__tes_testry__where-Word', 'This_is__This_is__a_T__spaces__eveThisTh_is_is__a_This_is__a__tes_test_is__a_This__This_is__a_This_ishappy_123__a__tes_test__spaceNoSpacesHere_is__a__tesHello_r-spaces__eveThis_is__a_This_This_iThis_is__Hey-e_there!a_This_is__a__tes_tests__a_This_is__a__tes_test__spaceNoSpacesHellThish_isThis_is__a_Hello_r__World_tsTesting-1__2-3_a__This_is__a_ssttessto_r-WorldHere_is__a__tes_testry__where-Word_testry__where__his_is__a__tes_testa__tes', 'Helo_r__Worlld', '_happyw_123_p_spacees__every__whhere__', 'HTh_is_is__a_This_is__a__tehappy_123__spaces__everyHello_r-spaces__eveThis_is__a_This_This_is__a_This_is__a__tes_test__spaceNoSpacesHello_r-WorldHere_is__a__tes_testry__where-Wordo,-world!stey-!', 'Thish_isThis_is__a_Hello_r__World_tsTesting_3_a__This_is__a_ssttesst', '-Exa_1_2_2\nmple\tExample-3', '-A-B-*_--C-', '---a-a-a---b-b-b-c-c-c---', 'Big_gaps-between_words-in_this_sentence', '-', '-', '-', 'Exa_1_2_2_mple', 'Example__1', '-Example-2', '-Example-2-Example-2', '__E__Example-2', 'this', '----a-a-a---b-b-b-c-c-c---', '-', 'his', 'words', 'ExampleEthisxa3e__1', 'Exx1', '__his-', 'gaps', 'ggaps', 'ggga', '__his-', '-Ex-2\nmple\tExample-3', '---a-a-a---b-b-b-c-c-c----', 'Example-Example-2-Example-2__1', 'A-B-*_--C', 'EEx', 'Exa', '-A-B-*_-E-C-Ex-2\nmple\tExample-3', '---a-ac-c----', 'ExampleEthisxa3e', '__his-', '2', 'in', '__E__Egapsxample-2', '__ExampleE__Expample-2', '-Exa_1_2_Exa2\nmple\tExample-3', '__E__Ega_psxample-2---sa-ac-c---', 'ExampleeEthisxa3e', 'zPb', 'ExampleEt__E__Ega_psxample-2---sa-ac-c---hisxa3e', 'hsis', '__E__Example__2', '-A-B-*_-E-C-Ex-2\nmple\tExample__m_3', 'EExample__1Ex', '__his-EExample', 'psxample', 'ExampleEthitsxa3e', '1', '----a-aa-a---b-b-b-c-c-c---', '---a--a-a---b-b-b-c-c-c---', 'hsExampleEthisxa3es', 'Expample', 'his__ExampleE__Expample-2', 'sentence', 'Exa2', '-Exa_1_2_2\nmple\tExample-2---sa-ac-c---', '-Exa_1_2_Exa2\nmple\tEx3', '-', '-Exa_1_2_2\nmple\tExample_3', 'ExampleEtEhisxa3e__1', '-E__Ega_psxample-2---sa-ac-c---_A-B-*_-E-C-Ex-2\nmple\tExample-3', 'hsE2xampleEthisxa3es', 'Example-Example-2-Examle-2__1', '__hExampleEthitssxa3eis-EExample', '-EEx', 'thits', '----a-a-a---b-b-b-c-c-c---ExampleEtEhisxa3e', '---a-ac-c---', '-psxample_EEx', 'E', '-his-A-B-*_--C-', 'TnYIFZqaAz', 'between', 'zEx3Pbb', 'gs', '-', '---a--a-a---b-b-b-c-c--c---', '-Ex-2\nmple\tExample-3i', '-Exa_mpleample-3', '__hismpleample-', 'thitts', 'ExampleEt__E__Ega_psxample-2---sa-ac-c---h-isxa3e', '__', '__his__hismpleample_', '---a--a-a---b-b-b--c-c-c---', 'word', 'thi__E-Exa_1_2_2\nmple\tExample_3__2', '---a-ac--A-B-*_-E-C-Ex-2\nmple\tExample-3c---', 'Exampl-eEthishiExamlesxa3e__1', '_Exx1-', 'ggap', '__hExampleEthitssxa3eis-EExampple', 'E__x3', '__his__h__hismpleample-ismpleample_', 'R', '-Ex-2\nmple\tExample-ExampleEi', 'ExampleEtEhisxa3e__1gggaps', 'hsExmampleEthisxa3es', 'ExaxmpleEthitsxa3e', '-Exa_1ExampleEtEhisxe__1gggaps-3', 'gss', '-', 'hhis', 'gggga', 'Exampl', 'ExampleEtExampl-eEthishiExamlesxa3e__1', '-his-A-B-*-_--C-', 'ExampleEtExampl', 'hhi---a-a-a---b-b-b-c-c-c---s', '---a--a-a---b-b-b-c-c--', 'Big_gaps-between_words-i2---sa-ac-c---n_this_sentence', 'Exam-Example-2pleEtEhisxa3e__1', '2---sa-ac-c---', '11', 'dwords', 'betweeExampleEthisxa3e__1n', 'hhi---a-a-a---__E__Ega_psxample-2---sa-ac-c---b-b-b-c-c-c---s', 'E__E2---sa-ac-c---b-b-b-c-c-c---sx', 'hhi--his-A-B-*-_--C---a-a-a---', 'hsExampthitsleEthisxa3es', 'ismpleample', 'hhi---a-a-a---', 'hsExampleEtheisxa3es', '-Exa_mp__leample-3', 'ExampleEt__E__Ega_psxample-2---sa-ac-c---h-isx', 'EleEatEhisxa3e__1', '__hs', '---a--a-a---b--psxample_EExb-b-c-c--', 's', 'ExExamplampleEthisxa3e', '-his__h__hismpleample-ismpleample_', '---a-ac-ca---', '__hExa__hsmpleEthitssxa3eis-EExample', 'A-B-*___hExampleEthitssxa3eis-EExampple-E-C', 'ExExamplampleEt__E__Example-2hisxggggaa3e', '---a-a-a----c----', 'Exampitsxa3e', '----a-a-a---b-hsmpleEthitssxa3eisb-b-c-c-c---', 'thtis', '---a-ac-c-thitts-', 'hihis', '---a-a__ExampleE__Expample-2__3c---', 'wo', 'Exaword', 'thhisis', 'hhi-', '-his-A-B-*_-E-C-Ex-2\nmple\tExample__m_3thitssxa3eis-EExample-C-', 'zPPb', 'EExampple-E-C', 'E__c-c-c---sx', 'i2---sa-ac-c---n', '-his-Exx1---C-', 'ExampleEtEhisxa3e', 'hhi---a-a-a---c-c---s', 'Exmpl', '3', 'Rhsis', 'sjRboRkSy', '2---sa-ac-c---h-isx', 'mples', 'Exa3c---leEtEhisxa3e', 'hsE-his-Exx1---C-xmampleEthisxa3es', 'i2---sa-a-c-c---n', '-Exa_1_2_Exa2\nmpl', 'thi', 'hsExampleExthisxa3es', 'hh', 'hhhis', 'hsE-his-Exx1---C-xmampleEthis-Exa_mp__leample-3xa3es', 'EExample-C', '2__2-', '2---sa-ac-c---h-isxa3e', '3xa3es', 'his__ExampleE__E3thitssxa3eisxpample-2', 'Exam', '---a-ac--A-B-*m_-E-C-Ex-2\nmple\tExample-3c---', '2----sa-ac-c---', 'thhiss', 'wodhhi-s', 'FoFlZTDagW', '-Exa_1_2_2\nmple\tExBig_gaps-between_words-i2---sa-ac-c---n_this_sentenceample_3', 'ExampleEtExpampl', '-Exa_1_2_2\nmple\tExa---a-ac-mple_3', '-Exa_mp__leample-3Example__1', 'Exa---a-ac-mple', 'sgs', '---a-thits-a-a---b-b-', 'xmampleEthisxa3es2__ExaxmpleEthitsxa3e3c---', 'his__ExampleE-2', '__---a-ac-c----Example-2', '3c---', 'ggagp', 'EFoFlZTDagWE', 'hs', '_p_ExaxmpleE__Expample-2', '111', 'ggagExampleEtEhisexa3gep', '-Exal_mp__leample-3', 'gapshhi---a-a-a---__E__Ega_psxample-2---sa-ac-c---b-b-b-c-c-c---s', 'ga_Exx1-s', '---a-a-a----c---', 'wwo', '-Exa_1ExampleEtEhmisxe__ggaps-3', 'A-B-*', '-Example-2-Example_words__2', '_Ex3__Ex-2\nmple\tExample-3i', 'thhi', 'iin', '--a-a-a---', 'his__ExapmpleE__E3thitssxa3eisxpample-2', '---a-ac-c-a---', 'jgOtGgdMm', 'ExampleEt__E__Ega_pshhi---a-a-a---b-b-b-c-c-c---sxample-2---sa-ac-c--11-h-isx', '1gggaps', '-E__c-c-c---sxxample_EExb-b-c-c--', 'hhi-hhh', '-Exa_1gaps-3', 'hsExampleExthi__hssxa3es', '----a--a-a---b-b-b-c-c--c---', '_p_Exax__Expample-2', 'ExExameplampleEthisxa3e', 'thi__E-Exa_1_2_2\nmple\tExampExampleEtle_3__2', 'hsmpleeEthishiExamlesxa3eEthitssxa3eis', '---a-a-aExampleEt__E_-c---hisxa3e--c---', '__hExampxleEtEhisxa3e__1ile', 'EleEatEhisxa3e', 'ExampleEi', 'wo_--C', 'Exampl-eEthish_iExamlesxa3e__1', 'c-c-c---sxxample', '-Exple-3', '__his_', '-hi_s__h__hismpleample-ismpleample_', 'gapshhi---a-a-a---__E__Ega_psxample-2---sa-ac-c----b-b-b-c-c-c---s', '__E__Ega_psxa-Ex-2\nmple\tExample-3mple-2---sa-ac-c---', 'A-B-*_', '-his-Exx1---C-', 'sentenceample', 'ggs', '-Example-2-Example-2-Exa_1ExampleEtEhisxe__1gggaps-3', 'c-c-c----sx', 'hsmpleEthitssxa3eis', '__his__hi2hisxggggaa3e_', '----a-ac-c-thitts-', '2-2-', 'Ex3ampleEtEhisxa3e__1', 'his__Exam-A-B-*_-E-C-Ex-2\nmple\tExample__m_3pleE__mE3thitssxa3eisxpample-2', '-Ex-2\nmple---a-a-a----c---\tExample__eEi', '-Exa_1_2_2\nmple\tExBig_gaps-between_words-i2---sa-ac-c---n_this_sentenceeample_3', '-E', '---a--a-a---b-b-Example__1-c--c---', '__E__Ega_psxample-2---sa-ac-c-__E__Example-2--', '_Exx-Ex-2\nmple\tExamhhple-3i1-', 'hsExampleExthi__hssxA-B-*_--Ca3es', '-his-A-B-*-3i1__--C-', 'E2---sa-ac-c---b-b-b-c-c-c---sx', '__E_2_Example-2', 'A-B*--*_--C', 'gapshhi---a-a-a---', 'thi__E-Exa_1_2_2\nmple\tExampExamplE__c-c-c---sxeEtle_3__2', 'cc-cggs-c---sxxcample', 'hhi---a-a-a---b-b-b--c-c-c---s', 'sggs', '__EExb-b-c-c--__Example-2', 'ss', '-Eexa_1_2_2\nmple\tExample_3', 'gapshhi---a-2---sa-ac-c---hisxa3e---', 'mple---a-a-a----c---', 'xmampleEthisxa3es', 'ggss', 'E_E_x3', 'sjRboRkS', '__his-hi2hisxgEleEatEhisxa3egggaa3e_', 'EEE', 'ExampleEtExampl-eEthishiExamlesxa3e__e1', 'hhh', '-his-', '22--', '-3', '---a--a-a---b-b-b-c-bismpleample', 'c-c-c---sxxamplthi__E-Exa_1_2_2\nmple\tExampExampleEtle_3__2e', '-A-B-*_-E-C-Ex-2\nmple\tExamp1gggapsle__m_3', 'Examle', '-Example-2-Example_words__22', 'tshitts', '2---sssa-ac-c---h-isxa3e', 'his__ExExampl-eEthishiExamlesxa3e__1ampleE__Expample-2', 'Examhhple', 'hsE', 'hisExampBig_gaps-between_words-in_this_sentenceleEthisxa3es', 'ExampleEtEhisx', 'senteExamplnce', '_p_ExaxmpleE__Expample_a__2', 'dwoc-c-c---sxeEtlerds', 'Exal', 'hsmpleeEthishiExame1lesxa3eEthitssxa3eis', 'E_sc-c-c---sx', 'worrd', 'Exam-Example-2pleEA-B-*_-E-CtEhisxa3e__1', 'Eexa', 'betweeExasxa3e__1n', 'sss', 'ExampleEtEhis3xa3e', '-A-B-*_-E-C-Ex-2\nmple\tExampsenteExamplnce1gggapsle__m_3', '2---sa-ac-c-Exax--', 'Eampl', 'IclExampleEthisxa3e__1', '---a--a-a---b-b--Example__1-c--c---', 'bet3e__1n', '---a-a--a----c---', 'hsExampleExthi_ExampleEi_hssxA-B-*_--Ca3es', 'EExx', 'IclExample', 'fwlMxhGm', '_sentenceleEthisxa3esc-c---', 'hjnY', '2-2', '2hsExampleExtEleEatEhisxa3e__1hi2--', 'ga', '-Example-2-Exampxle-2', 'ExamxpbetweeExasxa3e__1nl', '---a-thits-a-a-_sentenceleEthisxa3esc-c-----b-b-', 'ybsTcN', 'dw-his-ords', '2---sa-ac--c---', 'htsExampthitsleEthisxa3es', 'hsihis', 'ihihis', '__E__ExaExx2', '---a-thits-a-a-_sentenceleEthisxa3esc-c-----bggagp-b-', 'EExampple', 'Exmp---a--a-a---b-b-Examplel', '_sRentenceleEthisxa3esc-c--', '--', 'ExampleEmtExampl-eEthishiExamlesxa3e__e1', '__ExampleE__Expamplp2', '---a-thits-a-a-_sentenceleEthisxa3esc-c-----his__ExampleE__Expample-2b-b-', 'Exampthhisisa3e', '--C', 'KsMcxuu', 'ce-c-c---sxxample', '22__2-', '_--C', 'EExpampl', 'xmamspleEthisxae3es', '-ExapmpleEc-thitts-', 'his__Exam-A-B-*_-E-C-Ex-2\nmple\tExample__m_3pleE__mE3thitssxa3ei-2', 'ple', '3Example-Example-2-Example-2-Exa_1ExampleEtEhisxe__1gggaps-3', 'ExampleEtExampl-eEthishiExamlesxa3e_p_e1', '1gapszzPPb', 'DQaiLlVsgN', '-his-A-B-*_-E-C-Ex-2\nmple\tExample__m_3thitssxa3eis-EExample__hismpleample--C-', 'ExamplhsEteEthitsxa3e', 'ExampleEt__E__Ega_psxample-2---sa-abetweeExasxa3e__1n-isx', 'Ku-A-B-*_-E-C-Ex-2\nmple\tExample-3Mcxuu', 'ssgs', '---a-thits-a-a-_sentenceleEt_p_ExaxmpleE__Expample_a__2-b-b-', 'ExaxmpleEthitsxa3e3c---', 'ExampleEt-E__Ega_pshhi---a-a-a---b-ggsb-b-c-c-c---sxample-2---sa-ac-c--11-h-isx', 'sentenceleEthisxa3esc-c---', 'thmple', 'ssss', 'cc-cggss-c---sxxcample', 'Ku-A-B-*_-E-C-Ex-2\nmple\tExample-cc-cggs-c---sxxcample3Mcxuu', '__hExampleEthitssxa3eis_Ex3ampleEtEhisxa3e__1-EExample', 'sentenceleEthisxa3esc-c-----his', '3Mcxu-u', 'gsss', '-A-B-*_-E-C-Ex-hismpleamplegapsle__m_3', '---a-thits-a-a__his----b-b-', 'zExmplPb', 'EExammle', '---a-a__ExampleE__Exp-ample-2__3c---', 'EF2---sa-ac-c--11-h-isxoFlZTDagWE', '__his_EF2---sa-ac-c--11-h-isxoFlZTDagWE', 'hExampleEthitssxa3eis', 'hsExampaleEtheisxa3es', 'h', 'T', '_wo_--C', '2hsExampleExtEleEatEh-isxa3e__1hi2--', 'A-B---C', '2hsExampleExtEleEatEh-is-', '-Ex-2ple-3i', 'his__ExampleE-2', '__his-ExampExampleEtle_EExample', 'mE3thitssxa3eisxpample', '-his-A-B-*_-E-C-Ex-2\nmple\tExample__m_3thitssx-A-B-*_-E-C-Ex-2\nmple\tExample__m_3a3eis-EExample-C-', 'c-c-c---sxxamplthi__E-Exa2_2\nmple\tExampExampleEtle_3__2e', '-his-Exx1_Exa2--C-', '2pleEtEhisxa3e', 'xal', '-Example-2-Example_words__22', 'Examxpbetw--CeeExasxa3e__1nl', 'hhi---a-a-a---b-b-bKu-c-c-c---s', '2----sa-aciin-c---', 'rpfY', 'c-c-c---sxeEtle', '---a--a-a---b-b-Example', '----a-aa-a2-b-b-c-c-c---', 'Examxpbetweel', 'ExampExamplE', 'wodhhi-ws', '1ileExBig', '_ExampleEtEhisx__Exa_mp__leample-3', '2hsExampleEis-', 'zExmbplPb', '2__2---a-a--a----c----', '----a-a-a---b-b-b-c-c-c---ExamplceEtEhisxa3e', '2---sa-abetweeExasxa3e', 'Ega', '_ExampleEtEhis__his-ExampExampleEtle_EExamplex__Exa_mp__lmeample-3', '---a--ba-a---b-b-b-c-bismpleample', 'beteweeExasxa3e__1n', 'Exa1ExampleEtEhmisxemple__1', 'hhi----a-thits-a-a-_sentenceleEthisxa3esc-c-----bggagp-b-hhh', '3pleE', 'wordss', '---a-a', 'Exa3c--i-leEtEhisxa3e', 'EExam__E__ExaExx2ple__1Ex', 'hhihh', '---a---b-b-b-c-c-c---ExampleEtEhisxa3e', 'plethmple', 'xalxmamspleEhhhi---a-a-a---b-b-b--c-c-c---sthisxae3es', 'g-his-A-B-*_--C-gs', 'hiss', 'n', 'gsentencele-a---', 'PzPPb', '2---sa-ac---c---', '3Example', '__hjnYExample', '--CC', '---a--a-a---b-', '--CExampleEmtExamplC', 'Examxpbe2-2tw--CeeExasxa3e__1nl', '22EExample-C--', '-his-Exx1---C-d', 'EExc-c-c---sxeEtlepampl', 'ExampleEt__E__Ega_psxample-2---sa-ac-c---hisxa3eE', '1-Exa_1_2_2\nmple\tExBig_gaps-between_words-i2---sa-ac-c---n_this_sentenceample_3aps', 'hExampxleEtEhisxa3e', 'sentenceleEthicsxa3esc-c---', 'mplees', '-Ex-2\nmple\tExample-ExmampleEi', '-Example-2-Example-2-Exa_1ExampleEtEhisxe__1gggaps-3-', 'gW', 'htsExampthitsleEthisxahhi---a-a-a---b-b-bKu-c-c-c---s3es', 'i2---s-a-a-c-c---n', 'sentenceleEt3mplehicsxa3esc-c---', '---a--a-a---b-b-b-c-c----', '__his__h__hismplhsExampleExthi_ExampleEi_hssxA-B-*_--Ca3eseample-ismpleample_', 'wordrd', 'thitExampExampleEtles', '-A-B-*_-E-_C-Ex-2\nmple\t-E__Ega_psxample-2---sa-ac-c---_A-B-*_-E-C-Ex-2\nmple\tExample-3ampsenteExamplnce1gggapsle__m_3', '__E__xaExx2', 'xaE_sentenceleEthisxa3esc-c---', 'zP----a-a-a---b-b-b-c-c-c---ExamplceEtEhisxa3e', 'tsthitts', '3apswd', 'ExExamplampleEt__E__Example-2hisxggaa3e', 'thitteEthishts', 'A-B-*m_-E-C', 'sentenceleEthisxaa3es', 'ExampleEt__E__Ega_psxample-2---sa-ac-c---hisxa3e-C', '3thitssx', '---E__c-c-c---sxxample_EExb-b-c-c----a-a-a---b-b-b-c-c-c---ExamapleEtEhisxa3e', '-Examp2pleEtEhisxa3eExample-2', 's3thitssxa3eis', '-his-A-BA-B-*___hExampleEthitssxa3eis-EExampple-E-C-*-_--C-', '__hExampleEthitssxahsE2xampleEthisxa3es3eis-EExam', '1ampleE', 'mE3tshitssxa3eisxpample', '2---sa-ac-c--__Exx1--h-isxa3e', '-shis-', 'A-B-*mA_-E-C', 'ExExamplampleEt__E__Example-2hisx', 'ithits', '---a--a-a---b--Ex-2\nmple\tExample-ExmampleEib-b--c-c-c---', 'hismpleamplegapsle', 'nn', 'hsE-his-Exx1---CE-xmampleEthisxa3es', 'Exeamggapsle', '_s_ExampleeEthisxa3e', 'ExampsenteExamplnce1gggapsle', 'bExametweeExasxa3e__1n', '---a--a-a---b--Ex-2\nmple\tExample-ExmampleEib-b--cc-c-c---', 'E1ExampleEtEhisxeaEzExmplPbEEE', '-Exa_1ExampleEtEEhmisxe__ggaps-3', 'gaTnYIFZqaAzpshhi---a-a-a---', '2--his-A-B-*_-E-C-Ex-2\nmple\tExample__m_3thitssxa3eis-EExample-C---sa-ac---c---', '-his-A-BA-B-*___hEx__hExampleEthitssxa3eis-EExamppleampleEthitssxa3eis-EExampple-E-C-*-_--C-', 'cc-cggss-c---sxxcgapshhi---a-2---sa-ac-c---hisxa3e----ample', '-A-B-*_-E-C-Ex-2\nmple\tExample__E__c-c-c---sx3', 'ExpampA-B-*_le', '2hsExampleExtEleEasRentenceleEthisxa3esc-c--tE2-2h-is-', 'sRentenceleEthisxa3esc-c--', 'thitExmE3thitssxa3eisxpampleampExampleEtles', 'hisExampBig_gaps-between_words-in_this_sentenceleEthisxa3_es', '-Ex-22\nmple\tExample-3', 'Exa-E', 'hhis2---sa-ac-c---h-isx', '2---sa-ac-c-i--h-isxa3e', '_', '_a_b_c_', '_a__b__c_', '-', '_a-b_c__', 'ABC', '1_2_3', '百度是中国最大的搜索引擎', 'Big_gaps-between_words-in_thce', 'Big_gaps-between_words-in_this_sen3tence', '__Big_gaps-between_words-in_thce-', '-mple', '__Big-', 'mple', '__Big_gaps-between_words-Big_gaps-between_words-in_this_sen3tencein_thce-', '__Big-Example-2', 'Exa_1_2_2_mplle', '-gaps', 'wor__Big_gaps-between_words-Big_gaps-between_words-in_this_sen3tencein_thce-ds', 'thce', 'mmple', '-Example__1_', '-Example_2', 'sen3tence', 'mmpleExample__1', '__Big-ExamExaple-2', 'Big', '-Example-2-', 'Exa_1_2_2_mpsen3tencee', 'ExamExaple', 'Exxa', '-A-BExample-', '_Big_gaps-between_words-in_thce__', 'Big_gap-mples-between_words-in_thce', '-gaps_A-B-*_--C-', 'sen3tencein', 'se3n3tence', 'Big_gaps-between_words-in_this_sen3tence', 'mmpleExample', 'mplExa_1_2_2_mpsen3tenceees', 'Exa_1_2_2_mpl__Big-ExamExaple-2e', 'mmpleE1', '-A-B-*_--C__Big_gaps-between_words-in_this_sen3tence-_', '-A-gapsB-*_--C-', 't_Big_gaps-between_words-in_thce__his', 'Exa_1_2_2_mpExample__1sen3tencee', '__Big_gaps-between_words-in_thce-fKqrpAGA', 'EExample__1', '__Big_gaps-between_words-o_in_thce-', 'th-Exa_1_2_2\nmple\tExample-3s', 'BiBg', 'mfKqrpAGApleE1', 'EExampEle__1', 'BWnXAhX', '-', 'sen3tenncein', 'EExa', 'Ex-mmpleE1-ample__1', 'mpsen3tenceees', '_Big_gap-mples-between_words-in_thce', '-A-gaps-B-*_*--C-', '__Big_gaps-between_words-o_in_thce-', 'Ex-Example_2xa', 'EExample', '-A-gaps-B-*_*s--C-', '-sen3tenncein', '-le-', 'Exa_1_2_2_m', 'tthhce', 'Exa_1_2_2_mpsent3tencee', 'Exa_1_2__2_m', '-A-B-*_--C-mplExa', 'A-gapsB-*_--C', 'BWnXAh', 'fKqrpAGA', 'Exa_1_2_2_mp', 'Big_gaps-bet_ween_words-in_this_sentence', 'se3n3ntence', 'EExa_1_2_2_mpsent3tencee2xa', '-ExampleEx-Example_2xa_2', '-A-B--*_--C-mplExa', 'se3n-3tence', 'Exa_1_2_2_mpl__Big-ExamExa_1_2_2_me', 'ample', 'th-Exae_1_2_2\nmple\tExample-3s', 'BBig', '-A-x-', '-A-gapsB-_', 'ExxEa', '-gEExampleaps_A-B-*_--C-', 'sen3tence-', 'Bg', '-2', 'ExxA-xEa', '-', 'mplExa', '_Big_gaps-between_words-Big-in_thce__', 'ttse3n-3tencehhce', 'EEpxample', 'A-gapsB-**_--C', 'pBig_gap-mples-between_wo_rds-in_thce', '__Big-Exaple-2', 'm', 'sce', 'EEpxampl', 'xExxEA-xEa', '2xa', 'ExamExaplae', 'mmpleEmexample__Big_gaps-between_words-o_in_thce-1', 'Big_3tenceds-in_thce', 'gap', '-A-B-*---a-a-a---b-b-b-c-c-c---_--C-', 'ExamEA-gapsB-*_---Caple', 'isenn3tenncein_', '-le-', 'me', 'ggasen3tenceinp', 'Ex-Examplxe_2xa', 'BWnnX', 'EEpxampl-', 'tthhcewords', 'A-_B--*_--C', '-le-', 'EEx__a', '-gA-B-*---a-a-a---b-b-b-c-c-c---_--CEExampleaps_A-B-*_--C-', 'bet', '__Big-Exa_1_2_2\nmple\tExample-3-', 'mpl-A-x-', 'thh', '-x_Example-2', 'mplExa_1_2_2_mpsen3tenEExceees', 'A-gapsB--**_--C', '__Big_gaps-between_words-A-xin_thce-fKqrpAGA', '-x_Example-2gap', 'A-gapsB-', 'mm', 'Big_gaps-bet_ween_words-in_this_senbtence', '3tenceds', '2e', '-gaps_A-B-*_--C__msen3tenceinp_thce', '-gaps_A-B-*_--C__msen3tenceinp_thcae', 'mpscelle', 'se3n', 'Exaa', '-A-gapsB-_', 'EEExa_1_2_2_mpl__Big-ExamExaple-2e', 'ExamExbetweenlae', '-Exa_1_2_2\nmple\tE__Big_gaps-between_words-o_in_thce-xample-3', 'isenn3tenncein', '-ExampleEx-Example_2xa_2', 'BWn__Big-XAh', 'ExampleEx', 'ggasen3tenceinpsce', 'Big_gaps-bet_ween_words-in_this_senbtenc-A-gapsB-_e', '-x_ExamEEpxample_2', '__in_thce-', '2Big_gaps-between_words-in_thcee', 'tbet', 'sen3tencte', 'A-gapsB--**_--C_Big_gap-mples-between_words-in_thce', 'Big_gaps-between_wocrds-in_this_sen3tence', '__Big-1_2_2\nmple\tExample-3_', 'sen3tenecein', '2xExa_1_2_2_mpsen3tenceea', 'A-gaps-B-*_*--C', 'isennmpsen3tencee3tenncein_', 'mpsen3tenceeees', 'mpsent3tencee2xa', 'A-gapsB--**_--C_Big_gap-mples-between_words-in_thceEExample', 'betmples', '__Big_ga_ps-between_words-Big_gaps-between_words-in_this_sen3tencein_thce-', 'Exa_1_2_2_mpsen32tencee', 'Big_gaps-between_words-', 'pBiggap', 'mpsen3tenEExceees', 'rds', 'BiBgg', 'mmpleExample__ExampleEx1', 'mmpl__Big_gaps-between_words-o_in_thce-eExample__1', '-ExampExaplele__1_', 'Big_gaps__A-gapsB--**_--C_Big_gap-mples-between_words-in_thce__between_words-', 'Exa_1_2_2__ampsen3tencee', 'mplle', 'se3n-A-gapsB-_-C-', 'Big_gaps-between_words-in_this_sen3tenwce', 'tthhwords', 'pBig_gap-mples_in_thce', 'am-A-gapsB-_ExamExaple', 'BWnXsenbtenceAhX', 'CWSrjljyFR', 'Big_gaps-bet_weens-in_this_senbtenc-A-gapsBmplExa_1_2_2_mpsen3tenEExceees-_e', 'amplmmpleExample__ExampleEx1', 'ttse3n-3tencehhce-Example-2', 'gaa', '-Ethcele__1_', '-Example__2', 'th-Exa_1_2_2\nm3s', '-Exa_1_2_2\nmple\tE__Big_gaps-betwe2Big_gaps-between_words-in_thceeen_words-o_in_thce-xample-3', 'e', '-ExampExaplelea__1_', 'A-gapsB--**_--C_Big_gap-mples-between_words_n-in_thce', 'sen3tenc__Big_gaps-between_words-o_in_thce-te', 'weens', '-A-B--*_--C-mExampleplExa', 'mExampleplExa', 'th-Exa_1_2_2\nmple\tExample-3smp', 'wse3n3ntenceor', 'eExample', 'Exa-ExampExaplele__1_1_2_2__ampsen3tencee', 'isennmpsen3tencee3tennceinbet', 'se3n-A-gap_-C_3__', 'mmpleExample_gA-B-*---a-a-a---b-b-b-c-c-c---_--CEExampleaps_ExampleEx1', 'bets', 'mp', '-A-Bb-c-c-c---_--C-', 'EEpx', '-A-B--_*_--C-mplExa', 'ExamEA-gapsB-*_a--m-Cap', '__Bi-Exaple-2', 'pBig_gap-*_--C-mples-between_wo_rds-in_thce', 'BWnX-Ah', 'xExxEA-xEaExae', 'sen3tenc', 'mmpleExample_p_1', 'tthh', 'isennmpsen3teEExampEle-Example__2ncee3tennceinbet', '__a-', '__Big_gaps-between_wordae-fKqrpAGA', 'BWnX-mmpleExample_p_1Ah', '-Ethcele__1_', 'ebS', 'A-gaps-B-*_*s--C', 'eaxa', 'rrds', 'sece-', 'pBig_gap-*_--C-mples-bet-A-gaps-B-*_*--C-ween_wo_rds-in_thce', 'A**_--C_Big_g_ap-mples-bempl-A-x-hce', 't_Biig_gaps-between_wordshis-in_thce__his', 'ExamExaEple', '-Example-2mpsen3tenceea-', 'BWnXAxExxEA-xEaExaeX-Ethcele__1_', 'ps', 'a', 'isennmpsen3tencee3tennceintbet', 'ExampExaplelea', '-Exa_1_2_2\nmple\tE__Big_gaps-betwe2Big_gaps-between_words_xExxEA-xEaExae-in_thceeen_words-o_in_thce-xample-3', 'pmp', 'n-3tencehhce', 'rNfUBspa', '-Epxample-2-', 'wocrds', '_Ex-Examplxe_2xaA-B-*_--C-mplExa', 'rNfteUBspa', 'Bigmpsent3tencee-in_this_sentence', 'esen3tencempsen3tenEExceee3s-', '-mpl__Big-ExamExaple-2e', 'EEEpx', 't_Biig_gaps-between_wordshis-in_thce_t_his', '-x_xample_2', 'betmeples', 'th-Exa_1_2_2\nm3sBig_gaps-between_words-in_thce', 'te', '__Big-ExamExaple-2ExamExbetweenlae', 'XRSIx', 'BWnXAXhX', '-A-gapsB--ExamEEpxamplemplExa', '__Big-1_2_2\nmple\tEx2ample-3_', 'A-gapsB-B*_--C', 'th-Big-gaps-bet_ween_words-in_this_senbtenc-A-gapsB-_eExa_1_2_2\nmple\tEx__3smp', 'mpsece-lExa', 'tth', '__mpsent3tencee-', 'ExagmEA-gapsB-*_---Caple', 'ggasen3tenp', 'mmpleEsen3tenc__Big_gaps-between_words-o_in_thce-temexample__Big_gaps-between_words-o_in_thce-1', 'm3sBig', 'Exa_1_2_', 'BWnXhceAh', 'smpl-A---a-a-a---b-b-b-c-c-c----x-ece-', 'XBWX', 'A-B-*_-C', '__Big_gaps-betwneen_words-o_in_thce-', '__a-', 'sp', 'mpsen3tenEExceees-', 'EExampEle', 'BWnXAXhEEpxamplX', '3tencehhce', '-A-B--*mm_--C-mExampleplExa', '-gaps--_C__msen3tenceinp_thcae', 'Exa_1_2_2_m_psen3tencee', 'lmmple', 'secn3tExa_1_2_2_mpsent3tenceeencte', 'Exaisennmpsen3tencee3tennceinbet1_2_', '-Exa_1_2_2\nmple\tE__Big_gaps-betwe2Big_gaps-between_words_xExxEA-xEaEhxae-in_thceeen_words-o_in_thce-xample-3', '-Examaple__2', 'tben-3tencehhcebt', 'betmEx-Example_2xaples', 'ebBig_gaps-between_words-in_this_sen3tenceetween', 'A-B-*---a-a-a---b-b-b-c-c-c---_--C', 'senbtenc', 'BWn_i_Big-XAh', 'mmpleEsen3tenc', 'Examplxe', 'th-Exa_1_2_2\nmple\tExampale-3smp', 'tthhX', 'sen3tenwce', 'EExEampEle', 'mpsen33tenceees', '__e_A-B--*mm_--C-mExampleplExa', 'tthhrwords', 'ebese3n-A-gap_-C_3__tsExxEa', 'Big_gaps-between_words-in_this_sebSentencte', '-x_ExamEEpxample_2__Example_2', 'Ex2ample', 'betms', '__Big_gaps-betweentthhcewords_words-o_in_thce-', 'smpl-A---a-a-a---b-b-b-c--c-c----x-ece-', 'm-le-ple', 'BWnXpAXhEEpxamplX', 'mmpleEsen3tenc__Big_gaps-beBWnX-Ahtween_words-o_in_thce-temexample__Big_gaps-between_words-o_in_thce-1', 'gga-A-x-sen3tencce', 'pl-A-B-*_--C__Big_gaps-between_words-in_this_sen3tence-_ee', 'mpsen3ttenceemmpleExample__1s', 'mpsecmpscellee-lExa', 'plmmple', 'lmmpletthhcewords', 'wo__Big-EEExample__1ds', 'Big_gaps-between_words-in_s_sentence', 'am', 'Big_gaps-bet_ween_words-in_tsentence', 'epBig_gap-mples_in_thce', 'psen3tencee', 'A-gapsB--**_s--C', 'Big_gaps-between_words-iExaen_this_sen3tenwce', 'th-Exa_1_2_2\nmmple\tExampale-3smp', 'meaxaplle', '-Exa_1_2_2\nmple\tE__Big_gaps-betwe2Big_gapmpsen3tenEExceees-between_words_xExxEA-xEaExae-in_thceeen_words-o_in_thce-xample-3', 'pBgig', 'A-gap--**_s--C', 'mmmpleExample', 'mExa_1_2_2_mpl__Big-ExamExaple-2ee', 'ExampleEx1', 'ggasenp3tenp', 'XBWXX', 'betwneen', '2hcee', 'BWnplX', '2xExa', 'pBgiBg', 'EA---a-a-a---b-b-b-c-c-c----x2_mpsent3tencee', 't_Biig_gaps__e__between_wordshis-in_thce__his', 'Big__gaps-between_words-in_this_sen3tence', 'bteet', 'mpsen33temmpleEmexample__Big_gaps-between_words-o_in_thce-1nceees', 'BWnAXAh', 'BWnXAXhEEpxampllX', 'senbtence', 'ampl3tencehhcele', 'mfKqrpAGAlpleE1', '-A-gaps-B-*_*Bigmpsent3tencee-in_this_sentence--C_-__', '__Bigi-', 'mmpleExA-_B--*_--Cample_p_1', '-Exa_1_2_2\nmple\tE__Big_gaps-betwe2Big_gaps-between_words_xEx-xEA-xEaExae-in_thceeen_words-o_in_thce-xample-3', 'smpl-A---a-a-a---bisennmpsen3tencee3tenncein-b-b-c--c-c----x-ece-', 'A-Bb-c-c-c---_--C', 'tbsenbtencet', 'Big_gaps-bet_weens-in_this_senbtenc-A-gapsBmplsExa_1_2_2_mpsen3tenEExceees-_e', 'Exaisennmpsen3tencee3tennceinbet1', '-xExxEA-xEaExae__Ethcele__1_', 'Bmpsent3tenceetween_words-', 'A-Bf-*_-mfKqrpAGApleE1C', 'crdsExamplxe', 'betmEx-Epxample_2xaples', 'A-gapsBmplsExa', 'mmmp', '_Big_gaps-between_words-Big-in_', '-A-B--ExamEA-gapsB-rNfUBspa*_---Caple*_--C-mplEx', 'mpsen33temmpleEe-1nceees', 'senbteenc', 'ExapleEx', 'thisebBig', 'mpl-A-C-x-', 'EamExbetwe-Ethcele__1_enlae', 'Exa_1_2_2_mpExample__1__Big-sen3tencee', 'ebBigmp', 'pBig_gap-*_--C-mples-ebSbetween_wo_rds-in_thce', 'E-Ethcele__1_enlae', 'mmmm', 'mpsen3ttenceemmpple', '1nceees']
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(fix_spaces)