def fruit_distribution(s,n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for examble:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
    """
    print("s: {} type: {} len: {} n {}".format(s,type(s),len(s),n) )
    splitted = s.split(' ')
    
    #get only the integers
    # splited = ['5','apples','6','orange',',']  #list of string 6 strings in this example
    count_apples = [i for i in splitted if i.isnumeric()[0]]
    count_apples = ''.join(count_apples)
    count_apples_int = (10**len(count_apples))-1 #get the largest number possible like if 3333 return int(3) for example 233 will be int(233)
    # 1230036410059174984451914789736945244542379458911444419035190291031231221022323128473487634897349868847349834958648634367468786758646344675789678667467835473543678473647364543675736457987867647684776476786758463647576457368584784676367485678476367847678547657367764776578679889797987646786776998764799678476466478975678964678674699864656748677648467468684676848674686469986678566469986466999868998586768699676997999967656598564655955456465465967468569564646568666469856468564864856986456454646456466456645367689646799999565646856456895645685956568569648468564985646895698586985966959586966985966566596655655646664646648648586645856656964569695646965696646485665856656956468464895665868956469566569656656464566599866566485665565956956695866569985669566466459566646569998656695596696696685665656665645656466465665666568695646 