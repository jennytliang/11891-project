def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    mem = [0] * (n + 10)
    mem[0] = 0
    mem[1] = 0
    mem[2] = 2
    mem[3] = 0
    for i in range(4, n + 1):
        mem[i] = mem[i - 1] + mem[i - 2] + mem[i - 3] + mem[i - 4] 
    return mem[n]

if __name__ == "__main__":
    import doctest
    doctest.testmod




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
    inputs = [[5], [8], [10], [12], [1], [2], [3], [4], [6], [7], [9], [11], [15], [20], [19], [21], [16], [17], [14], [18], [22], [0], [13], [23], [24], [41], [25], [98], [26], [27], [82], [81], [80], [40], [99], [83], [84], [39], [100], [28], [29], [97], [85], [86], [30], [95], [87], [31], [32], [33], [34], [42], [43], [101], [79], [88], [96], [38], [94], [93], [89], [92], [37], [44], [35], [45], [102], [103], [36], [91], [105], [104], [106], [90], [50], [46], [49], [51], [47], [78], [77], [52], [48], [53], [76], [107], [54], [108], [109], [72], [73], [71], [74], [68], [67], [110], [70], [55], [500], [1000], [999], [998], [997], [1001], [1003], [498], [499], [1004], [1002], [1005], [996], [497], [75], [61], [62], [63], [64], [496], [501], [995], [502], [503], [66], [65], [504], [505], [495], [494], [493], [492], [1006], [491]]
    results = [4, 28, 104, 386, 0, 2, 0, 2, 8, 14, 54, 200, 2764, 73552, 38158, 141776, 5328, 10270, 1434, 19796, 273282, 0, 744, 526768, 1015378, 71083647136, 1957204, 1250966502919879120640717716, 3772632, 7271982, 34443880418283540493826, 17869142915445859640640, 9270333790937632951616, 36877489824, 2411315463631208843587520078, 66392714182364268855232, 127976071307031301941314, 19131675294, 4647959998589498844128566416, 14017196, 27019014, 648988991706202294407873694, 246681808823124970931012, 475494474730804082221384, 52080824, 174670928672918843046473740, 916545069043324623948942, 100389016, 193506050, 372994904, 718970794, 137018135298, 264110947552, 8959230956846789102764677904, 4809357057697235769150, 1766697423904284979042652, 336689040332208585492454928, 9925323044, 90617542208549397693915354, 47011480492525468175029672, 3405418776501538656143990, 24389088958214876577036162, 5149158974, 509090219810, 1385860764, 981302949796, 17269472921987375911121482114, 33287979341054872701602246512, 2671332512, 12652817013629100600492552, 123681326438367574275105379476, 64164643218478536559616972946, 238403421919888359447446081048, 6564155744179952341356968, 26112283777288, 1891522252456, 13546793363542, 50333045302120, 3646026369614, 2495046654202812132420, 1294405412608178787454, 97020064234626, 7027941791676, 187012186677576, 671524666429406262592, 459537370917789342983770679982, 360477579991610, 885786762494523813265939113452, 1707408881770569089972261253958, 48643920250633737730, 93764171013545442488, 25235982484270910776, 180736250708388495690, 3523669487722032972, 1828044717908083822, 3291136437102770605669417128440, 13092176959938404696, 694842876205932, 4683845716690180034539796272188497123185499535401362646845638880052842590096588363096828154816550799073811944964910934796641232183050271821520, 149547043138259727015096384049610726618726804255794097638599078041110780764071741229530332670686964029765482703354480554521159825599963893124385760545082454600686514973757585648968777570336074773234360071278282617747789932964133310884195664597309999155447895565685043713734470810760608, 77583520032237968378587772618535425191575509913567987406119797373147019391141324256620017416750041382241767216536494841318892788001313694598614670005755267502315822069599137802752127730223321831560623251004298203410859790833345184696271852051551460321923245189808074836212476262156702, 40249559297723974715950079949236002430423945312197229647912606593547214097941112719064962932043733178089331278072189769895020129777472120871317950997807774945333074946921261024265735148789247464604010734681176533935854869165969698579556028006971105202695520676040537458395870328044580, 20881071430992498667558244139656152882585768203969115040911834833913116975392307981894700746216590605092816576288374798734592196516503879341118163838572588798407063645105670133951386864673677825226510909176969097722740096660032751809964571919869313422436487989492763654846654794753086, 288261193899214168777192480757038307123312027685528429733543316841718131228546486187110013765697329195189397774251539964469664939895253587935436545387218085846742475635383654609938027314022321894625504966140726452817244689623480945969988116575701878102503149421026419663189472195714976, 1071033073437147703057703354799604920297652629021978259204436991105499076865460216065585690638312402392482626666357220490514455236770534472188191902873919390844822700304402017147583600377952684463444987311527791081887643696007888581680467294456097780362444101029079613884668708865309152, 1260624897417852625576044478298372128943521210742654024395221969632329136735782024940759454196815727303904706725268739805145177720572093582036, 2429932617609716069359946151595027889475026810784174006789181732198363225711635311383050097118386585780077976807725696990168782893560829719694, 2064482626842057437736818936980674415403729748130388531002754184837851134339779107874551363859874763402723486116177946139710017685539755249777769135742083514187329578539204896492415073025682047095329351372051283960364427601182431978664662736860644100402964956868351152933124941468461602, 555641316367435838886826717374420461364038287167087744426174798849523145481700664392325326785178067785285978972214705130204737683274003296529754926935863582895077887625661639085924667763370965964024499023104483807911749282586929140130011661231534442782569810852560075671532289596676866, 3979418210545855148458541489911738104188732692004982964366909291634591487915486474519572395049062562775681489529001411724898875545479546606431152510939084573773972642104652207335861368481028019417424342672824285302981065269400730646445129809123978201650482018171017262152515412126162596, 10832892377305285253000287342183146114141580826059765543654839240503430299596996271950651575676598864341567632457421144572654711304674198313334975702946823354630554312131516687999527826649827651843215176415838782678335176304785675798403212618918120208392641710343667764279469425806240, 653999670802812778855740732101389822158818576116982074644494772348569232802626450747381246319643705608563299128770307309056746543387968893726, 348380324456838586684, 35639919326849136, 68698153303713410, 132419948094134672, 255247656741676658, 339288530859798560748064910193707282608132937757552541016740405873580994846544576025637357181704780381265962303146190692270525025529379626064, 9028402902520561508331527634183286963762866133045172752674537354232104185346632150168018952451396817766357927626675678901011939340571164016976, 5619996926216209742079161187460123764424215571341877173640516705183258018210907283709702162813118734718051729718509128116625750402663496072843579466428080403945129165440689956535477890110568889886886430730313789073929648702557058508348039505792921488398594813931105958690481713552796, 17402806134238310237807314536265184105366913689973363430704579936115639137890637849588656658583149929924152556124581050492967132137754359140226, 33544987371058767850038584594231996081790306169204072837013937902598949139045493674236553862969484132544400405523893361180789086554936624698416, 948371435605898616, 492005677466373876, 64660042124507819630717223036868964274105585527623971667238694072999535052379352037090057628820581679308722834240061025371409390216312419677138, 124636238532325459226894649801549431425025671519846580687631749265946227514662115711083287102824612559543633723515211115946177548249574567532756, 176019518529252104180096031001558655764554086166985366732724584343883861326682259669272039420222372486344008650540459183696333604071387617868, 91317177225989181792142805001716368412015610701134042001262207066295047759928738498468811275244868827731436642811782620121572547583357444378, 47374444187772932135436985904407515374115941491310124893767575064809328869470876554003038442471683913221891532271874812968315366203844205416, 24577390916784342640389088286024743057447299398123007388986039398592756890462701303893468043765855153968625477522074075484303507670790358402, 7670575227192496128139890499066437901254153356324437499000275266427464844602426462852034776332427796356173581283751283485328086151063839624926868476490951061701202808573920760061784709648033716940223180379507844153144885849177980346920271501672254525198460886921008104641841352056610216, 12750506198705647612127151809410028920975234576418192448708762814186727806819943312906721658739964591422054997934727675122142182613395609672]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(fib4)